class YouTubeService:

    def search(self, query: str):
        return [
            {
                "videoId": "abc123",
                "title": f"{query}",
                "artist": "Dummy Artist",
                "thumbnail": "https://dummyimage.com/300x300",
                "duration": "3:25"
            }
        ]