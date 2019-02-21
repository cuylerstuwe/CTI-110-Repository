# Sales Prediction program
 # Date: 2/5/2019
 # CTI-110 P2T1 - Sales Prediction
 # Sean Pedigo
# Get the Projected Total Sales
total_sales = float(input ('Enter the projected sales: '))

# Calulate the profit as 23 percent of the total sales.
profit = total_sales * 0.23

# Display the profit
# print("The profit is $", format(profit,  '.2f '))
print("The profit is $", format(profit, ',.2f'), sep="" )
