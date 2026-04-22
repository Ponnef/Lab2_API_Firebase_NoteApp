from fastapi import FastAPI
from app.routers import auth, notes



app = FastAPI(title="Note App API")

app.include_router(auth.router)
app.include_router(notes.router)
# Yêu cầu Lab: Endpoint GET / và GET /health
@app.get("/")
def read_root():
    return {"message": "Welcome to Note App API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(auth.router)
app.include_router(notes.router)