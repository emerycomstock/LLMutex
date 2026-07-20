from fastapi import Header
from ..common.enums import ResponseType

def get_response_type(accept: str = Header("application/x-ndjson")):
    if "application/x-ndjson" in accept:
        return ResponseType.JSON_STREAM
    if "application/json" in accept:
        return ResponseType.JSON
    return ResponseType.UNSUPPORTED