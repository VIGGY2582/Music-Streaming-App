from fastapi import APIRouter
from app.services.youtube_service import YouTubeService

router = APIRouter()

youtube_service = YouTubeService()


@router.get("/search")
def search_song(q: str):
    return youtube_service.search(q)