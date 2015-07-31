import commands


def large_list(inp, endlist):
    if inp[-1] == 9:
        if len(inp) == 1:
            endlist.insert(0, 0)
            endlist.insert(0, 1)
            return endlist
        else:
            endlist.insert(0, 0)
            inp.pop(-1)
            large_list(inp, endlist)
    else:
        endlist.insert(0, inp.pop(-1) + 1)
        while len(inp) > 0:
            endlist.insert(0, inp.pop(-1))
    return endlist


def sparse(inpList):
    totalSum = 0
    vectDict = {}
    vectList = inpList[1:]
    for pair in vectList:
        pair = pair.split()
        if pair[0] in vectDict:
            totalSum += int(vectDict[pair[0]]) * int(pair[1])
        else:
            vectDict[pair[0]] = pair[1]
    return totalSum



def  say_what_you_see(input_strings):
    returnList = []
    for string in input_strings:
        repeat = string[0]
        actual = string[1:] + " "
        times = 1
        result = ""
        for char in actual:
            if char != repeat:
                result += str(times) + repeat
                times = 1
                repeat = actual
            else:
                time+=1
        returnList.append(result.strip())
    # for string in returnList:
    #     print string
    return returnList



def anagram(str1, ana1):
  inp1 = ''
  inp2 = ''
  for char in str1:
    if char.isalpha():
      inp1 = inp1 + char.lower()
  for char in ana1:
    if char.isalpha():
      inp2 = inp2 + char.lower()
  if sorted(inp1) == sorted(inp2):
    return True
  else:
    return False 

def unique(string):
  stringDict = {}
  for char in string:
    if char in stringDict:
      stringDict[char] += 1
    else:
      stringDict[char] = 1
    if stringDict[char] > 2:
      return False
  return True  

def substitute(key, code):
  keyDict = {}
  numString = ''
  for num in range(10):
    keyDict[key[num]] = num+1
  keyDict[key[9]] = 0
  for char in code:
    if char in keyDict:
      numString += str(keyDict[char])
  return int(numString)


def verbing(s):
  # +++your code here+++
  if len(s) > 2:
    if s[-3:] == 'ing':
      s += 'ly'
    else:
      s += 'ing'

  return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  notPos = s.find('not')
  badPos = s.find('bad')
  
  if (notPos and badPos) > 0 and notPos < badPos:
    s = s.replace(s[notPos:(badPos+3)], 'good')

  return s

## Given a dir path, run an external 'ls -l' on it --
## shows how to call an external program
def listdir(dir):
    cmd = 'ls -l ' + dir
    print "Command to run:", cmd   ## good to debug cmd before actually running it
    (status, output) = commands.getstatusoutput(cmd)
    if status:    ## Error case, print the command's output to stderr and exit
        sys.stderr.write(output)
        sys.exit(1)
    print output  ## Otherwise do something with the command's output



def split_string(a):
  split = []
  if len(a) % 2 == 1:
    split.append(a[:len(a)/2 + 1])
    split.append(a[len(a)/2 + 1:])
  else:
    split.append(a[:len(a)/2])
    split.append(a[len(a)/2:])
  
  return split

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++

  a = split_string(a)
  b = split_string(b)


  return a[0] + b[0] + a[1] + b[1]

  


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

    print
    print 'large_list'
    test(large_list([1,2,3],[]),[1,2,4])
    test(large_list([9,9,9],[]),[1,0,0,0])
    test(large_list([1,2,9],[]),[1,3,0])
    test(large_list([1,2,4,5,9,8,6],[]),[1,2,4,5,9,8,7])

    print
    print 'unique'
    test(unique('abc'), True)
    test(unique('aaa'), False)
    test(unique('abd'), True)

    print
    print 'substitute'
    test(substitute('TRADINGFEW','LGXWEV'),709)

    print
    print 'anagram'
    test(anagram('Arrigo Boito','Tobia Gorrio'), True)
    test(anagram('anagram','nag-a-ram'), True)
    test(anagram('zdklsd','sdfkljsdfs'), False)

    print
    print 'sparse'
    test(sparse(['3 3', '1 4', '4 2', '5 3', '1 7', '2 6', '5 1']), 31)

    print
    print 'directory path'
    listdir('~/Dev/PyCon/')

    print
    print 'say_what_you_see'
    test(say_what_you_see(['12','21']),['1112','1211'])

if __name__ == '__main__':
    main()
