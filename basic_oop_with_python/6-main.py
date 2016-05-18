from circle import Circle

''' guillaume's test case '''
print "guillaume's test case"
c1 = Circle(4)
c1.set_center([0, 0])
c1.name = "Sun"

c2 = Circle(4)
c2.set_center([1, 1])
c2.name = "Earth"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: whatever's on the intranet\n"

''' RADIUS = 0 '''
''' if they are the same point '''

print "RADIUS = 0"
print "================"
print "if they are the same point"

c1 = Circle(0)
c1.set_center([0, 0])
c1.name = "Mercury"

c2 = Circle(0)
c2.set_center([0, 0])
c2.name = "Mercury"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 100%\n"

''' if they are different points '''
print "if they are different points"
c1 = Circle(0)
c1.set_center([0, 0])
c1.name = "Mercury"

c2 = Circle(0)
c2.set_center([0, 10])
c2.name = "Pluto"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 0%\n"

''' RADIUS > 0 '''
''' if they do not overlap at all '''
print "RADIUS > 0"
print "================\n"

print "if they do not overlap at all (outside of each other)"

c1 = Circle(1)
c1.set_center([0, 0])
c1.name = "Jupiter"

c2 = Circle(2)
c2.set_center([0, 10])
c2.name = "Neptune"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 0%\n"

''' if they are kissing from the outside '''
print "if they are kissing from the outside"
c1 = Circle(1)
c1.set_center([0, 0])
c1.name = "Venus"

c2 = Circle(1)
c2.set_center([0, 2])
c2.name = "Mars"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 0%\n"

print "if they are kissing and one is inside the other"
c1 = Circle(2)
c1.set_center([0, 0])
c1.name = "Earth"

c2 = Circle(1)
c2.set_center([0, 1])
c2.name = "Mars"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: some positive number\n"

print "if they switch places"
c1 = Circle(1)
c1.set_center([0, 1])
c1.name = "Mars"

c2 = Circle(2)
c2.set_center([0, 0])
c2.name = "Earth"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 100%\n"

print "if they are inside each other but not kissing (take 1)"
c1 = Circle(4)
c1.set_center([0, 0])
c1.name = "Earth"

c2 = Circle(1)
c2.set_center([0, 2])
c2.name = "Mars"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: some positive number\n"

print "if they switch places (take 1)"
c1 = Circle(1)
c1.set_center([0, 2])
c1.name = "Mars"

c2 = Circle(4)
c2.set_center([0, 0])
c2.name = "Earth"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 100%\n"

print "if they are inside each other but not kissing (take 2)"
c1 = Circle(4)
c1.set_center([0, 0])
c1.name = "Earth"

c2 = Circle(1.9)
c2.set_center([0, 2])
c2.name = "Mars"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: some positive number\n"

print "if they switch places (take 2)"
c1 = Circle(1.9)
c1.set_center([0, 2])
c1.name = "Mars"

c2 = Circle(4)
c2.set_center([0, 0])
c2.name = "Earth"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 100%\n"

print "if they are inside each other but not kissing (take 3)"
c1 = Circle(4)
c1.set_center([0, 1])
c1.name = "Earth"

c2 = Circle(2)
c2.set_center([0, 2])
c2.name = "Mars"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: some positive number\n"

print "if they switch places (take 3)"
c1 = Circle(2)
c1.set_center([0, 2])
c1.name = "Mars"

c2 = Circle(4)
c2.set_center([0, 1])
c2.name = "Earth"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 100%\n"

print "if they are concentric, different sizes"
c1 = Circle(4)
c1.set_center([0, 0])
c1.name = "Earth"

c2 = Circle(3)
c2.set_center([0, 0])
c2.name = "Mars"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: some positive number\n"

print "if they switch places"
c1 = Circle(3)
c1.set_center([0, 0])
c1.name = "Mars"

c2 = Circle(4)
c2.set_center([0, 0])
c2.name = "Earth"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 100%\n"

print "if they are concentric, same size"
c1 = Circle(5)
c1.set_center([0, 0])
c1.name = "Earth"

c2 = Circle(5)
c2.set_center([0, 0])
c2.name = "Mars"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: some positive number\n"

print "if they switch places"
c1 = Circle(5)
c1.set_center([0, 0])
c1.name = "Mars"

c2 = Circle(5)
c2.set_center([0, 0])
c2.name = "Earth"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
print "Expected: 100%\n"
