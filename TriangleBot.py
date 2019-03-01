import time

# Get number input from user, given a prompt.
# prompt: What to prompt the user.
# returns: The user's numerical response, cast to an integer.
def get_numerical_input(prompt):
  input_as_number = None
  while input_as_number is None:
    user_input = input(prompt)
    try:
      input_as_number = int(user_input)
    except:
      print("", end="")
  return input_as_number

# Prompt the user to confirm a yes/no option, return whether "yes".
# prompt: What to prompt the user.
# returns: Whether the user said "yes", or not.
def did_user_say_yes(prompt):
  user_input = input(prompt + (" (y/n)\n"))
  user_input_lower = user_input.lower()
  return (user_input_lower[0] == "y")

def run_triangle_bot_9002_once():

    length1 = get_numerical_input("Enter length of first triangle \n")
    width1 = get_numerical_input("Enter width of first triangle \n")
    length2 = get_numerical_input("Enter length of second triangle \n")
    width2 = get_numerical_input("Enter width of second triangle \n")

    area1 = length1 * width1
    area2 = length2 * width2
    
    if area1 > area2:
        print("The first rectangle has the greater area \n")
    elif area1 < area2:
        print("The second rectangle has the greater area \n")
    else:
        print("Both have the same area. \n")

print("Hello and welcome to Triangle Bot 9002. "
      + "This program measures the length and width of two triangles and tells you which has the greater area. \n")

run_triangle_bot_9002_once()

if did_user_say_yes("Would you like to run Triangle Bot 9002 again?"):
  print("Okay, reinitializing...")
  time.sleep(.900)
  run_triangle_bot_9002_once()
else:
  print("Okay, thanks for using the Triangle Bot 9002.")
