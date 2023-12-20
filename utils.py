from typing import Any

from bson import ObjectId
from pymongo.cursor import Cursor


def bson_dumps(o: Any) -> Any:
    if isinstance(o, ObjectId):
        return str(o)
    elif isinstance(o, (list, Cursor)):
        return [bson_dumps(x) for x in o]
    elif isinstance(o, dict):
        buf = {}
        for k, v in o.items():
            buf['id' if k == '_id' else k] = bson_dumps(v)
        return buf
    else:
        return o
