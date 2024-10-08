"""This script asks the user for the number of coffee and muffins they are purchasing and displays a receipt"""

# set constants: prices and tax rate
coffee_price = 5
muffin_price = 4
bagel_price = 2
tea_price = 2
tax_rate = 0.06

print('***************************************\nMy Coffee and Muffin Shop')

# ask for numbers of coffees and muffins bought
coffee_count = int(input('Number of coffees bought?\n'))
muffin_count = int(input('Number of muffins bought?\n'))
bagel_count = int(input('Number of bagels bought?\n'))
tea_count = int(input('Number of teas bought?\n'))

print('***************************************\n')

# crunch numbers
coffee_total = coffee_price*coffee_count
muffin_total = muffin_price*muffin_count
bagel_total = bagel_price*bagel_count
tea_total = tea_price*tea_count
subtotal = coffee_total + muffin_total + bagel_total + tea_total
tax_total = subtotal * tax_rate
tax_total_string = str(tax_total)  # string form to be able to later print without leading 0 if necessary
total = subtotal + tax_total

print('***************************************\nMy Coffee and Muffin Shop Receipt')

# change message between plural and singular
if coffee_count == 1:
    print(f"{coffee_count} Coffee at ${coffee_price} each: $ {coffee_total:.2f}")
else:
    print(f"{coffee_count} Coffees at ${coffee_price} each: $ {coffee_total:.2f}")

# change message between plural and singular
if muffin_count == 1:
    print(f"{muffin_count} Muffin at ${muffin_price} each: $ {muffin_total:.2f}")
else:
    print(f"{muffin_count} Muffins at ${muffin_price} each: $ {muffin_total:.2f}")

# change message between plural and singular
if bagel_count == 1:
    print(f"{bagel_count} Bagel at ${bagel_price} each: $ {bagel_total:.2f}")
else:
    print(f"{bagel_count} Bagels at ${bagel_price} each: $ {bagel_total:.2f}")

# change message between plural and singular
if tea_count == 1:
    print(f"{tea_count} Tea at ${tea_price} each: $ {tea_total:.2f}")
else:
    print(f"{tea_count} Teas at ${tea_price} each: $ {tea_total:.2f}")

# print tax without leading zero if necessary
if 1 > tax_total > 0:
    print(f"{tax_rate*100}% tax: $ .{tax_total_string[2]}{tax_total_string[3]}")
else:
    print(f"{tax_rate*100}% tax: $ {tax_total:.2f}")

print(f"---------\nTotal: $ {total:.2f}\n***************************************")

print('Thank you')
