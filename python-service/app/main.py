from fastapi import FastAPI

app = FastAPI(
    title="Music Streaming Python Service",
    description="Handles YouTube search and streaming using yt-dlp",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Python Service is Running Successfully!"
    }