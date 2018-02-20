foodCharge = float( input( "Please enterr the charge of the food: " ) )

tip = 0.18 * foodCharge

salesTax = 0.07 * foodCharge

total = foodCharge + tip + salesTax

print( "Food Charge: $" + format( foodCharge, ",.2f"), "Tip: $" + \
       format( tip, ",.2f"), "Sales Tax: $" + format( salesTax, ",.2f"), \
       "Total: $" + format( total, ",.2f"), sep = "\n" )
