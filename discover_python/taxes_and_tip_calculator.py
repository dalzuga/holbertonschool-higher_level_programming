price = input("What is the price before tax? ")
tax_percent = input("What are the taxes? (in %) ")
tip_percent = input("What do you to tip? (in %) ")

print "The price you need to pay is:",price*(100+tax_percent)*(100+tip_percent)/10000
