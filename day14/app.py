import streamlit as st
import requests

API_URL = "http://localhost:8000/auth/login"

# Initialize session state
if "token" not in st.session_state:
    st.session_state["token"] = None

if "email" not in st.session_state:
    st.session_state["email"] = None


# -------------------------
# DASHBOARD
# -------------------------
if st.session_state["token"]:

    st.title("Dashboard")

    st.success(f"Welcome, {st.session_state['email']}!")

    st.write("This is a placeholder dashboard.")

    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()

# -------------------------
# LOGIN PAGE
# -------------------------
else:

    st.title("Login")

    with st.form("login_form"):

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Login")

    if submitted:

        try:

            response = requests.post(
                API_URL,
                json={
                    "email": email,
                    "password": password
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state["token"] = data["token"]
                st.session_state["email"] = email

                st.success("Login successful!")

                st.rerun()

            else:

                error_message = response.json().get(
                    "detail",
                    "Login failed"
                )

                st.error(error_message)

        except requests.exceptions.ConnectionError:

            st.error("Backend server is offline")