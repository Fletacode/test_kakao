from fastapi import FastAPI, HTTPException, Header
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World", "status": "ok"}

if __name__ == "__main__":
    import uvicorn
 
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)