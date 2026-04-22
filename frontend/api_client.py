import requests

API_BASE = "http://localhost:8000"

def signup(email: str, password: str):
    r = requests.post(f"{API_BASE}/auth/signup", json={"email": email, "password": password})
    r.raise_for_status()
    return r.json()

def login(email: str, password: str):
    r = requests.post(f"{API_BASE}/auth/login", json={"email": email, "password": password})
    r.raise_for_status()
    return r.json()

def google_login(id_token: str):
    r = requests.post(f"{API_BASE}/auth/google", json={"id_token": id_token})
    r.raise_for_status()
    return r.json()
def get_notes(id_token: str):
    """Yêu cầu: Hiển thị dữ liệu đã lưu [cite: 100]"""
    r = requests.get(
        f"{API_BASE}/notes",
        headers={"Authorization": f"Bearer {id_token}"}
    )
    r.raise_for_status()
    return r.json()

def create_note(id_token: str, title: str, content: str):
    """Yêu cầu: Nhập dữ liệu cho feature chính """
    r = requests.post(
        f"{API_BASE}/notes",
        json={"title": title, "content": content},
        headers={"Authorization": f"Bearer {id_token}"}
    )
    r.raise_for_status()
    return r.json()