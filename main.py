import uvicorn
from fastapi import FastAPI
import routes.default

app = FastAPI(
    debug=False,
    version='1.0.0',
    title='EVE',
    description='也不知道要做什么，写着玩吧',
)

app.include_router(routes.default.router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
