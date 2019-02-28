import time

def triangleArea():
    length1 = int(input("Enter length of first triangle \n"))
    width1 = int(input("Enter width of first triangle \n"))
    length2 = int(input("Enter length of second triangle \n"))
    width2 = int(input("Enter width of second triangle \n"))
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
triangleArea()

while True:
    answer = input("Would you like to run TriangleBot9002 again? \n").lower().strip( )
    if answer == "yes":
        print("Okay, reinitializing...")
        time.sleep(.900)
        triangleArea()
    else:
        print("Okay, thanks for using the Triangle Bot 9002")
        break
