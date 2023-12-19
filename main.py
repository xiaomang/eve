import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI(
    debug=True,
    version='1.0.0',
    title='EVE',
    description='也不知道要做什么，写着玩吧',
)


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient()
    app.db = app.mongodb_client['eve']


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@app.get(path='/', name='默认首页')
async def default():
    return {}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
