# Descriptive-statistics-house-expensive-project
# 📊 Descriptive Statistics Dashboard — Streamlit Project

### 🔍 Project Overview
This project is an interactive **Descriptive Statistics Dashboard** built using **Streamlit**, designed to analyze the dataset `Inc_Exp_Data.csv`.  
It enables users to explore **central tendency, distribution patterns, and visual insights** of numerical variables in a dynamic and user-friendly way.

---

## 🚀 Features
| Feature | Description |
|--------|-------------|
| 📂 Auto dataset loading | Reads `Inc_Exp_Data.csv` automatically from local path |
| 📌 Dataset overview | Displays total rows, total columns & missing value count |
| 📊 Summary statistics | Mean, Median, Mode, Skewness & Kurtosis |
| 📈 Interactive visualizations | Histogram, Boxplot & Scatterplot |
| 🤖 Automatic insights | Detects skewness & kurtosis and explains distribution behavior |

---

## 🖥️ Tech Stack
| Library | Role |
|--------|------|
| Streamlit | Dashboard UI |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Seaborn | Visualizations |
| Matplotlib | Plot rendering |

---

## 📌 Workflow
1. Load dataset automatically
2. Display dataset preview and metadata
3. Choose a numerical variable from sidebar
4. View statistical summary
5. Select plots (Histogram, Boxplot, Scatterplot)
6. Read distribution-based insights generated automatically

---

## 🔑 Key Insights
The dashboard provides:
- Clear understanding of **data distribution**
- Identification of **outliers** using boxplots
- **Correlation patterns** using scatterplots
- Whether a variable is:
  - **Positively or negatively skewed**
  - **Leptokurtic / Platykurtic / Mesokurtic**

This helps users quickly interpret **data behavior without manual calculations**.

---

## 🏁 Conclusion
This project simplifies exploratory data analysis by combining **statistical summaries + visualization + automated insights** in a single tool.  
It is useful for:
- Students learning statistics
- Data science beginners
- EDA for analytics / ML projects
- Academic report & presentation preparation

---

## 📌 How to Run the App
```bash
pip install -r requirements.txt
streamlit run app.py
