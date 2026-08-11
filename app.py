import streamlit as st

# ============================================
# TO-DO LIST APPLICATION
# Author: Tehmina Anwar
# ============================================

st.set_page_config(
    page_title="To-Do List Application",
    page_icon="📝",
    layout="wide"
)

# ---------- Session State ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = []


# ---------- Helper ----------
def display_task(task, index):
    st.write(f"### {index}. {task['task']}")
    st.write(f"**Priority:** {task['priority']}")
    st.write(f"**Due Date:** {task['due_date']}")
    st.write(f"**Status:** {task['status']}")
    st.divider()


# ---------- Title ----------
st.title("📝 To-Do List Application")
st.write("Manage your daily tasks with priority, due dates and status tracking.")

# ---------- Sidebar ----------
st.sidebar.title("📋 Task Manager")

menu = st.sidebar.radio(
    "Choose an option:",
    [
        "➕ Add Task",
        "👀 View Tasks",
        "✏️ Update Task",
        "🗑️ Delete Task",
        "🔢 Count Tasks",
        "🔍 Search Task",
        "✅ Mark Completed",
        "📋 Completed Tasks",
        "🧹 Clear All Tasks",
        "⏳ Pending Tasks",
        "🔝 Sort by Priority",
        "📊 Statistics",
        "🔄 Mark Pending"
    ]
)


# ============================================
# 1. ADD TASK
# ============================================

if menu == "➕ Add Task":

    st.header("➕ Add New Task")

    task = st.text_input("Enter Task")

    priority = st.selectbox(
        "Select Priority",
        ["High", "Medium", "Low"]
    )

    due_date = st.date_input("Select Due Date")

    if st.button("✅ Add Task"):

        if task.strip() == "":
            st.error("Task cannot be empty!")

        else:

            st.session_state.tasks.append({
                "task": task.strip(),
                "priority": priority,
                "due_date": due_date.strftime("%d-%m-%Y"),
                "status": "Pending"
            })

            st.success("✅ Task Added Successfully!")


# ============================================
# 2. VIEW TASKS
# ============================================

elif menu == "👀 View Tasks":

    st.header("📋 Your Tasks")

    if not st.session_state.tasks:

        st.info("No tasks found.")

    else:

        for index, task in enumerate(
            st.session_state.tasks,
            start=1
        ):
            display_task(task, index)


# ============================================
# 3. UPDATE TASK
# ============================================

elif menu == "✏️ Update Task":

    st.header("✏️ Update Task")

    tasks = st.session_state.tasks

    if not tasks:

        st.info("No tasks available.")

    else:

        options = [
            f"{i + 1}. {task['task']}"
            for i, task in enumerate(tasks)
        ]

        selected = st.selectbox(
            "Select Task",
            options
        )

        index = options.index(selected)

        new_task = st.text_input(
            "New Task",
            value=tasks[index]["task"]
        )

        new_priority = st.selectbox(
            "New Priority",
            ["High", "Medium", "Low"],
            index=["High", "Medium", "Low"].index(
                tasks[index]["priority"]
            )
        )

        new_due_date = st.text_input(
            "New Due Date",
            value=tasks[index]["due_date"]
        )

        if st.button("💾 Update Task"):

            tasks[index]["task"] = new_task
            tasks[index]["priority"] = new_priority
            tasks[index]["due_date"] = new_due_date

            st.success("✅ Task Updated Successfully!")


# ============================================
# 4. DELETE TASK
# ============================================

elif menu == "🗑️ Delete Task":

    st.header("🗑️ Delete Task")

    tasks = st.session_state.tasks

    if not tasks:

        st.info("No tasks available.")

    else:

        options = [
            f"{i + 1}. {task['task']}"
            for i, task in enumerate(tasks)
        ]

        selected = st.selectbox(
            "Select Task",
            options
        )

        index = options.index(selected)

        if st.button("🗑️ Delete Task"):

            deleted = tasks.pop(index)

            st.success(
                f"✅ '{deleted['task']}' deleted successfully!"
            )


# ============================================
# 5. COUNT TASKS
# ============================================

elif menu == "🔢 Count Tasks":

    st.header("🔢 Task Count")

    total = len(st.session_state.tasks)

    st.metric(
        "📋 Total Tasks",
        total
    )


# ============================================
# 6. SEARCH TASK
# ============================================

elif menu == "🔍 Search Task":

    st.header("🔍 Search Task")

    keyword = st.text_input(
        "Enter keyword to search"
    )

    if keyword:

        found = False

        for index, task in enumerate(
            st.session_state.tasks,
            start=1
        ):

            if keyword.lower() in task["task"].lower():

                display_task(task, index)

                found = True

        if not found:

            st.warning("❌ Task not found.")


# ============================================
# 7. MARK COMPLETED
# ============================================

elif menu == "✅ Mark Completed":

    st.header("✅ Mark Task as Completed")

    tasks = st.session_state.tasks

    if not tasks:

        st.info("No tasks available.")

    else:

        options = [
            f"{i + 1}. {task['task']} ({task['status']})"
            for i, task in enumerate(tasks)
        ]

        selected = st.selectbox(
            "Select Task",
            options
        )

        index = options.index(selected)

        if st.button("✅ Mark Completed"):

            tasks[index]["status"] = "Completed"

            st.success(
                "✅ Task marked as Completed!"
            )


# ============================================
# 8. VIEW COMPLETED TASKS
# ============================================

elif menu == "📋 Completed Tasks":

    st.header("📋 Completed Tasks")

    found = False

    for index, task in enumerate(
        st.session_state.tasks,
        start=1
    ):

        if task["status"] == "Completed":

            display_task(task, index)

            found = True

    if not found:

        st.info("No completed tasks.")


# ============================================
# 9. CLEAR ALL TASKS
# ============================================

elif menu == "🧹 Clear All Tasks":

    st.header("🧹 Clear All Tasks")

    if not st.session_state.tasks:

        st.info("No tasks available.")

    else:

        st.warning(
            "⚠️ This will delete all tasks."
        )

        if st.button("🗑️ Clear All Tasks"):

            st.session_state.tasks.clear()

            st.success(
                "✅ All tasks deleted successfully!"
            )

            st.rerun()


# ============================================
# 10. VIEW PENDING TASKS
# ============================================

elif menu == "⏳ Pending Tasks":

    st.header("⏳ Pending Tasks")

    found = False

    for index, task in enumerate(
        st.session_state.tasks,
        start=1
    ):

        if task["status"] == "Pending":

            display_task(task, index)

            found = True

    if not found:

        st.success("🎉 No pending tasks!")


# ============================================
# 11. SORT BY PRIORITY
# ============================================

elif menu == "🔝 Sort by Priority":

    st.header("🔝 Tasks Sorted by Priority")

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    sorted_tasks = sorted(
        st.session_state.tasks,
        key=lambda x: priority_order.get(
            x["priority"],
            4
        )
    )

    if not sorted_tasks:

        st.info("No tasks available.")

    else:

        for index, task in enumerate(
            sorted_tasks,
            start=1
        ):
            display_task(task, index)


# ============================================
# 12. STATISTICS
# ============================================

elif menu == "📊 Statistics":

    st.header("📊 Task Statistics")

    total = len(st.session_state.tasks)

    completed = sum(
        1
        for task in st.session_state.tasks
        if task["status"] == "Completed"
    )

    pending = sum(
        1
        for task in st.session_state.tasks
        if task["status"] == "Pending"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📋 Total", total)

    with col2:
        st.metric("✅ Completed", completed)

    with col3:
        st.metric("⏳ Pending", pending)


# ============================================
# 13. MARK PENDING
# ============================================

elif menu == "🔄 Mark Pending":

    st.header("🔄 Mark Task as Pending")

    tasks = st.session_state.tasks

    if not tasks:

        st.info("No tasks available.")

    else:

        options = [
            f"{i + 1}. {task['task']} ({task['status']})"
            for i, task in enumerate(tasks)
        ]

        selected = st.selectbox(
            "Select Task",
            options
        )

        index = options.index(selected)

        if st.button("🔄 Mark Pending"):

            tasks[index]["status"] = "Pending"

            st.success(
                "✅ Task marked as Pending!"
            )


# ============================================
# FOOTER
# ============================================

st.sidebar.divider()

st.sidebar.caption(
    "© 2026 Tehmina Anwar | To-Do List Application"
)
```
