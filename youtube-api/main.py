from youtube_statistics import YTstats

# API_KEY = "AIzaSyCQm4GVgvjcL9py7dRMRyQbbQ7lvo_NUNg"
API_KEY = "AIzaSyDWnu79suHr3doi_0KN1VoURCGpklaBdX0"
CHANNEL_ID = "UCbXgNpp0jedKWcQiULLbDTA"

yt = YTstats(API_KEY, CHANNEL_ID)
yt.get_channel_statistics()
# yt._get_channel_videos(50)
yt.get_channel_video_data()
# yt._get_channel_videos_per_page(url)
yt.dump()