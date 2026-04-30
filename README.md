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
   ```

2. Cài đặt thư viện:
   ``` bash
   pip install -r requirements.txt
   ```
3. Tạo thêm file `secret.toml` trong folder frontend
   ``` bash
   [firebase_client]
   #to do
   [firebase_admin]
   #to do
   [google-login]
   #to do
   111

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

### **🎥 Video demo**
