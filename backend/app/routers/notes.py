from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.auth_dependencies import get_current_user
from app.schemas.note_schemas import NoteRequest, NoteResponse 
from app.services.firestore_service import save_note, load_notes

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("")
def create_user_note(payload: NoteRequest, user=Depends(get_current_user)):
    try:
        save_note(user["uid"], payload.title, payload.content)
        return {"message": "Lưu ghi chú thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("", response_model=list[NoteResponse])
def get_user_notes(user=Depends(get_current_user)):
   
    return load_notes(user["uid"])