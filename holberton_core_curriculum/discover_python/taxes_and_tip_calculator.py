'''
Daniel Alzugaray
'''

price = input("What is the price before tax? ") # get the price
tax_percent = input("What are the taxes? (in %) ") # get the tax percentage as an integer
tip_percent = input("What do you to tip? (in %) ") # get the tip percentage as an integer

# take the price, and apply the tax first (price with applied tax)
# after the tax is applied, the tip is calculated from the price including tax, not just original price
# the division by 100 twice results in a simplified formula: 10,000 = 100 * 100
print "The price you need to pay is:",price*(100+tax_percent)*(100+tip_percent)/10000
