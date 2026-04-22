from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.auth_dependencies import get_current_user
from app.schemas.note_schemas import NoteRequest
from app.services.firestore_service import save_note, load_notes
from app.services.ollama_service import summarize_note

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("")
def create_user_note(payload: NoteRequest, user=Depends(get_current_user)):
    try:
        # Tích hợp Ollama tóm tắt (Feature thông minh)
        summary = summarize_note(payload.content)
        save_note(user["uid"], payload.title, payload.content, summary)
        return {"message": "Note saved successfully", "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("")
def get_user_notes(user=Depends(get_current_user)):
    return load_notes(user["uid"])