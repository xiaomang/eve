import time

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from dependencies import remote_ip

router = APIRouter()


class FindResponse(BaseModel):
    ip: str
    curr_time: float


@router.get(path='/', name='默认首页', response_model=FindResponse)
async def find(
    ip: str = Depends(remote_ip),
):
    res = {
        'ip': ip,
        'curr_time': time.time(),
    }
    return res
