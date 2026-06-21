# Verify login data and display the Login screen if the user is not registered.
import sqlite3
import streamlit as st

def login(username: str, password: str):
    """Verify user data directly from the database"""
    conn = sqlite3.connect("Faculty.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Role FROM Users WHERE Username = ? AND Password = ? 
        """, (username, password)
    )
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def render_login_page():
    """Design and manage the login screen"""
    st.markdown("<h2 style='text-align: center;'>🔐 Enterprise AI Database Portal</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            st.subheader("Login Credentials")
            user_input = st.text_input("Username")
            pass_input = st.text_input("Password", type='password')
            login_btn = st.form_submit_button("Sign In", width='stretch')
            
            if login_btn:
                user_role = login(user_input, pass_input)
                if user_role:
                    st.session_state.logged_in = True
                    st.session_state.username = user_input
                    st.session_state.role = user_role
                    st.success(f"Welcome back, {user_input}! Redirecting...")
                    st.rerun()
                else:
                    st.error("❌ Invalid Username or Password.")
