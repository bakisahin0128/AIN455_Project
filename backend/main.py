from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# /static yolunu static klasörüne bağla
app.mount("/static", StaticFiles(directory="static"), name="static")

# "/" isteğinde index.html dön
@app.get("/")
def read_index():
    return FileResponse(os.path.join("static", "index.html"))
