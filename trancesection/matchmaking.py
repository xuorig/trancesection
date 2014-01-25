import soundcloud

from apiclient.discovery import build
from apiclient.errors import HttpError

YOUTUBE_EMBED_URL = '<iframe id="ytplayer" type="text/html" width="640" height="390" src="http://www.youtube.com/embed/%s?autoplay=0&origin=http://trancesection.edm" frameborder="0"/>'
soundcloudclient = soundcloud.Client(client_id='e926a44d2e037d8e80e98008741fdf91')

class Track:
  pass

class YoutubeTrack(Track):
  def __init__(self,title,id):
    self.title = title
    self.id = id

  def get_embed_url(self):
    return YOUTUBE_EMBED_URL % self.id

class SoundCloudTrack(Track):
  def __init__(self,title,uri):
    self.title = title
    self.uri = uri

  def get_embed_url(self):
    return soundcloudclient.get('/oembed', url=self.uri).html

# API STUFF #############################################################################
DEVELOPER_KEY = "AIzaSyAqHvolBIvx6h1CbttV3Qw-0RdhOMs6Jt8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(track_name):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=track_name,
    part="id,snippet",
    maxResults=10
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(YoutubeTrack(search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))

  return videos


def soundcloud_search(track_name):
  sc = soundcloudclient.get('/tracks', q=track_name)
  print 'sc'
  print sc
  tracks = [SoundCloudTrack(t.title,t.uri) for t in sc]
  return tracks

###########################################################################################

IGNORED_TOKENS = [
  "[",
  "]",
  "(",
  ")",
  "-",
  "vs",
  "feat",
  "featuring"
]  

def title_score(track_name, possible_match):

  match_title = possible_match.title

  #Make sure caps dont make results wrong
  track_name = track_name.lower()
  match_title = match_title.lower()

  for ignore in IGNORED_TOKENS:
    track_name.replace(ignore,"")
    match_title.replace(ignore,"")

  t = track_name.split()
  m = match_title.split()

  score = len(set(t).intersection(set(m)))

  #return a tuple (score, object)
  return (score,possible_match)

def get_best_title_score(track_name,track_list):

  if track_list == None:
    return None

  score_results = map(lambda x: title_score(track_name, x),track_list)

  #by default, max() will give us the first max he finds,
  #luckily this is what we want cause we trust the API's 
  #in their index choice.
  return max(score_results,key=lambda x: x[0])

def find_match(track_name):

  # Get our tracks ready for the scoring
  soundcloud_tracks = soundcloud_search(track_name) or None
  youtube_tracks = youtube_search(track_name) or None

  #Now get the best score for each type (For now just SoundCloud and YouTube)

  #Score according to title
  youtube_best_title_score = get_best_title_score(track_name,youtube_tracks)
  soundcloud_best_title_score = get_best_title_score(track_name,soundcloud_tracks)


  if youtube_best_title_score and soundcloud_best_title_score:
    overall_best_score = max(youtube_best_title_score,soundcloud_best_title_score,key=lambda x: x[0])

    # If the best on each site has the same score, we have to make a desision,
    # Lets take soundcloud cause its cooler.
    if youtube_best_title_score[0] == soundcloud_best_title_score[0]:
      overall_best_score = soundcloud_best_title_score

  else:
    overall_best_score = youtube_best_title_score or soundcloud_best_title_score

  if overall_best_score == None:
    return "Could not find a match for this track :("
  else:
    print overall_best_score
    return overall_best_score[1].get_embed_url()



  #TODO: Score according to length (cluster)