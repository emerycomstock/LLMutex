from fastapi import APIRouter, HTTPException

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

@router.post("/generate")
async def generate():
    """ Handler for `/generate` API. Provides basic one-off prompt functionality from LLM. """
    raise HTTPException(status_code=500, detail="API not functional.")

@router.post("/chat")
async def chat():
    """ Handler for `/chat` API. Provides chat-like prompting with message history and tool use. """
    raise HTTPException(status_code=500, detail="API not functional.")
