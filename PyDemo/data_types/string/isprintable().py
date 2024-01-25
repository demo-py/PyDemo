"""

  str.isprintable()

  Checks if all characters in the string are printable or the string is empty

  ===========================================================================

  Printable Characters :

  Digits ( 0123456789 )

  Uppercase letters ( ABCDEFGHIJKLMNOPQRSTUVWXYZ )

  Lowercase letters ( abcdefghijklmnopqrstuvwxyz )

  Punctuation characters ( !”#$%&'()*+, -./:;?@[\]^_`{|}~ )

  Space (  )

"""

string : str = "pydemo"
print(string.isprintable())

# Output :
# True

# ================================

string : str = "welcome to pydemo"
print(string.isprintable())

# Output :
# True

# ================================
#
# Case : empty string

string : str = ""
print(string.isprintable())

# Output :
# True

# ==================================
#
# Case : escape characters

string : str = "escaping\ncharacter"
print(string.isprintable())

# Output :
# False