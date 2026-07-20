from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_response_type
from ...common.enums import ResponseType
from ...common.types.dtos import ChatRequest, ChatResponseJson, ChatResponseNdjson, GenerateRequest, GenerateResponseJson, GenerateResponseNdjson

router = APIRouter(
    tags=["inference"],
    responses={
        500: {"description": "Internal server error."},
        503: {"description": "API overloaded, try again later."}
    }
)
"""
Defines the handlers for API routes related to inference:
- `/generate`
- `/chat`
"""

@router.post(
        "/generate",
        responses={
            200: {
                "content": {
                    "application/json": {"schema": GenerateResponseJson.model_json_schema()},
                    "application/x-ndjson": {"schema": GenerateResponseNdjson.model_json_schema()}
                }
            }
        })
async def generate(request: GenerateRequest, format_type: ResponseType = Depends(get_response_type)):
    """ Handler for `/generate` API. Provides basic one-off prompt functionality from LLM. """
    raise HTTPException(status_code=500, detail="API not functional.")

@router.post(
        "/chat",
        responses={
            200: {
                "content": {
                    "application/json": {"schema": ChatResponseJson.model_json_schema()},
                    "application/x-ndjson": {"schema": ChatResponseNdjson.model_json_schema()}
                }
            }
        })
async def chat(request: ChatRequest, format_type: ResponseType = Depends(get_response_type)):
    """ Handler for `/chat` API. Provides chat-like prompting with message history and tool use. """
    raise HTTPException(status_code=500, detail="API not functional.")
