import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Create Month column
df['Month'] = df['Order Date'].dt.month


# BASIC ANALYSIS


# Total Sales
print("Total Sales:", df['Sales'].sum())

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:\n", category_sales)

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:\n", region_sales)

# Monthly Sales
monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales:\n", monthly_sales)

# Top 10 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products:\n", top_products)


# VISUALIZATIONS


# Category Sales Bar Chart
category_sales.plot(kind='bar', title='Sales by Category')
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Region Sales Pie Chart
region_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Region')
plt.ylabel("")
plt.show()

# Monthly Sales Line Chart
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Top Products Bar Chart
top_products.plot(kind='barh', title='Top 10 Products')
plt.xlabel("Sales")
plt.ylabel("Product")
plt.show()