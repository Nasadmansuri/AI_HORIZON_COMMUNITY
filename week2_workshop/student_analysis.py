import pandas as pd
import numpy as np
import streamlit as st

# -----------------------------------------------
# Page Setup
# -----------------------------------------------
st.set_page_config(page_title="Student Performance", page_icon="🎓")
st.title("🎓 Student Performance Analysis")
st.write("Upload your student CSV file to explore the data.")

# -----------------------------------------------
# File Upload
# -----------------------------------------------
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if not uploaded_file:
    st.info("👆 Please upload a CSV file to get started.")
    st.stop()

# -----------------------------------------------
# Load Data
# -----------------------------------------------
df = pd.read_csv(uploaded_file)
st.success(f"✅ File uploaded! {len(df)} students found.")

# Show raw data (collapsible so it's not overwhelming)
with st.expander("📋 View Raw Data"):
    st.dataframe(df, use_container_width=True)

st.divider()

# -----------------------------------------------
# Sidebar Filters
# -----------------------------------------------
st.sidebar.header("🔍 Filter Students")
st.sidebar.write("Use these filters to narrow down the data.")

filtered_df = df.copy()  # Always filter from original, not overwrite df

# Filter by Name
if "Name" in df.columns:
    selected_names = st.sidebar.multiselect(
        "Student Name", sorted(df["Name"].unique())
    )
    if selected_names:
        filtered_df = filtered_df[filtered_df["Name"].isin(selected_names)]

# Filter by City
if "City" in df.columns:
    selected_cities = st.sidebar.multiselect(
        "City", sorted(df["City"].unique())
    )
    if selected_cities:
        filtered_df = filtered_df[filtered_df["City"].isin(selected_cities)]

# Filter by Nationality / Country
nat_col = next(
    (c for c in df.columns if c.lower() in ("nationality", "country")), None
)
if nat_col:
    selected_nat = st.sidebar.multiselect(
        nat_col, sorted(df[nat_col].unique())
    )
    if selected_nat:
        filtered_df = filtered_df[filtered_df[nat_col].isin(selected_nat)]

# -----------------------------------------------
# Filtered Data Table
# -----------------------------------------------
st.subheader("📄 Filtered Data")
st.write(f"Showing **{len(filtered_df)}** of **{len(df)}** students")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

# Download filtered data
st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_students.csv",
    mime="text/csv"
)

st.divider()

# -----------------------------------------------
# Numeric columns (grade subjects only)
# -----------------------------------------------
exclude_cols = {"age"}
numeric_cols = [
    c for c in filtered_df.select_dtypes(include=np.number).columns
    if c.lower() not in exclude_cols
]

if not numeric_cols:
    st.warning("No grade columns found in the data.")
    st.stop()

# -----------------------------------------------
# Quick Summary Cards
# -----------------------------------------------
st.subheader("📊 Quick Summary")

filtered_df["Average"] = filtered_df[numeric_cols].mean(axis=1).round(1)

col1, col2, col3, col4 = st.columns(4)
col1.metric("👥 Total Students", len(filtered_df))
col2.metric("📈 Class Average",  f"{filtered_df['Average'].mean():.1f}")
col3.metric("🏆 Highest Score",  f"{filtered_df[numeric_cols].max().max():.0f}")
col4.metric("📉 Lowest Score",   f"{filtered_df[numeric_cols].min().min():.0f}")

st.divider()

# -----------------------------------------------
# Statistics Table
# -----------------------------------------------
st.subheader("📋 Statistics Summary")
st.write("Mean, Median, Min, and Max for each subject.")

stats_df = pd.DataFrame({
    "Mean":   filtered_df[numeric_cols].mean().round(2),
    "Median": filtered_df[numeric_cols].median().round(2),
    "Min":    filtered_df[numeric_cols].min(),
    "Max":    filtered_df[numeric_cols].max(),
})
st.dataframe(stats_df, use_container_width=True)

st.divider()

# -----------------------------------------------
# Visualizations
# -----------------------------------------------
st.subheader("📈 Grade Visualizations")

# Let user pick which subject to view
subject = st.selectbox("Select a subject to visualize:", numeric_cols)

# Bar chart — average score for selected subject
st.write(f"**Average {subject} score: {filtered_df[subject].mean():.1f}**")
st.bar_chart(filtered_df.set_index("Name")[subject] if "Name" in filtered_df.columns
             else filtered_df[subject])

st.write("---")

# All subjects average comparison
st.write("**Average Score per Subject (all subjects)**")
avg_per_subject = filtered_df[numeric_cols].mean().round(1)
st.bar_chart(avg_per_subject)


