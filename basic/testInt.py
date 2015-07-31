

def largeList(inp):
  carry = 0
  endList = []

  while len(inp) > 1:
    if inp[-1] == 9:
      endList.insert(0 + carry, 0)
      carry = 1
      inp.pop(-1)
    else:
      endList.insert(inp.pop(-1) + carry, 0)
      carry = 0

  if inp == 9:
    endList.insert(0, 0)
    endList.insert(1, 0)
  else:
    endList.insert(inp.pop(-1) + carry, 0)
  return endList
#rovided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
 
  print
  print 'large list'
  test(largeList([1,2,3,4], [1,2,3,5])



# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
