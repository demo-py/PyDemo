"""

  str.isalpha()

  Checks whether all characters in the string are an alphabet

"""

string : str = "demo"
print(
  string.isalpha()
)

# Output :
# True

# =========================

string : str = "abcde12345"
print(
  string.isalpha()
)

# Output :
# False

# ==========================
#
# SPACE is not an alphabet :

string : str = "demo testing"
print(
  string.isalpha()
)

# Output :
# False

# ===============================
#
# UNDERSCORE is not an alphabet :

string : str = "demo_testing"
print(
  string.isalpha()
)

# Output :
# Falsee