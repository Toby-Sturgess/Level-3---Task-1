# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")       # Syntax error, forgot to add brackets
print("\n")         #Syntax error, forgot to add brackets was also indented

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"       # Syntax error, code doesn't need to be indented, also one too many = added. Need to remove "years old" to fix runtime error 
age = int(age_Str)      # Syntax error and Runtime error, code is indented and trying to turn a word into an integer, will need to change previous line to fix

# I would also like to add that in this case it is useless declaring a variable and then casting that same variable into another, far more efficient to only declare the second variable as 24. But for the sake of showing I know what errors are in place I've left them both in

print("I'm " + str(age) + " years old.")       # Runtime error, need to cast int into str. Syntax error, code indented.

# Variables declaring additional years and printing the total years of age
years_from_now = 3        # Need to change from a str to int to fix Logical error. Also syntax error as code was indented.
total_years = age + years_from_now      # Logical error, will give you 243 rather than 27. Syntax error, Code was indented

print("How old I'll be in 3 years time: " + str(total_years))   # Syntax error, forgotten brackets, variable answer_years is encased in "" and is also the wrong variable. Runtime error, need to cast to str.
# ^this print statement also doesn't make sense with what is being presented, I've changed it to make sense.

# Variable to calculate the total amount of months from the total amount of years and printing the result.
total_months = total_years * 12       # Syntax error, wrong variable used.
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")       # Syntax error, forgotten brackets. Runtime error, need to cast to str. Logical error in that we haven't calculated the extra 6 months. I've fixed it by adding the extra 6 months

#HINT, 330 months is the correct answer

