import json
import requests
import traceback
from tqdm import tqdm 

class YTstats:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None 
        self.video_data = None

    def get_channel_statistics(self):
        """
        Extract the channel statistics.
        """
        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0]['statistics']
        except KeyError:
            print(f"Could not get the channel statistics")
            data = {}
        
        self.channel_statistics = data
        return data
    
    def get_channel_video_data(self):
        """
        Extract all the videos on the channel
        """
        #1 - Get vidoe ids
        channel_videos = self._get_channel_videos(50)
        # print(channel_videos) 

        #2 - Get the video statistics
        
        parts = ["snippet","statistics","contentDetails"]
        # channel_videos2 = ["07Pxa3TbQc4", "du8vQC44PC4"]
        for video_id in tqdm(channel_videos):
            for part in parts:
                data = self._get_single_channel_video_data(video_id, part)
                channel_videos[video_id].update(data)
        self.video_data = channel_videos
        return channel_videos

    def _get_single_channel_video_data(self, video_id, part):
        url = f'https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}'
        json_url = requests.get(url)
        data = json.loads(json_url.text) # json data convert into python dictionary 
        try:
            data = data['items'][0][part]
        except KeyError as e:
            print(e)
            data = dict()
        
        return data

    def _get_channel_videos(self, limit=None):
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=snippet,id&order=date'
        
        if limit is not None and isinstance(limit, int):
            url += '&maxResults=' + str(limit)
        
        channel_videos, nextPageToken = self._get_channel_videos_per_page(url)
        idx = 0
        while nextPageToken is not None and idx < 10:
            next_url = url + "&pageToken=" + nextPageToken
            next_channel_videos, nextPageToken = self._get_channel_videos_per_page(next_url)
            channel_videos.update(next_channel_videos)
            idx += 1 
        return channel_videos

    def _get_channel_videos_per_page(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()
        item_data = data['items']
        nextPageToken = data.get("nextPageToken", None)
        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == "youtube#video":
                    videoId = item['id']['videoId']
                    channel_videos[videoId] = dict()
            except Exception:
                traceback.print_exc()

        return channel_videos, nextPageToken

    def dump(self):
        """
        Dumps the channel statistics into json file.
        """

        if self.channel_statistics is None or self.video_data is None:
            print("Data is None.")
            return 
        fused_data = {self.channel_id: {"channel_statistics": self.channel_statistics, "video_data": self.video_data}}
        print(list(self.video_data.values())[0].get('channelTitle'))
        
        # channel_title = self.video_data.popitem()[1].get('channelTitle', self.channel_id)
        channel_title = str(list(self.video_data.values())[0].get('channelTitle'))
        channel_title = channel_title.replace(" ", "_").lower()
        filename = channel_title + '.json'
        with open(filename, "w") as file:
            json.dump(fused_data, file, indent=4)

