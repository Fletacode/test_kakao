from fastapi import FastAPI, HTTPException, Header
import os

app = FastAPI()

@app.get("/")
async def root():
    return {
  "version": "2.0",
  "template": {
    ...
  },
  "context": {
    ...
  },
  "data": {
    ...
  }
}


if __name__ == "__main__":
    import uvicorn
 
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)