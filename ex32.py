the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also can go through mixed lists too
# notice the use of %r since the type may vary
for i in change:
	print "I got %r" % i
	
# lists can also be built, start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
	
# now print the new elements
for i in elements:
	print "Element was: %d" % i