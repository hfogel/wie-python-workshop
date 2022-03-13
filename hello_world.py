# ------------------------------------------------------------------------------ #
# ----------------- WIE Winnipeg's High School Python Workshop ----------------- #
# ---------------------- An Introduction to Python Basics ---------------------- #
# ------------------------------- March 13, 2022 ------------------------------- #
# ------------------------------------------------------------------------------ #


# Lesson 1 - Variables and Loops
# Variables in Python are similar to variables in math class:
x = 2
y = 5

# Once defined, we can use these variables by name:
print(x + y)
product = x * y
print(product)

# We can name variables whatever we want, and can also have variables that aren't numbers!
name = "Hannah"  # note the "" around my name (this is called a STRING)
my_dogs = ["Jax", "Ozzy"]  # putting things inside [] makes a LIST

# We can access the items in a list using INDEXING:
print(my_dogs[1])  # this has an unexpected result! (Python uses 0-based indexing)

# We can also find out how many items are in a list using the LEN function:
print(len(my_dogs))

# What if I had a long list of dog names, and wanted to print them all?
# There is a much faster way than:
# print(my_dogs[0])
# print(my_dogs[1])
# print(my_dogs[2])
# ...
# print(my_dogs[99])

# The more efficient way is to use a LOOP. There are two different kinds of LOOPS in Python that we will cover

# A FOR LOOP looks like this:
for number in range(1, 5):
    print(number)
# Pay special attention to the colon (:) at the end of the first line, and the fact that the next line is indented.
# These two things are part of Python's syntax rules.
# Also notice that when we use the RANGE function, the NUMBER variable starts at the provided start point (1)
# and goes up to, but does not include, the provided end point (5).
# If we want the index to start at 0, we don't need to provide a start point at all.
# Eg. range(5) is equivalent to range(0, 5)


# The looping variable doesn't have to be a number; we can loop through each of the items in a list like this:
for dog in my_dogs:
    print(f"{dog} is a good boy!")

# We can also use the LEN function to loop through the items in a list by index, rather than the items themselves
x_list = [5, 14, 23]
y_list = [3, 40, 12]
for index in range(len(x_list)):
    print(x_list[index] + y_list[index])

# A WHILE LOOP has similar behaviour, but is controlled a little differently.
# The lines in a while loop get executed over and over again until the while (STATEMENT) part is no longer true
countdown = 10
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
print("Blast Off!!!!")

# A key difference between FOR and WHILE loops is that a FOR LOOP runs for a pre-determined number of iterations
# (the index variable gets incremented automatically), whereas a WHILE LOOP could run forever -
# we're in charge of stopping it by changing the value of the loop variable

# -------------------------------------------------------------------- #
# ------------------------- Coding Challenge ------------------------- #
# Define three new variables:                                          #
#   NAME (your name), CITY (where you were born), YEAR (you were born) #
# Use the PRINT function to display:                                   #
#   <your name> was born in <city> in <year>                           #
# -------------------------------------------------------------------- #

# -------------------------------------------------------------------- #
# ------------------------- Coding Challenge ------------------------- #
# Predict the value of the DIRECTION variable after the following      #
# lines are executed:                                                  #
#   initial = "left"                                                   #
#   direction = initial                                                #
#   initial = "right"                                                  #
# Was your prediction correct? Try it out and see.                     #
# -------------------------------------------------------------------- #


# -------------------------------------------------------------------- #
# Lesson 2 - Conditionals
# Sometimes we only want to execute a particular block of code under certain conditions.
# For example, what if we only wanted to print numbers less than or equal to 5 in our countdown?
countdown = 10
print("Counting down...")
while countdown > 0:
    if countdown <= 5:  # Note the colon (:) and indent!
        print(countdown)
    countdown = countdown - 1
print("Blast Off!!!!")

# We can also add an ELSE statement:
countdown = 10
print("Counting down...")
while countdown > 0:
    if countdown <= 5:
        print(countdown)
    else:
        print("Countdown is greater than 5!")
    countdown = countdown - 1

# -------------------------------------------------------------------- #
# ------------------------- Coding Challenge ------------------------- #
#       Modify the above block of code to count up instead of down!    #
# -------------------------------------------------------------------- #


# --------------------------------------------------------------------
# Lesson 3 - Defining Functions
# We've already used a few of Python's built-in functions (RANGE, LEN, PRINT).
# These are really handy, but don't cover everything we may want to do.
# We can also create our own functions. For example:
def compute_speed(distance, time):
    speed = distance / time
    return speed
# The DEF keyword means "define a function";
# whatever comes next is the name of the function - it can be whatever you want!
# Inside the brackets are the INPUT ARGUMENTS - these are the parameters we give to the function.
# At the end is the RETURN keyword - the variables listed here get passed back to the calling program.


# Example usage of compute_speed():
d = 1036    # [km]
t = 9.4  # [h]
s = compute_speed(d, t)
print(f"My speed is {s} km/h")
# Note that our compute_speed function does not take units into consideration - this is left to the user!


def say_hello(name, language):
    if language == "English":   # note the double equals (==) here, distinguishing from setting a variable
        print(f"Hello, {name}!")
    elif language == "French":  # ELIF = ELSE, IF
        print(f"Bonjour, {name}!")
    else:
        print("Sorry, I don't know that language :(")


say_hello("Maya", "French")
say_hello("Jasmin", "English")
say_hello("Alex", "Spanish")

# -------------------------------------------------------------------- #
# ------------------------- Coding Challenge ------------------------- #
#           Add a new language option to the say_hello function!       #
# -------------------------------------------------------------------- #

# -------------------------------------------------------------------- #
# ------------------------- Coding Challenge ------------------------- #
#       Write your own function that computes an equation              #
#                   you learned in physics class                       #
# -------------------------------------------------------------------- #
