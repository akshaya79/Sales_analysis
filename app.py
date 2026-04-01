import pandas as pd
import streamlit as st


# PAGE CONFIG
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Superstore Sales Dashboard")


# LOAD DATA
df = pd.read_csv("train.csv")

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Create Month column
df['Month'] = df['Order Date'].dt.month


# SIDEBAR FILTERS
st.sidebar.header("Filter Data")

region = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

# Apply filters
filtered_df = df[(df['Region'].isin(region)) & (df['Category'].isin(category))]

# KPIs
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", round(filtered_df['Sales'].sum(), 2))
col2.metric("Total Orders", filtered_df.shape[0])
col3.metric("Total Customers", filtered_df['Customer ID'].nunique())

# CHARTS
# Sales by Category
st.subheader("📊 Sales by Category")
category_sales = filtered_df.groupby('Category')['Sales'].sum()
st.bar_chart(category_sales)

# Sales by Region
st.subheader("🌍 Sales by Region")
region_sales = filtered_df.groupby('Region')['Sales'].sum()
st.bar_chart(region_sales)

# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")
monthly_sales = filtered_df.groupby('Month')['Sales'].sum()
st.line_chart(monthly_sales)

# Top 10 Products
st.subheader("🏆 Top 10 Products")
top_products = filtered_df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)


# DATA VIEW
st.subheader("📄 View Data")
st.dataframe(filtered_df)