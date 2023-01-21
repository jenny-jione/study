from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
async def root():
    return {"message":"i am jenny"}

@app.get('/view/')
async def syswow():
    import os
    path = os.getcwd()
    result = os.listdir(path)
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)
    