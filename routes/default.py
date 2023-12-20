from fastapi import APIRouter, Depends
from pymongo.database import Database

from dependencies import DB

router = APIRouter()


@router.get(path='/', name='默认首页')
async def default(
    db: Database = Depends(DB),
):
    user_col = db.get_collection('users')
    res = {
        'data': list(user_col.find({}, {'_id': False, 'password': False, 'ua': False}))
    }
    return res
