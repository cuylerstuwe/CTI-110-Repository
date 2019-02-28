# My goal is to make a script which matches primary colors, and tells you what the output is. In other words.
# If a user inputs red and blue the program will explain that purple is the answer.
# 1.) Create a welcome message.
# 2.) Create a function for input(userinput).
# 3.) Return the input from said function to another function(colormixed).
    # I will take the strings from input and declare them as variables
    # When colors have been declared determine what happens if colors are mixed.
        # Add the first color declared by the user, then add the second color defined by the user.
        # Final result will be the outcome of two mixed colors.
# 4.) Run while loop which asks if the user wants to restart the program or not.
# 5.) If user selects yes, rerun the program. Else the program ends.

def userinput():
    color1 = input("Choose your first color" + "\n").lower().strip( )
    color2 = input("What is the second color you would like to choose?" + "\n").lower().strip( )
    return color1, color2

def colormixed():
    color1, color2 = userinput()
    red = "red"
    blue = "blue"
    yellow = "yellow"
    if (color1 + color2 == red + blue) or (color1 + color2 == blue + red):
       print("\x1b[1;35;48m You like purple? Well you got purple. No take-backs, go paint your cadillac. "
             + "You're a pimp now \x1b[0m" +'\n')
    elif (color1 + color2 == red + yellow) or (color1 + color2 == yellow + red):
        print("\x1b[1;33;48m The color you will get is orange. Great, now everyone is going to notice you. "
              "Hope you like the attention. \x1b[0m" + '\n')
    elif (color1 + color2 == blue + yellow) or (color1 + color2 == yellow + blue):
        print("\x1b[1;92;48m The color you will get is green, like a leprechaun. " +
              "Hope you like lucky charms, bucko.\x1b[0m" + '\n')
    else:
        print("Well you're definitely no picasso. That color sucks. Try something else" + '\n')

print('\n'+
      "Hello, welcome to the Super Duper Color Mixer 9,001 I'm here to help you because you never graduated preschool."
      + '\n'
      + '\n'
      + "Choose two colors, I will mix them, tell you what the result is, and prevent you from the embarrassment "
      + "of asking a preschooler to help you with your homework.")
colormixed()

while True:
    answer = input("Would you like to run the program again? Yes or no." + "\n").lower().strip( )
    if answer == "yes":
        print('\n' + "Whoa, really? You still don't got it yet? Okay, lets go again."
        + '\n')
        colormixed()
        continue
    else:
        print('\n' + "Bye Felicia.")
        break