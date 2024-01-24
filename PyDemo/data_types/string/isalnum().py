"""

  str.isalnum()

  Checks whether all the characters in a given string are either alphabet or numeric characters

"""

string : str = "demo123"
print(
  string.isalnum()
)

# Output :
# True

# =======================

string : str = "demo 123"
print(
  string.isalnum()
)

# Output :
# False

# =======================

string : str = "demo_123"
print(
  string.isalnum()
)

# Output :
# False

# ====================

string : str = "abcde"
print(
  string.isalnum()
)

# Output :
# True

# ====================

string : str = "01234"
print(
  string.isalnum()
)

# Output :
# True