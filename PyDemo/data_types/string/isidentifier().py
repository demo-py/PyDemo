"""

  str.isidentifier()

  Checks whether a string is a valid identifier or not

  ====================================================

  A string is considered as a valid identifier if :

  1. Only consists of alphanumeric characters and UNDERSCORE
  2. Doesn't start with a SPACE or a number

"""

string : str = "pydemo"
print(
  string.isidentifier()
)

# Output :
# True

# ======================

string : str = "py_demo1"
print(
  string.isidentifier()
)

# Output :
# True

# =====================
#
# Case : empty string :

string : str = ""
print(
  string.isidentifier()
)

# Output :
# False

# ==================================
#
# Case : beginning with an integer :

string : str = "1ml"
print(
  string.isidentifier()
)

# Output :
# False