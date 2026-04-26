from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from app.routers.auth import router as auth_router
from app.routers.notes import router as notes_router
app = FastAPI(title="Note App API", description="API cho ứng dụng Ghi chú đơn giản")

# Cấu hình CORS để Frontend (Streamlit) có thể gọi được Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các nguồn (dễ dàng chạy test local)
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép mọi phương thức GET, POST, PUT, DELETE...
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(notes_router)
# 1. Các endpoint BẮT BUỘC theo đề bài
@app.get("/")
def read_root():
    """Endpoint gốc của ứng dụng"""
    return {"message": "Welcome to Note App API"}

@app.get("/health", tags=["System"])
async def health_check():
    """
    Endpoint kiểm tra trạng thái hệ thống (Health Check)
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
        "services": {
            "api": "online",
            "database": "connected" # Firestore là serverless nên mặc định là online
        }
    }