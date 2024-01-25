"""

  str.istitle()

  Checks if all the words in the string are title cased

"""

string : str = "Pydemo"
print(string.istitle())

# Output :
# True

# ================================

string : str = "Welcome to Pydemo"
print(string.istitle())

# Output :
# False

# ========================
#
# Case : contains digit(s)
# Note : digits are ignored

string : str = "Day 25"
print(string.istitle())

# Output :
# True