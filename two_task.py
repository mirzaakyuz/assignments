# task1

sales = {

  "cost_value": 31.87,

  "sell_value": 45.00,

  "inventory": 1000

}  

print(f"the profit is", round(sales["inventory"] * (sales["sell_value"] - sales["cost_value"] )) )

# task2

amount = float(str(input("How much will you be paid for this employee: ")))

print( "$%0.2f" % amount)

