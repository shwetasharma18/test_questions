
user = int(raw_input("enter a num :- "))

i = 2

while i < user:
    
    if user % i == 0:
    
        print "no it is not a prime number"
    
        break
    
    i = i + 1

else:
    print "yes it is a prime number"