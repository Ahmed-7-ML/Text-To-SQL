import streamlit as st
import pandas as pd
from src.db_manager import get_records

def render_admin_dashboard():
    """Renders the comprehensive full-access dashboard for Admin users."""
    st.info("⚡ **Admin Mode Active:** You have full Read/Write/Delete/Update privileges over the entire database.")

    # 📊 Feature: Dynamic Data Preview with Row Limit Selector
    st.subheader("🔍 Database Live Schema & Dynamic Preview")
    row_limit = st.slider("Select maximum rows to preview:", min_value=1, max_value=50, value=5)
    
    preview_col1, preview_col2 = st.columns(2)
    
    with preview_col1:
        st.markdown("##### 👤 Students Table Preview")
        try:
            raw_students = get_records(f"SELECT * FROM Students LIMIT {row_limit};")
            df_students = pd.DataFrame(raw_students, columns=["Id", "Name", "DoB", "Section"])
            st.dataframe(df_students, use_container_width=True, hide_index=True)
        except Exception:
            st.caption("⚠️ Table unavailable. Ensure your database initialization script has run.")

    with preview_col2:
        st.markdown("##### 📊 Marks Table Preview")
        try:
            raw_marks = get_records(f"SELECT * FROM Marks LIMIT {row_limit};")
            df_marks = pd.DataFrame(raw_marks, columns=["MarkId", "StudentId", "Subject", "Score"])
            st.dataframe(df_marks, use_container_width=True, hide_index=True)
        except Exception:
            st.caption("⚠️ Table unavailable. Ensure your database initialization script has run.")

    st.markdown("---")

    # 🛠️ Admin Quick Actions Panel
    with st.expander("🛠️ Admin Quick Actions (Direct DB Modification)"):
        admin_tab1, admin_tab2, admin_tab3 = st.tabs(["➕ Insert Record", "🔄 Update Marks", "🗑️ Destructive Actions"])
        
        # 1. Insert Action
        with admin_tab1:
            st.markdown("##### Add New Student")
            new_name = st.text_input("Student Name", key="new_student_name")
            new_dob = st.text_input("Date of Birth (DD-MM-YYYY)", key="new_student_dob")
            new_section = st.number_input("Section Number", min_value=1, step=1, key="new_student_sec")
            if st.button("➕ Insert Student Record", type="secondary"):
                if new_name and new_dob:
                    try:
                        get_records(f"INSERT INTO Students (Name, DoB, Section) VALUES ('{new_name}', '{new_dob}', {new_section});")
                        st.success(f"Successfully added student: {new_name}")
                        st.rerun()
                    except Exception as ex:
                        st.error(f"Failed to insert: {ex}")
        
        # 2. Update Action (NEW FEATURE)
        with admin_tab2:
            st.markdown("##### Update Student Examination Marks")
            target_student_id = st.number_input("Target Student ID", min_value=1, step=1, key="update_sid")
            target_subject = st.text_input("Subject Title (e.g., Machine Learning)", key="update_sub")
            new_score = st.number_input("New Examination Score", min_value=0, max_value=100, step=1, key="update_score")
            
            if st.button("🔄 Update Score Record", type="secondary"):
                if target_subject:
                    try:
                        # Check if record exists first to decide INSERT or UPDATE safely
                        check_exist = get_records(f"SELECT 1 FROM Marks WHERE StudentId={target_student_id} AND Subject='{target_subject}';")
                        if check_exist:
                            get_records(f"UPDATE Marks SET Score={new_score} WHERE StudentId={target_student_id} AND Subject='{target_subject}';")
                        else:
                            get_records(f"INSERT INTO Marks (StudentId, Subject, Score) VALUES ({target_student_id}, '{target_subject}', {new_score});")
                        st.success(f"Successfully updated grade for Student ID {target_student_id} in {target_subject} to {new_score}%")
                        st.rerun()
                    except Exception as ex:
                        st.error(f"Failed to update score: {ex}")

        # 3. Delete Action
        with admin_tab3:
            st.markdown("##### Destructive Actions")
            delete_id = st.number_input("Target Student ID to Delete", min_value=1, step=1, key="del_sid")
            if st.button("🗑️ Force Hard Delete Record", type="primary"):
                try:
                    get_records(f"DELETE FROM Students WHERE Id = {delete_id};")
                    get_records(f"DELETE FROM Marks WHERE StudentId = {delete_id};")
                    st.warning(f"Cleared all records associated with Student ID: {delete_id}")
                    st.rerun()
                except Exception as ex:
                    st.error(f"Failed to delete: {ex}")
                    