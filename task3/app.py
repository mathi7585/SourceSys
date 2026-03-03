import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Dropout Analysis", layout="wide")

st.title("📊 Student Dropout Analysis App")

# File uploader (CSV only)
uploaded_file = st.file_uploader("Upload Student Dataset (CSV Only)", type=["csv"])

if uploaded_file is not None:
    # Read dataset
    df = pd.read_csv(uploaded_file)

    st.success("Dataset Uploaded Successfully!")

    # Show dataset preview
    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    # Show dataset info
    st.subheader("📊 Basic Statistics")
    st.write(df.describe())

    # Check if Dropout column exists
    if "Dropout" in df.columns:

        # Total students
        total_students = len(df)

        # Dropout count
        dropout_count = df["Dropout"].sum()

        # Dropout percentage
        dropout_percentage = (dropout_count / total_students) * 100

        st.subheader("📈 Dropout Overview")
        col1, col2, col3 = st.columns(3)

        col1.metric("Total Students", total_students)
        col2.metric("Dropouts", dropout_count)
        col3.metric("Dropout %", f"{dropout_percentage:.2f}%")

        # -------------------------
        # Dropout Distribution Plot
        # -------------------------
        st.subheader("📊 Dropout Distribution")

        dropout_distribution = df["Dropout"].value_counts()

        fig1, ax1 = plt.subplots()
        ax1.bar(dropout_distribution.index.astype(str), dropout_distribution.values)
        ax1.set_xlabel("Dropout (0 = No, 1 = Yes)")
        ax1.set_ylabel("Count")
        ax1.set_title("Dropout Count Distribution")

        st.pyplot(fig1)

        # -------------------------
        # Dropout by Gender (Optional)
        # -------------------------
        if "Gender" in df.columns:
            st.subheader("👥 Dropout by Gender")

            gender_dropout = df.groupby("Gender")["Dropout"].sum()

            fig2, ax2 = plt.subplots()
            ax2.bar(gender_dropout.index.astype(str), gender_dropout.values)
            ax2.set_xlabel("Gender")
            ax2.set_ylabel("Number of Dropouts")
            ax2.set_title("Dropouts by Gender")

            st.pyplot(fig2)

        # -------------------------
        # Dropout by Course (Optional)
        # -------------------------
        if "Course" in df.columns:
            st.subheader("🎓 Dropout by Course")

            course_dropout = df.groupby("Course")["Dropout"].sum()

            fig3, ax3 = plt.subplots()
            ax3.bar(course_dropout.index.astype(str), course_dropout.values)
            ax3.set_xlabel("Course")
            ax3.set_ylabel("Number of Dropouts")
            ax3.set_title("Dropouts by Course")

            plt.xticks(rotation=45)
            st.pyplot(fig3)

    else:
        st.error("❌ 'Dropout' column not found in dataset!")

else:
    st.info("Please upload a CSV file to begin analysis.")