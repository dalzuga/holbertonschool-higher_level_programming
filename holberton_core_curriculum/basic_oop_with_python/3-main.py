from circle import Circle

c = Circle(4)
c.set_center([0, 0])
c.set_color("Yellow")
c.name = "Sun"
print "Area of %s is %f" % (c.name, c.area())
