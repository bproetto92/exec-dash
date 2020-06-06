# dashboard_generator.py

# Input File selected from User: Selections include - sales-201710.csv
file_name = input("Please input csv file name: ")

if file_name != "sales-201710.csv":
    if file_name != "sales-201803.csv":
     print("Sorry, no file exists")
     exit()


import os
import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71

csv_filename = file_name
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



plt.barh(row_name,monthly_sales, align='center')
plt.yticks(row_name, row_name, fontsize=8)
plt.ylabel('Products')
plt.xlabel('Sales (USD)')
plt.title('Monthly Sales by Product')


# print("-----------------------")
# print("MONTH: March 2018")

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
