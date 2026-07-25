from fastapi import APIRouter, HTTPException
from app.services.youtube_service import YouTubeService

router = APIRouter()

youtube_service = YouTubeService()


@router.get("/stream/{video_id}")
def get_stream(video_id: str):

    try:
        return youtube_service.get_stream(video_id)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to resolve audio stream"
        )