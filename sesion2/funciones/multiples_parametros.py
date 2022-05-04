def foo( first, second, third, *therest):
	print("First: ", first)
	print("Second: ", second)
	print("Third: ", third)
	print("Rest of the parameters: ", list(therest))
	return first, second, third , list(therest)

var1, var2,var3,var_list= foo( "Monday",  "Tuesday",  "Wednesday",  "Thursday", "Friday", "Saturday")
print(var1,var2,var3,var_list)
