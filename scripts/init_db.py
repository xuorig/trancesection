from trancesection import db
from trancesection.models import Podcast

# Add new podcasts here!
PODCASTS = [{'name':'Group Therapy','author':'Above & Beyond','imgurl':'http://www.aboveandbeyond.nu/sites/www.aboveandbeyond.nu/themes/abv2/images/blocks/tatw450/gtfacts/gt_radio_logo_570x430.jpg'},
			{'name':'International Departures','author':'Myon and Shane54','imgurl':'http://a3.mzstatic.com/us/r30/Podcasts/v4/07/96/33/0796339a-d060-20f0-1516-a2bed68f55ef/mza_234808192339220016.600x600-75.jpg'},
			{'name':'Future Sounds Of Egypt','author':'Aly and Fila','imgurl':'http://www.audioreligion.co.uk/wp-content/uploads/2012/07/FSOE-220x220.jpg'},
			{'name':'A State Of Trance','author':'Armin Van Buuren','imgurl':'http://www.youredm.com/wp-content/uploads/2012/10/asot600-armin-van-buuren-youredm-1024x582.png'},
			{'name':'Trance Around The World','author':'Above & Beyond','imgurl':'http://4.bp.blogspot.com/-O2ErAnCYjn0/UJbf_rhe-eI/AAAAAAAAAYw/fPN8a85iSfM/s1600/Logo%2BTATW.jpg'}
]


def main():
	db.create_all()
	for podcast in PODCASTS:
		pod = Podcast(podcast['name'],podcast['author'],podcast['imgurl'])
		db.session.add(pod)

	db.session.commit()
	db.session.close()


if __name__ == "__main__":
	main()