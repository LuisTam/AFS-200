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
    print("Your Receipt")
    print("-------------------------------------------------------")
    new_price = (price - discount) 
    sales_tax = float(tax * new_price * qty)
    saved = (qty * discount)
    total= (qty * new_price + sales_tax)
    print(f"Items: {qty} {product_desc} @ ${new_price} each.")
    print(f"Sales tax: ${sales_tax:.2f}")
    print("Total amount due: ${:,.2f}".format(total))
    print (f"You saved ${saved:.2f} today.")
#Price Check to see if product need 25% off
elif price >= 39.99:
    discount = ( price / a * c )
    print("Your Receipt")
    print("-------------------------------------------------------")
    new_price = (price - discount) 
    sales_tax = float(tax * new_price * qty)
    saved = (qty * discount)
    total= (qty * new_price + sales_tax)
    print(f"Items: {qty} {product_desc} @ ${new_price} each.")
    print(f"Sales tax: ${sales_tax:.2f}")
    print("Total amount due: ${:,.2f}".format(total))
    print (f"You saved ${saved:.2f} today.")
#Product does not qualify for discount
else:
    print("Sorry not Discount :(")
    print("Your Receipt")
    print("-------------------------------------------------------")
    sales_tax = float(tax * price * qty)
    total= (qty * price + sales_tax)
    print(f"Items: {qty} {product_desc} @ ${price:.2f} each.")
    print(f"Sales tax: ${sales_tax:.2f}")
    print("Total amount due: ${:,.2f}".format(total))
    print ("You saved $0 today.")

