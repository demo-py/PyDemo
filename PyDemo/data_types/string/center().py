"""

str.center(
  length : int,
  fillchar : Optional[str] = " "
)

Returns a new string that is padded with the specified character


Parameters:

Length : length of the string after padding with the characters

fillchar : ( optional ) characters which need to be padded. If it's not provided, spacec is taken as the default argument

"""

string = "sample string"
print(
  string.center(
    23,
    "#"
  )
)

# Output :
# #####sample string#####


"""

if LENGTH is less than the original string length, it returns the string as is

"""

string = "sample string"
print(
  string.center(
    10,
    "$"
  )
)

# Output :
# sample string