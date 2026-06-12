from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)