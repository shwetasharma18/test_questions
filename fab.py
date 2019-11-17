n = input("enter a num :- ")

i = 0

j = 1

if n < 0:
	print "enter a positive integer"

if n == 0 or n > 1:
	print i

if n == 1 or n > 1:
	print j

k = 2

while k < n:
   
    l = i + j
    
    i = j
    
    j = l
    
 
    print j
    
    k = k + 1


