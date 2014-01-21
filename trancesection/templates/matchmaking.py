import soundcloud

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))

  return videos


 def soundcloud_search(track_name):
 	soundcloudclient = soundcloud.Client(client_id='e926a44d2e037d8e80e98008741fdf91')
 	tracks = soundcloudclient.get('/tracks', q=track_name)
 	return tracks

def get_length_score(track_name):
	pass


def get_best_title_score(track_name):
	matches = soundcloud_search(track_name)
	score_results = map(lambda x: title_score(track_name, x),matches)
	best = max(score_results)

def title_score(track_name, possible_match):

	tracks = (track_name,possible_match)
	for t in tracks:
		t.replace("[","")
		t.replace("]","")
		t.replace("(","")
		t.replace(")","")
		t.replace("-","")
		t.replace("vs","")
		t.replace("feat","")

		t = t.split()

	track_name set(tracks[0])
	possible_match = set(tracks[1])

	return len(track_name.intersection(possible_match))

