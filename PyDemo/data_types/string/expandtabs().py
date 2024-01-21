"""

  str.expandtabs(
    tabsize : Optional[int] = 8
  )

  Specifies the amount of space to be substituted with the "\t" symbol in the string

  ==============================================================================================

  Parameters :

  tabsize : int = specifies the space that is to be replaced with the "\t" symbol in the string.
                  By default the space is 8

  ==============================================================================================

"""

string = "sample\tstring"
print(string.expandtabs())

# Output :
# sample        string


print(string.expandtabs(4))

# Output ;
# sample    string