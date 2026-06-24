import pandas as pd
import sqlite3

# ============================================================
# WEEK 3 SQL DATA ANALYSIS PROJECT
# ============================================================

# Load Dataset
df = pd.read_excel("Cleaned_Dataset(3).xlsx")

# Create Database
conn = sqlite3.connect("week3.db")

# Create SQL Table
df.to_sql("sales", conn, if_exists="replace", index=False)

cursor = conn.cursor()

print("=" * 70)
print("WEEK 3 SQL DATA ANALYSIS")
print("=" * 70)

# ============================================================
# TOTAL ORDERS
# ============================================================

print("\nTOTAL ORDERS")
print("-" * 70)

total_orders = cursor.execute(
    "SELECT COUNT(*) FROM sales"
).fetchone()[0]

print(total_orders)

# ============================================================
# TOTAL REVENUE
# ============================================================

print("\nTOTAL REVENUE")
print("-" * 70)

total_revenue = cursor.execute(
    "SELECT SUM(TotalPrice) FROM sales"
).fetchone()[0]

print(round(total_revenue, 2))

# ============================================================
# AVERAGE ORDER VALUE
# ============================================================

print("\nAVERAGE ORDER VALUE")
print("-" * 70)

average_order_value = cursor.execute(
    "SELECT AVG(TotalPrice) FROM sales"
).fetchone()[0]

print(round(average_order_value, 2))

# ============================================================
# PRODUCT ANALYSIS
# ============================================================

print("\nPRODUCT ANALYSIS")
print("-" * 70)

for row in cursor.execute("""
SELECT Product, COUNT(*) AS TotalOrders
FROM sales
GROUP BY Product
ORDER BY TotalOrders DESC
"""):
    print(row)

# ============================================================
# PAYMENT METHOD ANALYSIS
# ============================================================

print("\nPAYMENT METHOD ANALYSIS")
print("-" * 70)

for row in cursor.execute("""
SELECT PaymentMethod, COUNT(*) AS TotalOrders
FROM sales
GROUP BY PaymentMethod
ORDER BY TotalOrders DESC
"""):
    print(row)

# ============================================================
# ORDER STATUS ANALYSIS
# ============================================================

print("\nORDER STATUS ANALYSIS")
print("-" * 70)

for row in cursor.execute("""
SELECT OrderStatus, COUNT(*) AS TotalOrders
FROM sales
GROUP BY OrderStatus
ORDER BY TotalOrders DESC
"""):
    print(row)

# ============================================================
# KEY INSIGHTS
# ============================================================

most_sold_product = cursor.execute("""
SELECT Product
FROM sales
GROUP BY Product
ORDER BY COUNT(*) DESC
LIMIT 1
""").fetchone()[0]

most_used_payment = cursor.execute("""
SELECT PaymentMethod
FROM sales
GROUP BY PaymentMethod
ORDER BY COUNT(*) DESC
LIMIT 1
""").fetchone()[0]

most_common_status = cursor.execute("""
SELECT OrderStatus
FROM sales
GROUP BY OrderStatus
ORDER BY COUNT(*) DESC
LIMIT 1
""").fetchone()[0]

print("\nKEY INSIGHTS")
print("-" * 70)

print(f"1. Total Orders Processed: {total_orders}")
print(f"2. Total Revenue Generated: {round(total_revenue, 2)}")
print(f"3. Average Order Value: {round(average_order_value, 2)}")
print(f"4. Most Sold Product: {most_sold_product}")
print(f"5. Most Preferred Payment Method: {most_used_payment}")
print(f"6. Most Common Order Status: {most_common_status}")

# Close Connection
conn.close()

print("\nSQL PROJECT COMPLETED SUCCESSFULLY")
print("=" * 70)