# Profit and Loss Program

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit is:", profit)

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss is:", loss)

else:
    print("No Profit No Loss")