"""

  str.isdecimal()

  Checks if all characters in a string  are decimal

"""

string : str = "3412"
print(
  string.isdecimal()
)

# Output :
# True

# =================
#
# Contains SPACEs :

string : str = "25 1346"
print(
  string.isdecimal()
)

# Output :
# False

# ====================
#
# Contains alphabets :

string : str = "1a2b3c"
print(
  string.isdecimal()
)

# Output :
# False