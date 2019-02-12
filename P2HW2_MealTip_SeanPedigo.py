# This project was created to calculate the tip for a restaurant. I also added the option to include sales tax.
# 2/7/2018
# CTI-110 P2HW2 - Meal Tip Calculator
# Sean Pedigo
# Step 1.) I will declare my variables. I need to figured out how to declare a variable from user input.
# Step 2.) I will ask the user to input their meal total.
# Step 3.) Then I need to understand what the calculations are that need to be run.
# What is the math behind determining the tip?
# Step 4.) Run the calculations and print the total. This would be user input + all of the tips.
#
# (Optional steps)
# Step 5.) I will include the option to calculate what the total should be including taxes.
# Step 6.) Run a loop which asks a yes or no question. This will allow the user to say they do not want to include tax.
# Step 7.) If the answer is no, the user will be thanked for using the app and the process will finish.
# Step 8.) If the answer is yes it will ask what the sales tax is in their local area. Then it will determine how much
# the total cost is including sales tax. The user will be thanked and the process will finish.

meal = float(input('What was the total cost of your meal? ').strip('$'))
tip15 = meal + meal * .15
tip18 = meal + meal * .18
tip20 = meal + meal * .20

print('\n', 'The total cost of your meal with a 15% tip is $', format(tip15, '.2f'), "\n" +
      'The total cost of your meal with a 18% tip is $', format(tip18, '.2f'), "\n" +
      'The total cost of your meal with a 20% tip is $', format(tip20, '.2f'), "\n", sep='')

# This is optional code. This app will run fine without it. All it does is give the option of adding tax with a 'while'
# loop.

while True:
    answer = input("Would you like to include sales taxes? ").strip().lower()
    if answer == 'yes':
        print('\n')
        tax = str(input("What is the percentage of sales tax in your area? ")).strip('%')
        if tax.isdigit():
            tax = float(tax) / 100


# Below is a set variables I used to determine tax and tip. This could have been accomplished easier if I reassigned
# variables. I didn't want to do that, so I created a new set of variables here. This is a great example of how
# reassigning variables can make it easier to program, but if I wanted to call that variable later then I will be
# calling the new variable values instead.

# Commented below is an example of another code which would have made this easier.

# Meal = meal + meal * tax
# Total = meal + meal * tip

            Tax15 = tip15 * tax
            Tax18 = tip18 * tax
            Tax20 = tip20 * tax
            Total15 = Tax15 + tip15
            Total18 = Tax18 + tip18
            Total20 = Tax20 + tip20

            print('\n', 'The total cost of your meal with a 15% tip and tax is $', format(Total15, '.2f'), '\n' +
                  'The total cost of your meal with a 18% tip and tax is $', format(Total18, '.2f'), '\n' +
                  'The total cost of your meal with a 20% tip and tax is $', format(Total20, '.2f'), '\n', '\n' +
                  'Thank you for using my app. I hope you found it helpful.', sep='')

            break
    if answer == 'no':
        print('\n', 'Okay, thank you for using my app. I hope you found it helpful.')
        break
