from yt_dlp import YoutubeDL


class YouTubeService:

    def search(self, query: str):

        ydl_opts = {
            "quiet": True,
            "extract_flat": True
        }

        with YoutubeDL(ydl_opts) as ydl:

            result = ydl.extract_info(
                f"ytsearch10:{query}",
                download=False
            )

            songs = []

            if "entries" not in result:
                return songs

            for video in result["entries"]:

                songs.append(
                    Song(
                        videoId=video.get("id"),
                        title=video.get("title"),
                        artist=video.get("channel"),
                        thumbnail=video.get("thumbnails", [{}])[-1].get("url"),
                        duration=str(video.get("duration"))
                    )
                )

            return songs

    def get_stream(self, video_id: str):

        url = f"https://www.youtube.com/watch?v={video_id}"

        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio/best"
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                url,
                download=False
            )

            return {
                "videoId": info.get("id"),
                "title": info.get("title"),
                "artist": info.get("channel"),
                "thumbnail": info.get("thumbnail"),
                "duration": info.get("duration"),
                "streamUrl": info.get("url")
            }