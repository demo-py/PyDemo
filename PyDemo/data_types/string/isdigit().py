"""

  str.isdigit()

  Checks if all characters in the string are digits

"""

string : str = "5293"
print(
  string.isdigit()
)

# Output :
# True

# ====================
#
# Contains alphabets :

string : str = "admin123"
print(
  string.isdigit()
)

# Output :
# False

# ========================
#
# Contains a superscript :

string : str = "2²"
print(
  string.isdigit()
)

# Output :
# True