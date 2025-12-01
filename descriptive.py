import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="📊 Descriptive Statistics Dashboard", layout="wide")

# Title
st.markdown("<h1 style='text-align:center;'>📌 Descriptive Statistics Project Dashboard</h1>", unsafe_allow_html=True)

# Load Dataset from local path
file_path = 'Inc_Exp_Data.csv'

try:
    df = pd.read_csv(file_path)
    st.success("📂 Dataset Loaded Successfully Loaded automatically")
except:
    st.error("❌ Error loading the dataset — Check the file path")
    st.stop()

# Dataset Overview
st.subheader("📌 Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isna().sum().sum())

st.dataframe(df.head())

# Select numeric column
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

st.sidebar.header("📌 Summary Statistics")
selected_num = st.sidebar.selectbox("Choose a Numerical Column", numeric_cols)

# Statistics
if selected_num:
    desc = df[selected_num].describe()
    st.subheader(f"📍 Statistical Summary for `{selected_num}`")
    st.write(desc)

    mean = df[selected_num].mean()
    median = df[selected_num].median()
    mode = df[selected_num].mode()[0]
    skew = df[selected_num].skew()
    kurt = df[selected_num].kurt()

    st.write(f"""
    📌 **Mean**: {mean:.2f}  
    📌 **Median**: {median:.2f}  
    📌 **Mode**: {mode:.2f}  
    📌 **Skewness**: {skew:.3f}  
    📌 **Kurtosis**: {kurt:.3f}
    """)

# Visualization Options
st.sidebar.header("📌 Select Graphs")
plot_type = st.sidebar.multiselect(
    "Choose Visualizations",
    ["Histogram", "Boxplot", "Scatterplot"]
)

st.subheader("📊 Visualizations")

if "Histogram" in plot_type:
    fig, ax = plt.subplots()
    sns.histplot(df[selected_num], kde=True, bins=25, ax=ax)
    ax.set_title(f"Histogram of {selected_num}")
    st.pyplot(fig)

if "Boxplot" in plot_type:
    fig, ax = plt.subplots()
    sns.boxplot(x=df[selected_num], ax=ax)
    ax.set_title(f"Boxplot of {selected_num}")
    st.pyplot(fig)

if "Scatterplot" in plot_type:
    other_col = st.selectbox("Select another Numeric column for Scatterplot", numeric_cols)
    if other_col:
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[selected_num], y=df[other_col], ax=ax)
        ax.set_title(f"{selected_num} vs {other_col}")
        st.pyplot(fig)

# Automatic Insights
st.subheader("🔍 Insights")
if skew > 0:
    st.write(f"➡ `{selected_num}` is **positively skewed** (right-tailed distribution).")
elif skew < 0:
    st.write(f"➡ `{selected_num}` is **negatively skewed** (left-tailed distribution).")
else:
    st.write(f"➡ `{selected_num}` is **perfectly symmetrical**.")

if kurt > 3:
    st.write("🔺 Distribution is **leptokurtic (sharp peak, heavy tails)**.")
elif kurt < 3:
    st.write("🔻 Distribution is **platykurtic (flat distribution)**.")
else:
    st.write("➖ Distribution is **mesokurtic (normal-like)**.")

st.markdown("<hr><center>🚀 Dashboard Completed — Ready for Report & Presentation</center>", unsafe_allow_html=True)

