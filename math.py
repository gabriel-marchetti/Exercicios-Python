from math import sin

# Change the list below to whatever x values you wish to see evaluated.
# Make sure you keep it in list format (include [] around your list!)
x_vals = [0,.125, .25, 0.5, 1, 1.5, 2]  

for x in x_vals:
	print("When x =", x)
	try:
        # the function we want to see what happens as x approaches 0
		print("y = " , sin(x) /x, "\n")
	except  ZeroDivisionError: 
		print("Error! Cannot Divide By Zero!\n")