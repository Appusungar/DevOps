from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

app = FastAPI(title="VisionAI Backend")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production!
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "VisionAI Backend is running!"}

@app.post("/api/test-upload")
async def test_upload(file: UploadFile = File(...)):
    """Simple endpoint to test if upload works"""
    # Read the image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    # Get basic info
    width, height = image.size
    format = image.format
    
    return {
        "filename": file.filename,
        "size": f"{width}x{height}",
        "format": format,
        "message": "Upload successful! No ML yet."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)