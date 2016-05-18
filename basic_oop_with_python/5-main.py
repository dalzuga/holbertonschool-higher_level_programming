from circle import Circle

c1 = Circle(4)
c1.set_center([0, 0])
c1.name = "Sun"

c2 = Circle(4)
c2.set_center([1, 1])
c2.name = "Earth"

if c1.intersection(c2):
    print "Intersection between %s and %s" % (c1.name, c2.name)
else:
    print "No intersection between %s and %s" % (c1.name, c2.name)
print "Expected: intersection"


c1 = Circle(2.5)
c1.set_center([0, 0])
c1.name = "Mercury"

c2 = Circle(2.5)
c2.set_center([4, 3])
c2.name = "Venus"

if c1.intersection(c2):
    print "Intersection between %s and %s" % (c1.name, c2.name)
else:
    print "No intersection between %s and %s" % (c1.name, c2.name)
print "Expected: intersection"

c1 = Circle(2.4)
c1.set_center([0, 0])
c1.name = "Mercury"

c2 = Circle(2.5)
c2.set_center([4, 3])
c2.name = "Earth"

if c1.intersection(c2):
    print "Intersection between %s and %s" % (c1.name, c2.name)
else:
    print "No intersection between %s and %s" % (c1.name, c2.name)
print "Expected: no intersection"

c1 = Circle(6.5)
c1.set_center([0, 0])
c1.name = "Mars"

c2 = Circle(6.5)
c2.set_center([5, 12])
c2.name = "Earth"

if c1.intersection(c2):
    print "Intersection between %s and %s" % (c1.name, c2.name)
else:
    print "No intersection between %s and %s" % (c1.name, c2.name)
print "Expected: intersection"

c1 = Circle(6.5)
c1.set_center([0, 0])
c1.name = "Jupiter"

c2 = Circle(6.4)
c2.set_center([5, 12])
c2.name = "Earth"

if c1.intersection(c2):
    print "Intersection between %s and %s" % (c1.name, c2.name)
else:
    print "No intersection between %s and %s" % (c1.name, c2.name)
print "Expected: no intersection"
