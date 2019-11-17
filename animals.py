# defined a parent class with a function inside it.
class Animals:
	def a_type(self):
		print "It is a pet animal"
		
# inherited the parent class Animals in the child class rabbit.
class Rabbit(Animals):
	def charcteristics(self):
		print "It is really soft"
		print "Its color can be either pink or white"
		print "It is my favourite pet animal"

# created a constructor to call the child class.
b1 = Rabbit()
# with the use of constructor we are printing the values of the child class as well as calling the function from the parent class and child class.
b1.a_type()
b1.charcteristics()