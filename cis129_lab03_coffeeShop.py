"""This script asks the user for the number of coffee and muffins they are purchasing and displays a receipt"""

coffee_price = 5
muffin_price = 4
tax_rate = 0.06

print('***************************************\nMy Coffee and Muffin Shop')

coffee_count = int(input('Number of coffees bought?\n'))
muffin_count = int(input('Number of muffins bought?\n'))

print('***************************************\n')

coffee_total = coffee_price*coffee_count
muffin_total = muffin_price*muffin_count
subtotal = coffee_total + muffin_total
tax_total = subtotal * tax_rate
tax_total_string = str(tax_total)
total = subtotal + tax_total

print('***************************************\nMy Coffee and Muffin Shop Receipt')

if coffee_count == 1:
    print(f"{coffee_count} Coffee at ${coffee_price} each: $ {coffee_total:.2f}")
else:
    print(f"{coffee_count} Coffees at ${coffee_price} each: $ {coffee_total:.2f}")

if muffin_count == 1:
    print(f"{muffin_count} Muffin at ${muffin_price} each: $ {muffin_total:.2f}")
else:
    print(f"{muffin_count} Muffins at ${muffin_price} each: $ {muffin_total:.2f}")

if tax_total < 1 and tax_total > 0: 
    print(f"{tax_rate*100}% tax: $ .{tax_total_string[2]}{tax_total_string[3]}")
else:
    print(f"{tax_rate*100}% tax: $ {tax_total:.2f}")

print(f"---------\nTotal: $ {total:.2f}\n***************************************")
