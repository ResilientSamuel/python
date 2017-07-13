i = 8
if(i % 2):
    print "8%2"
    
else:
    print "Even Number"
    
print"\n"
def isEven(number):
	return number % 2 == 0

isEven(3)

def evens(numbers):
	acc = 0
	for i in numbers:
		if(i % 2==0):
			acc = acc + i
	return acc
	
	
print evens([1,6,3,7,5,8])
print evens([76,9,43,7])
