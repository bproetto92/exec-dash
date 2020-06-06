# dashboard_generator.py


import os
import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71

csv_filename = "sales-201710.csv"
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)
csv_data = pandas.read_csv(csv_filepath)


#Total Monthly Sales
monthly_total = csv_data["sales price"].sum()

#List of Top Selling Products

product_totals = csv_data.groupby(["product"]).sum()

product_totals = product_totals.sort_values("sales price", ascending=False)

top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1

#Bar Chart depicting information

row_name = []
monthly_sales = []
for x in top_sellers:
    row_name.append(x["name"])
    monthly_sales.append(x["monthly_sales"])

#monthly_sales = to_usd(monthly_sales)
print(row_name)
print(monthly_sales)

plt.bar(row_name, monthly_sales, align='center')
plt.xticks(row_name, row_name, fontsize=5)
plt.ylabel('Monthly Sales')
plt.title('Product')

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + to_usd(d["monthly_sales"]))

print("-----------------------")
print("VISUALIZING THE DATA...")

plt.show()