"""

  str.format(
    value : Any
  )

  Returns a formatted string with the value passed as parameter in the placeholder position

  =======================================================================================================

  Parameters :

  value : Any = can be an integer, floating point, numeric constant, string, characters or even variables

  =======================================================================================================

  Type Specifying :

  %s -- string conversion
  %c -- character conversion
  %i -- signed decimal integer
  %d -- signed decimal integer ( base-10 )
  %u -- unsigned decimal integer
  %o -- octal integer
  f --- floating-point displayy
  b --- binary number
  o --- octal number
  x --- hexadecimal with loercase letters after 9
  X --- hexadecimmal with uppercase letters after 9
  e --- exponent notation

  =======================================================================================================

  Padding Substitutions or Generating Spaces

  By default :
    strings are left-justified
    numbers are right-justified

  < : left-align text
  ^ : center text
  > : right-align text

"""

# syntax : {[index]:[width].[precision][type]}
# values of these placeholders are ordered inside the .format() method

string = "welcome to {}"

print(
  string.format("PyDemo")
)

# welcome to PyDemo

# ===========================================
#
# decimal syntax : {var:.nf}
# where :
#   var : int = a variable of type INT
#   n   : int = amount of decimals to take in

string : str = "Score : {score:.2f}"
print(
  string.format(
    score = 10
  )
)

# Score : 10.00

# =============================
#
# Using multiple placeholders :
# syntax : {} {}

string : str = "My name is {} and I'm {} years old"
print(
  string.format(
    "demo",
    18
  )
)

# My name is demo and I'm 18 years old

# ====================================
#
# Using positional arguments :
# syntax : {n} {n}
# where :
#   n : int = the n-th place in the arguments of .format()

string : str = "this part of {1} is {0}"
print(
  string.format(
    "easy",
    "code"
  )
)

# this part of code is easy

# =========================================================================================
#
# Using keyword arguments :
# syntax : {var} {var}
# where :
#   var : Any = any type of data : string, integer, float, character, a variable, et cetera

string : str = "{name} is {1} at coding, {0}"
print(
  string.format(
    "not",
    "good",
    name = "demo"
  )
)

# demo is good at coding, not

# ===========================
#
# Using Type Specifying :
#
# syntax : "str" % (args, kwargs)
#
# %s -- string conversion via str() prior to formatting

string : str = "sample string"
print(
  "%s" % (string)
)

# sample string

# ===================================
#
# %c -- character prior to conversion

string : str = "d"
print(
  "%c" % (string)
)

# d

# ============================
#
# %i -- signed decimal integer

count : int = -1.000
print(
  "%i" % (count)
)

# -1

# ========================================
#
# %d -- signed decimal integer ( base-10 )

count : int = 1.000
print(
  "%d" % (count)
)

# 1

# ===============================
#
# %u -- unsigned decimmal integer

count : float = 1.000
print(
  "%u" % (count)
)

# 1

# ===================
#
# %o -- octal integer

count : int = 1_000
print(
  "%o" % (count)
)

# 1750

# ============================
#
# f -- floating-point display

count : float = 1.000
print(
  "{:f}".format(
    count
  )
)

# 1.000000

# ==================
#
# b -- binary number

count : int = 18
print(
  "{:b}".format(
    count
  )
)

# 10010

# ==================
#
# %o -- octal number

count : int = 18
print(
  "{:o}".format(
    count
  )
)

# 22

# ===============================================
#
# x -- hexadecimal with lowercase letters after 9

integer : int = 15
print(
  "{:x}".format(
    integer
  )
)

# f

# ================================================
#
# X -- hexadecimal with uppercasee letters after 9

integer : int = 15
print(
  "{:X}".format(
    integer
  )
)

# F

# ======================
#
# e -- exponent notation

integer : int = 2
print(
  "{:e}".format(
    integer
  )
)

# 2.000000e+00

# ===================================
#
# You can also use {:} instead of % :

integer : int = 2.16849
print(
  "it's approximately {:.2f} cm".format(integer)
)

# it's approximately 2.17 cm

# =========================================
#
# Padding Subsitutions or Generating Spaces
#
# < : left-align text

string : str = "demo"
integer : int = 18
print(
  """{0:5}
{1:5}
{0:<5}
{1:<5}""".format(
    string,
    integer
  )
)

# demo
#    18
# demo
# 18

# ---------------
#
# ^ : center text

string : str = "demo"
integer : int = 18
print(
  """{0:5}
{1:5}
{0:^5}
{1:^5}""".format(
    string,
    integer
  )
)

# demo
#    18
#  demo
#   18

# --------------------
#
# > : right-align text

string : str = "demo"
integer : int = 18
print(
  """{0:5}
{1:5}
{0:>5}
{1:>5}""".format(
    string,
    integer
  )
)

# demo
#    18
#  demo
#    18

# ==================
#
# Using a dictionary

string : str = "{greeting} ! Soy {name} y soy {age} anos"
dictionary : dict = {
  "greeting": "hola",
  "age": 18,
  "name": "demo"
}

# use the " ** " operator to unpack the values from a dict

print(string.format(**dictionary))

# Output :
# hola ! Soy demo y soy 18 anos

# =============================
#
# Using lists

num_list : list = [85.641, 90.158, 89.99, 88.8]
rounded_num : list = ["{:.2f}".format(num) for num in num_list]
print(rounded_num)

# Output :
# ["85.64", "90.16", "89.99", "88.80"]