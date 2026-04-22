from datetime import datetime, timezone
from app.core.firebase_config import get_firestore
from firebase_admin import firestore

_db = None

def get_db():
    global _db
    if _db is None:
        _db = get_firestore()
    return _db

def save_note(uid: str, title: str, content: str, summary: str):
    db = get_db()
    doc = {
        "title": title,
        "content": content,
        "summary": summary,
        "created_at": datetime.now(timezone.utc)
    }
    db.collection("users").document(uid).collection("notes").add(doc)

def load_notes(uid: str):
    db = get_db()
    docs = db.collection("users").document(uid).collection("notes")\
             .order_by("created_at", direction=firestore.Query.DESCENDING).stream()
    return [{**d.to_dict(), "id": d.id} for d in docs]