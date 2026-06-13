import streamlit as st
import pandas as pd
from datetime import date

# ===================================
# PAGE CONFIG
# ===================================
st.set_page_config(
    page_title="Task Manager",
    page_icon="📋",
    layout="wide"
)
#css
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: black;
}

/* Text */
h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111111;
}

/* Input Fields */
input, textarea {
    background-color: #222222 !important;
    color: white !important;
}

/* Buttons */
.stButton button {
    background-color: #444444 !important;
    color: white !important;
}

/* Metrics */
[data-testid="metric-container"] {
    background-color: #222222;
    border-radius: 10px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# ===================================
# SESSION STATE
# ===================================
if "users" not in st.session_state:
    st.session_state.users = {}

if "tasks" not in st.session_state:
    st.session_state.tasks = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None


# ===================================
# REGISTER
# ===================================
def register():

    st.header("Register")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        if not username or not email or not password:
            st.error("Please fill all fields")

        elif username in st.session_state.users:
            st.error("Username already exists")

        else:
            st.session_state.users[username] = {
                "email": email,
                "password": password
            }

            st.session_state.tasks[username] = []

            st.success("Registration Successful!")
            st.info("Please Login")


# ===================================
# LOGIN
# ===================================
def login():

    st.header("Login")

    username = st.text_input(
        "Username",
        key="login_user"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_pass"
    )

    if st.button("Login"):

        if (
            username in st.session_state.users
            and
            st.session_state.users[username]["password"] == password
        ):

            st.session_state.logged_in = True
            st.session_state.current_user = username

            st.rerun()

        else:
            st.error("Invalid Username or Password")


# ===================================
# DASHBOARD
# ===================================
def dashboard():

    user = st.session_state.current_user

    st.title("📋 Task Manager Dashboard")

    st.success(f"Welcome {user}")

    # Metrics
    tasks = st.session_state.tasks[user]

    total_tasks = len(tasks)

    completed_tasks = sum(
        1 for task in tasks
        if task["completed"]
    )

    pending_tasks = total_tasks - completed_tasks

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Tasks", total_tasks)

    with col2:
        st.metric("Completed", completed_tasks)

    with col3:
        st.metric("Pending", pending_tasks)

    st.divider()

    # Create Task
    st.subheader("Create Task")

    with st.form("task_form"):

        title = st.text_input("Title")

        description = st.text_area(
            "Description"
        )

        priority = st.selectbox(
            "Priority",
            ["Low", "Medium", "High"]
        )

        due_date = st.date_input(
            "Due Date",
            min_value=date.today()
        )

        submit_task = st.form_submit_button(
            "Create Task"
        )

    if submit_task:

        if title:

            task_id = len(
                st.session_state.tasks[user]
            ) + 1

            st.session_state.tasks[user].append(
                {
                    "id": task_id,
                    "title": title,
                    "description": description,
                    "priority": priority,
                    "due_date": str(due_date),
                    "completed": False
                }
            )

            st.success(
                f"Task '{title}' created successfully!"
            )

            st.rerun()

        else:
            st.error("Task Title is required")

    st.divider()

    # My Tasks
    st.subheader("My Tasks")

    tasks = st.session_state.tasks[user]

    if tasks:

        df = pd.DataFrame(
            [
                {
                    "ID": task["id"],
                    "Title": task["title"],
                    "Description": task["description"],
                    "Priority": task["priority"],
                    "Due Date": task["due_date"],
                    "Completed":
                        "Yes" if task["completed"]
                        else "No"
                }
                for task in tasks
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "Update Task Status"
        )

        for index, task in enumerate(tasks):

            col1, col2, col3 = st.columns(
                [4, 2, 1]
            )

            with col1:
                st.write(
                    f"**{task['title']}**"
                )

            with col2:

                if task["completed"]:
                    st.success("Completed")

                else:
                    if st.button(
                        "Complete",
                        key=f"complete_{index}"
                    ):
                        task["completed"] = True
                        st.rerun()

            with col3:

                if st.button(
                    "Delete",
                    key=f"delete_{index}"
                ):
                    st.session_state.tasks[user].pop(
                        index
                    )
                    st.rerun()

    else:
        st.info("No Tasks Available")

    st.divider()

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.current_user = None

        st.rerun()


# ===================================
# MAIN APP
# ===================================
if st.session_state.logged_in:

    dashboard()

else:

    st.title("📋 Task Manager")

    option = st.sidebar.selectbox(
        "Menu",
        [
            "Login",
            "Register"
        ]
    )

    if option == "Login":
        login()
    else:
        register()