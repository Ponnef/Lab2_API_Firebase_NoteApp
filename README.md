# 📝 PonNote - Lab 2: API & Firebase
### Thông tin sinh viên
* ### Họ và Tên: Nguyễn Huỳnh Gia Bảo
* ### MSSV: 24120264
* ### Lớp/Khóa: 24CTT3/K24
* ### Ứng dụng ghi chú cá nhân sử dụng **FastAPI** (Backend) và **Streamlit** (Frontend) tích hợp xác thực Google.

* ### PonNote là một ứng dụng ghi chú cá nhân được xây dựng theo mô hình Client-Server. Ứng dụng cho phép người dùng đăng nhập an toàn và quản lý các ghi chú của mình trên nền tảng đám mây, đảm bảo dữ liệu luôn được đồng bộ và truy cập được mọi lúc, mọi nơi.

## 🛠️ Hướng dẫn cài đặt Environment

1. Clone dự án:
   ```bash
   git clone https://github.com/Ponnef/Lab2_API_Firebase_NoteApp
   cd Lab2_API_Firebase_NoteApp
   python -m venv .venv
   ```

2. Cài đặt thư viện:
   ``` bash
   pip install -r requirements.txt
   ```
3. Tạo thêm file `secret.toml` trong folder frontend
   ``` bash
   [firebase_client]
   apiKey = "YOUR_FIREBASE_WEB_API_KEY"
   authDomain = "YOUR_PROJECT.firebaseapp.com"
   projectId = "YOUR_PROJECT_ID"
   storageBucket = "YOUR_PROJECT.appspot.com"
   messagingSenderId = "YOUR_SENDER_ID"
   appId = "YOUR_APP_ID"
   
   [firebase_admin]
   type = "service_account"
   project_id = "YOUR_PROJECT_ID"
   private_key_id = "YOUR_PRIVATE_KEY_ID"
   private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
   client_email = "firebase-adminsdk-xxx@YOUR_PROJECT_ID.iam.gserviceaccount.com"
   client_id = "YOUR_CLIENT_ID"
   auth_uri = "https://accounts.google.com/o/oauth2/auth"
   token_uri = "https://oauth2.googleapis.com/token"
   auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
   client_x509_cert_url = "YOUR_CLIENT_X509_CERT_URL"
   universe_domain = "googleapis.com"
   
   [google-login]
   frontend_url = "http://localhost:8501"
   google_client_id = "YOUR_GOOGLE_CLIENT_ID"
   google_client_secret = "YOUR_GOOGLE_CLIENT_SECRET"
   google_redirect_uri = "http://localhost:8501"
   google_scopes = "openid email profile"
   cors_origins = "http://localhost:8501"
   ```

## Hướng dẫn chạy Backend
1. Đảm bảo bạn đã có file `backend/serviceAccountKey.json` từ Firebase Console

2. Di chuyển đến thư mục backend:
   ```bash
   cd backend
   ```
3. **Khởi chạy Server:**
   ```bash
   uvicorn app.main:app --reload
   ```
## Hướng dẫn chạy Frontend

1. Đảm bảo có file `frontend/.streamlit/secrets.toml` đã được cấu hình đầy đủ Client ID và API Key.

2. **Di chuyển đến thư mục frontend:**
   ```bash
   cd frontend
   ```
3. **Khởi chạy ứng dụng:**
   ```bash
   streamlit run app.py
   ```
Ứng dụng sẽ tự động mở trên trình duyệt tại: http://localhost:8501
## **Cấu trúc thư mục:**
### **Backend:**
``` bash
backend/app/
├── core/
│   ├── firebase_config.py # Khởi tạo Firebase Admin/Pyrebase
├── dependencies/
│   ├── auth_dependencies.py # xác thực Firebase ID token
├── routers/
│   ├── auth.py
│   ├── notes.py
├── schemas/
│   ├── auth_schemas.py 
│   ├── note_schemas.py
├── services/
│   ├── firestore_service.py # Tương tác Firestore, xử lí dữ liệu, thống kê hệ thống.
└── main.py # Khởi tạo FastAPI app
```
### **Frontend:**
``` bash 
frontend/app/
├── .streamlit/
│    ├── secrets.toml
├── api_client.py
│
└── app.py
```
### **[🎥 Video demo] (https://drive.google.com/file/d/1FMI1TrbBpy7Qer7qiTewV2GhvAPPzNz6/view?usp=sharing)**

