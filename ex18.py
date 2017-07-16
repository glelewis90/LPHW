# this one is like scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# to define number of arguments:
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this takes no arguments
def print_none():
	print "Nothing"

print_two("Glenn","Lewis")
print_two_again("Lewis","Glenn")
print_one("Glenn")
print_none()