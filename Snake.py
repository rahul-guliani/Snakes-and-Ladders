'''
---------------

'''
for i in range(1, 11):
    for j in range(1, 11):
        if i % 2 == 0:  # If it is odd number of row starting from 1
            print(str(10 * (10 - i) + j).rjust(3), end=' ')
        else:   # Reverse the column numbering for even no. rows 
            print(str(10 * (10 - i) + (11 - j)).rjust(3), end=' ')
    print()
