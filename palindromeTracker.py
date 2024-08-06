class PalindromeTracker:

  def __init__(self):

    self.string = ""

    self.trailingPalindromes = []

  def clear(self):

    self.__init__()

  def track(self, char):

    self.string += char

    length = len(self.string)

    newTrailing = [ length - 1 ]

    self.string[length - 2] == char

    newTrailing.append(length - 2)

    for index in self.trailingPalindromes:

      if index > 0 and self.string[index - 1] == char:

        newTrailing.append(index - 1)

    self.trailingPalindromes = newTrailing

  def isPalindrome(self):

    return bool(self.trailingPalindromes and 0 == self.trailingPalindromes[-1])
