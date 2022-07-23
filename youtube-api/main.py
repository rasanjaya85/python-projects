from youtube_statistics import YTstats

API_KEY = "xxxxxxxxxxxxxxxxxxx"
CHANNEL_ID = "UCbXgNpp0jedKWcQiULLbDTA"

yt = YTstats(API_KEY, CHANNEL_ID)
yt.get_channel_statistics()
# yt._get_channel_videos(50)
yt.get_channel_video_data()
# yt._get_channel_videos_per_page(url)
yt.dump()