"""

  str.isnumeric()

  Checks whether the string consists of numeric characters or not

"""

string : str = "12330"
print(string.isnumeric())

# Output :
# True

# =======================

string : str = "admin123"
print(string.isnumeric())

# Output :
# False

# =================
#
# Contains SPACEs :

string : str = "good bye"
print(string.isnumeric())

# Output :
# False

# ====================
#
# Contains fractions :

string : str = "⅓"
print(string.isnumeric())

# Output :
# True

# ====================================
#
# Contains subscripts / superscripts :

string : str = "²"
print(string.isnumeric())

# Output :
# True

# ================================================
#
# Contains roman numerals ( written in unicode ) :
# VIII = roman numeral eight

string : str = "2167"
print(string.isnumeric())

# Output :
# True