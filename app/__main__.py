import settings
from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.post("/")
def root():
    return {"Hello": "World_post"}

@app.get("/")
def root():
    return {"Hello": "World_get"}    

if __name__ == '__main__':
    uvicorn.run("__main__:app", host=settings.APP_HOST, port=settings.APP_PORT, log_level="debug", workers=1, reload=False, debug=False)