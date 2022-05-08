my_string = "coding**is**cool"
are_all_letters = [char.isalpha() for char in my_string]
print(all(are_all_letters))
#False

my_string = "56456278"
are_all_digits = [char.isdigit() for char in my_string]
print(all(are_all_digits))
# True





