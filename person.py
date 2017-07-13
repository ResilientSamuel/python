#this area shows name,age, and calcutions

def get_age():
		age = (int)(raw_input("whats your age?"))
		return age
		
def get_name():
		return raw_input ("whats your name?")
		
		age = get_age()
		name = get_name()
		
print "Hey, " + name + ", you are " + str(age) + "years old, dude!"
		
def calculate(op1, op2, f):
	if f == "add":
	   return op1 + op2
	elif f == "subtract":
		return op1 - op2
	elif f == "division":
		return op1 / op2
		
value = calculate(4,5 "add")
print value
		
