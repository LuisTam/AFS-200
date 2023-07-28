#Item Decription
product_desc = input("Enter Product description:")

#Quantity as integer
qty = int(input(f"How many of item {product_desc} are being purchased? "))

#Original price as float number
price= float(input("What is the regular price? "))
a = 100
b = 15 
c = 25

#Formula to calculate tax
tax = 6.5 / a

#Price check to see if price needs a 15% off
if (price >= 19.99) and (price  <= 39.98):
    discount = ( price / a * b )
    saved = (qty * discount)

#Price Check to see if product need 25% off
elif price >= 39.99:
    discount = ( price / a * c )
    saved = (qty * discount)

#Product does not qualify for discount
else:
    discount = 0
    saved = 0

#finding new price of item after discount
new_price = (price - discount) 

#finds sales tax and sets it as a float number
sales_tax = float(tax * new_price * qty)

#finds grand total of purchase
total= (qty * new_price + sales_tax)

print("Your Receipt")
print("-------------------------------------------------------")

print(f"Items: {qty} {product_desc} @ ${new_price:,.2f} each.")
print(f"Sales tax: ${sales_tax:.2f}")
print("Total amount due: ${:,.2f}".format(total))
print (f"You saved ${saved:,.2f} today.")
