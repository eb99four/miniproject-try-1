print ('task 1') #1
star = ""
for i in range(1, 6):
    star = star + "*"
    print(star)
    length = len(star)
    if length == 5:
        for i in range(6):
            print('*' * (length - 1))
            length = length - 1

#print ('task 2') #2
#def print_pattern(rows):
#    """Prints a pattern of asterisks, with the given number of rows.
 #   Args:
   #     rows: The number of rows in the pattern.
  #  """

   # for i in range(rows):
    #    for j in range(rows):
     #       if i == j or i + j == rows - 1:
      #          print('*', end='')
       #     else:
        #        print(' ', end='')
        #print()


#if __name__ == '__main__':
 #   print('Printing a pattern with 10 rows.')
  #  print_pattern(10)

print ('task 2') #2
for i in range(1, 6):
  spaces = " " * (i-1)
  print(spaces + "*")

length = 6
for i in range(length - 1):
  spaces = " " * (length - i - 1)
  print(spaces + "*")

print ('task 3') #3
for i in range(3):
  for j in range(1, 6):
    spaces = " " * (j-1)
    print(spaces + "*")

  for j in range(5, 0, -1):
    spaces = " " * (j-1)
    print(spaces + "*")


     


