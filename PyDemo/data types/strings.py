from typing import Optional

sample : str = "This is a String"
sample : str = 'This is also a String'

sample : str = "Sample string"

class StringMethods:
  def capitalize(
    self
  ) -> str:
    # Sample string
    string = "sample string"
    return string.capitalize()

  def casefold(
    self
  ) -> str:
    # sample string
    string = "Sample String"
    return string.casefold()

  def center(
    self,
    length : int = 23,
    fillchar : Optional[str] = " "
  ) -> str:
    #      Sample string     
    string = "Sample string"
    return string.center(length, fillchar)

  def count(
    self,
    substring : str = "a",
    start : Optional[int] = 0,
    end : Optional[int] = 5
  ) -> int:
    # 2
    string = "aboard"
    return string.count(substring, start, end)

  def encode(
    self,
    encoding : str = "utf-8",
    errors : Optional[str] = "ignore"
  ) -> str:
    # b'S'
    string = "S"
    return string.encode(encoding, errors)

  def endswith(
    self,
    suffix : str = "ing",
    start : Optional[int] = 0,
    end : Optional[int] = 6
  ) -> bool:
    # True
    string = "string"
    return string.endswith(suffix, start, end)

  def expandtabs(
    self,
    tabsize : int = 8
  ) -> str:
    #         string        
    string = "\tstring\t"
    return string.expandtabs(tabsize)

  def find(
    self,
    sub : str = "str",
    start : Optional[int] = 0,
    end : Optional[int] = 6
  ) -> int:
    # 0
    string = "string"
    return string.find(sub, start, end)

  def format(
    self,
    value = "any value",
    value2 = "at all"
  ) -> str:
    # format with any value at all
    string = "format with {} {}"
    return string.format(value, value2)

  def format_map(
    self,
    map : dict = {
      "x": 5,
      "y": 25
    }
  ) -> str:
    # coordinate : 5, 25
    string = "coordinate : {x}, {y}"
    return string.format_map(map)

sample = StringMethods()
print(sample.format_map())