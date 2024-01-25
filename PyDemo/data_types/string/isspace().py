"""

  str.isspace()

  Checks if all characters in the string are whitespace characters

  ================================================================

  Considered whitespace characters :

  " " : Space

  "\t" : Horizontal Tab

  "\n" : New line

  "\v" : Vertical Tab

  "\f" : Feed

  "\r" : Carriage return

"""

string : str = "\n\t"
print(string.isspace())

# Output :
# True

# ===========================================
#
# Case : contains non-whitespace characters :

string : str = "pydemo"
print(string.isspace())

# Output :
# False

# ==========================================================
#
# Case : contains non-whitespace and whitespace characters :

string : str = "welcome\tto\tpydemo"
print(string.isspace())

# Output :
# False