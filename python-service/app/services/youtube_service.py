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