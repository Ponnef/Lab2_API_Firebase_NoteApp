import streamlit as st
from api_client import signup, login, google_login, get_notes, create_note

st.set_page_config(page_title="Note App", page_icon="📝", layout="centered")

if "user" not in st.session_state:
    st.session_state.user = None
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

# Custom CSS cho toàn bộ app
st.markdown("""
<style>
    /* Nút Google Login */
    .google-btn {
        display: block;
        text-align: center;
        padding: 12px 24px;
        background: linear-gradient(135deg, #4285F4 0%, #3367D6 100%);
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 16px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(66, 133, 244, 0.35);
        cursor: pointer;
    }
    .google-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(66, 133, 244, 0.45);
        background: linear-gradient(135deg, #357AE8 0%, #2F5ACE 100%);
    }
    
    /* Container cho ghi chú */
    .note-container {
        border-left: 4px solid #4285F4;
        padding: 16px;
        border-radius: 8px;
        background: linear-gradient(90deg, rgba(66, 133, 244, 0.08) 0%, rgba(255, 255, 255, 0) 100%);
        transition: all 0.3s ease;
    }
    .note-container:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
</style>
""", unsafe_allow_html=True)

def logout():
    st.session_state.user = None
    st.query_params.clear()
    st.rerun()

def handle_google_callback():
    # Streamlit phiên bản mới dùng st.query_params như một dictionary
    if "id_token" in st.query_params and not st.session_state.user:
        try:
            id_token = st.query_params["id_token"]
            user = google_login(id_token)
            st.session_state.user = user
            st.query_params.clear()
            st.rerun()
        except Exception as e:
            st.error(f"Đăng nhập Google thất bại: {e}")

# --- GIAO DIỆN ĐĂNG NHẬP / ĐĂNG KÝ ---
def auth_section():
    st.title("📝 Ứng Dụng Ghi Chú")
    st.write("Vui lòng đăng nhập để tiếp tục")
    
    if st.session_state.show_signup:
        st.subheader("Tạo tài khoản mới")
        with st.form("signup_form"):
            email = st.text_input("Email")
            pwd = st.text_input("Mật khẩu", type="password")
            if st.form_submit_button("Đăng ký"):
                try:
                    signup(email, pwd)
                    st.success("Đăng ký thành công! Mời bạn đăng nhập.")
                    st.session_state.show_signup = False
                    st.rerun()
                except Exception as e: 
                    st.error(f"Lỗi: {e}")
        if st.button("Đã có tài khoản? Đăng nhập"):
            st.session_state.show_signup = False
            st.rerun()
    else:
        st.subheader("Đăng nhập hệ thống")
        with st.form("login_form"):
            email = st.text_input("Email")
            pwd = st.text_input("Mật khẩu", type="password")
            if st.form_submit_button("Đăng nhập"):
                try:
                    user = login(email, pwd)
                    st.session_state.user = user
                    st.rerun()
                except Exception as e: 
                    st.error("Sai email hoặc mật khẩu!")
        
        st.write("---")
        
        # Nút đăng nhập Google - Cải thiện UI
        google_url = st.secrets["google-login"]["google-url"]
        st.markdown(
            f'''<a href="{google_url}" target="_self" class="google-btn">
                🌐 Đăng nhập bằng Google
            </a>''', 
            unsafe_allow_html=True
        )
        
        st.write("")
        if st.button("Chưa có tài khoản? Đăng ký ngay"):
            st.session_state.show_signup = True
            st.rerun()

# --- GIAO DIỆN QUẢN LÝ GHI CHÚ ---
def notes_section():
    # Header hiển thị user và nút đăng xuất
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("📝 Ghi chú của tôi")
        st.write(f"Xin chào, **{st.session_state.user['email']}**")
    with col2:
        if st.button("🚪 Đăng xuất"): 
            logout()

    st.divider()

    # Form thêm ghi chú mới
    with st.expander("➕ THÊM GHI CHÚ MỚI", expanded=True):
        title = st.text_input("Tiêu đề")
        content = st.text_area("Nội dung ghi chú", height=150)
        if st.button("💾 Lưu ghi chú", type="primary"):
            if title and content:
                try:
                    create_note(st.session_state.user["idToken"], title, content)
                    st.success("Đã lưu ghi chú thành công!")
                    st.rerun()
                except Exception as e: 
                    st.error(f"Lỗi khi lưu: {e}")
            else:
                st.warning("Vui lòng nhập đầy đủ tiêu đề và nội dung.")

    # Danh sách ghi chú đã lưu
    st.subheader("🗂️ Danh sách đã lưu")
    try:
        notes = get_notes(st.session_state.user["idToken"])
        if not notes:
            st.info("Bạn chưa có ghi chú nào. Hãy tạo một cái mới ở trên nhé!")
        else:
            for note in notes:
                st.markdown(
                    f'''<div class="note-container">
                        <h4>{note['title']}</h4>
                        <p style="font-size: 12px; color: #666; margin: 8px 0;">
                            📅 {str(note['created_at'])[:16].replace("T", " ")}
                        </p>
                        <p>{note['content']}</p>
                    </div>''',
                    unsafe_allow_html=True
                )
    except Exception as e:
        st.error("Phiên đăng nhập đã hết hạn hoặc có lỗi kết nối. Vui lòng đăng xuất và đăng nhập lại.")

# --- LUỒNG CHẠY CHÍNH ---
handle_google_callback()

if not st.session_state.user:
    auth_section()
else:
    notes_section()