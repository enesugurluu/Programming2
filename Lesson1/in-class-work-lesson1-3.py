product1_price= int(input("Enter product 1 price: "))
product2_price= int(input("Enter product 2 price: "))
product3_price= int(input("Enter product 3 price: "))
product4_price= int(input("Enter product 4 price: "))
product5_price= int(input("Enter product 5 price: "))
print("----------------------------------------------")

sum_products = product1_price + product2_price + product3_price + product4_price + product5_price

print("Product 1 Entry Price", product1_price)
print("Product 2 Entry Price", product2_price)
print("Product 3 Entry Price", product3_price)
print("Product 4 Entry Price", product4_price)
print("Product 5 Entry Price", product5_price)

print("----------------------------------------------")

print("Products total price without tax: ", sum_products)

tax_ratio = 20

product1_price_of_tax = product1_price * (tax_ratio/100)
product2_price_of_tax = product2_price * (tax_ratio/100)
product3_price_of_tax = product3_price * (tax_ratio/100)
product4_price_of_tax = product4_price * (tax_ratio/100)
product5_price_of_tax = product5_price * (tax_ratio/100)
print("----------------------------------------------")

print("Product 1 Price with Tax", product1_price + product1_price_of_tax)
print("Product 2 Price with Tax", product2_price + product2_price_of_tax)
print("Product 3 Price with Tax", product3_price + product3_price_of_tax)
print("Product 4 Price with Tax", product4_price + product4_price_of_tax)
print("Product 5 Price with Tax", product5_price + product5_price_of_tax)

print(f"Total tax count {product1_price_of_tax + product2_price_of_tax + product3_price_of_tax + product4_price_of_tax + product5_price_of_tax}")

