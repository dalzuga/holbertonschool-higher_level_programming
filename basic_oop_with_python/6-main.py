from circle import Circle

c1 = Circle(4)
c1.set_center([0, 0])
c1.name = "Sun"

c2 = Circle(4)
c2.set_center([1, 1])
c2.name = "Earth"

print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
