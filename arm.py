user = input(" enter your input :- " )

user1 = str(user)

if len(user1) > 4 and len(user1) < 3:
    print "invalid input, the input should be a 3 digit number"

sum_of_num = int(user1[0])**3 + int(user1[1])**3 + int(user1[2])**3

if user == sum_of_num:
    print "yes it is an armstrong number"
    
else:
    print "No it is not an armstrong number"
  