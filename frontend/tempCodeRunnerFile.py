import streamlit as st
import requests
from api_client import signup, login, google_login, get_notes, create_note

st.set_page_config(page_title="PonNotes", page_icon="📝", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

def logout():
    st.session_state.user = None
    st.query_params.clear()
    st.rerun()

def handle_google_callback():
    params = st.query_params
    if "id_token" in params and not st.session_state.user:
        try:
            user = google_login(params["id_token"])
            st.session_state.user = user
            st.query_params.clear()
            st.rerun()
        except Exception as e:
            st.error(f"Google login failed: {e}")

def auth_section():
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
                except Exception as e: st.error(f"Lỗi: {e}")
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
                except Exception as e: st.error(f"Sai thông tin: {e}")
        
        st.write("---")
        # Nút đăng nhập Google [cite: 60]
        google_url = st.secrets["google-login"]["google-url"]
        st.markdown(f'<a href="{google_url}" target="_self" style="text-decoration:none;"><div style="text-align:center; padding:10px; border:1px solid #ddd; border-radius:5px; color:white;">Login with Google</div></a>', unsafe_allow_html=True)
        
        if st.button("Chưa có tài khoản? Đăng ký ngay"):
            st.session_state.show_signup = True
            st.rerun()

def notes_section():
    # 1. Hiển thị thông tin người dùng [cite: 97]
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("📝 Ghi chú của tôi")
        st.write(f"Chào mừng, **{st.session_state.user['email']}**")
    with col2:
        if st.button("Đăng xuất"): logout()

    st.divider()

    # 2. Nhập liệu ghi chú mới (Feature chính) 
    with st.expander("➕ Thêm ghi chú mới", expanded=True):
        title = st.text_input("Tiêu đề")
        content = st.text_area("Nội dung ghi chú")
        if st.button("Lưu ghi chú"):
            if title and content:
                try:
                    res = create_note(st.session_state.user["idToken"], title, content)
                    st.success(f"Đã lưu! AI Summary: {res.get('summary', 'N/A')}") # Hiển thị kết quả từ BE [cite: 99]
                    st.rerun()
                except Exception as e: st.error(f"Lỗi lưu: {e}")
            else:
                st.warning("Vui lòng nhập đầy đủ tiêu đề và nội dung.")

    st.subheader("🗂️ Danh sách đã lưu")
    try:
        notes = get_notes(st.session_state.user["idToken"])
        if not notes:
            st.info("Bạn chưa có ghi chú nào.")
        else:
            for note in notes:
                with st.container(border=True):
                    st.markdown(f"### {note['title']}")
                    st.caption(f"📅 {note['created_at']}")
                    st.write(note['content'])
                    if note.get('summary'):
                        st.info(f"🤖 **AI Summary:** {note['summary']}")
    except Exception as e:
        st.error(f"Không thể tải danh sách: {e}")

handle_google_callback()

if not st.session_state.user:
    auth_section()
else:
    notes_section()