from pydantic import BaseModel


class Song(BaseModel):
    videoId: str | None = None
    title: str | None = None
    artist: str | None = None
    thumbnail: str | None = None
    duration: str | None = None