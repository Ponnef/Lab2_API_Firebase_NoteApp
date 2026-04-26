import os
import toml
import firebase_admin
import pyrebase
from firebase_admin import credentials, firestore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SECRETS_PATH = os.path.join(BASE_DIR, "frontend", ".streamlit", "secrets.toml")

try:
    secrets = toml.load(SECRETS_PATH)
except FileNotFoundError:
    raise Exception(f"Không tìm thấy file secrets tại: {SECRETS_PATH}")

def get_pyrebase_auth():
    firebase_cfg = secrets.get("firebase_client", {})
    firebase_app = pyrebase.initialize_app(firebase_cfg)
    return firebase_app.auth()

def init_firebase_admin():
    if not firebase_admin._apps:
        cred_dict = dict(secrets.get("firebase_admin", {}))
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)

def get_firestore():
    init_firebase_admin()
    return firestore.client()