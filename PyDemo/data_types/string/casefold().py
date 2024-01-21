"""

str.casefold()

Convert string to lowercase

"""

string = "Sample STRING"
print(string.casefold())

# Output :
# sample string


"""

Similar to str.lower() except it is more aggressive to lowercase characters
because it tends to remove all case distinctions in a string.

"""

string = "ß"
print(string.casefold())

# Output :
# ss