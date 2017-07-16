from sys import argv

script, filename = argv

print "Erasing file %r." % filename
print "To continue, hit RETURN. To cancel, hit CTRL-C (^C)."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file..."
target.truncate()

print "Please provide three lines:"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Writing lines to the file..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "Closing file..."
target.close()

print "Complete"