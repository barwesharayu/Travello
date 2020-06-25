# convert europian floors into US floors

#iflrnum = input('Enter floor number ')
#usflrnum = int(iflrnum) + 1
#print('US floor is ', usflrnum)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)