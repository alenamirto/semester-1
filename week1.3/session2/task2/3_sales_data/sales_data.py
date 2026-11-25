# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

x = "/workspaces/semester-1/week1.3/session2/task2/3_sales_data/sales.csv"
sales = []

with open (x,"r") as y:
    sales = y.read()


data = [line.split(",") for line in sales.strip().split("\n")]
data.remove(data[0])

# creating list of sale amounts
sale_amounts=[]
for line in data:
    sale_amounts.append(line[2])

# converting to list of ints
sale_amounts = [int(sale_amounts[i]) for i in range(0, len(sale_amounts))]

# finding largest sale day and widget sold the most
highest_sale_amount = sale_amounts[0]  
highest_sale_day = data[0][0]

for i in range(1, len(sale_amounts)):
    if sale_amounts[i] > highest_sale_amount:
        highest_sale_amount = sale_amounts[i]
    
for line in data:
    if line[2] == str(highest_sale_amount):
        highest_sale_day = line[0]
        most_sold_widget = line[1]

print(f"""\nhighest sale amount is {highest_sale_amount} on {highest_sale_day}
the most sold widget is {most_sold_widget}\n""")

# average sale amount
sale_sum = 0
for amount in sale_amounts:
    sale_sum += amount

mean = sale_sum/(len(sale_amounts))
print(f"mean sales is {mean}")

# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows