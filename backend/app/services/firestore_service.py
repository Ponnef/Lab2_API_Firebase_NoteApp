from datetime import datetime, timezone
from app.core.firebase_config import get_firestore
from firebase_admin import firestore


_db = None

def get_db():
    global _db
    if _db is None:
        _db = get_firestore()
    return _db

def save_note(uid: str, title: str, content: str):
    db = get_db()
    doc_data = {
        "title": title,
        "content": content,
        "created_at": datetime.now(timezone.utc)
    }
    db.collection("users").document(uid).collection("notes").add(doc_data)
def load_notes(uid: str) -> list[dict]:
    """
    Lấy danh sách ghi chú của user, sắp xếp theo thời gian tạo mới nhất.
    """
    db = get_db()
    docs = db.collection("users").document(uid).collection("notes")\
             .order_by("created_at", direction="DESCENDING").stream()
             
    # Ép kiểu dữ liệu Firestore Document thành dictionary và gộp id vào
    return [{**d.to_dict(), "id": d.id} for d in docs]