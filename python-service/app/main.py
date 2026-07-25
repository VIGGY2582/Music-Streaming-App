from fastapi import FastAPI
from app.routes.search import router as search_router
from app.routes.stream import router as stream_router

app = FastAPI(
    title="Music Streaming Python Service",
    version="1.0.0"
)

app.include_router(search_router)
app.include_router(stream_router)


@app.get("/")
def home():
    return {
        "message": "Python Service is Running Successfully!"
    }