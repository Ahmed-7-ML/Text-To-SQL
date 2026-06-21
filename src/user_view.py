import streamlit as st
import pandas as pd
from src.db_manager import get_records

def render_user_dashboard():
    """Renders the safe, query-only workspace interface for Standard users."""
    st.success("ℹ️ **Standard User Mode Active:** Your workspace is strictly limited to natural language querying (Read-Only).")

    # Fixed Sample Preview for User Comfort
    st.subheader("🔍 Database Schema & Sample Rows Overview")
    preview_col1, preview_col2 = st.columns(2)

    with preview_col1:
        st.markdown("##### 👤 Students Table (Sample View)")
        try:
            raw_students = get_records("SELECT * FROM Students LIMIT 3;")
            df_students = pd.DataFrame(raw_students, columns=["Id", "Name", "DoB", "Section"])
            st.dataframe(df_students, use_container_width=True, hide_index=True)
        except Exception:
            st.caption("⚠️ Sample rows currently unavailable.")

    with preview_col2:
        st.markdown("##### 📊 Marks Table (Sample View)")
        try:
            raw_marks = get_records("SELECT * FROM Marks LIMIT 3;")
            df_marks = pd.DataFrame(raw_marks, columns=["MarkId", "StudentId", "Subject", "Score"])
            st.dataframe(df_marks, use_container_width=True, hide_index=True)
        except Exception:
            st.caption("⚠️ Sample rows currently unavailable.")

    st.markdown("---")
    