# Convert pounds to kilograms
# 2/6/2018
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Sean Pedigo
# Step 1.) Ask the user how many pounds need to be converted 
# Step 2.) The inputted answer should be typed in
# Step 3.) Print out the conversions of pounds inputted divided by 2.2046 to get
# the answer for how many kilos are in the specified number of pounds.

print('\n')
print ("This is a small program which converts pounds to kilograms." + '\n')
pounds = int (input("Please enter how many pounds you need to convert: "))
print ('\n',(pounds),('pounds is'), format(pounds / 2.2046,'.2f'), "kilograms")
