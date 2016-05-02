from bicycle import Shop, Bike, Customer

billys = Shop("Billy's Bikes", {"Huffy": 3, "Giant":2, "Schwinn": 5, "Trek": 7, "Specialized": 2, "GT": 4})
print("Take a look at our inventory: ", billys.inventory)
print(billys.inventory)

prices = {"Huffy": 180, "Giant": 480, "Schwinn": 930, "Trek": 660, "Specialized": 960, "GT": 474}

print(prices)

huffy = Bike("Huffy", 17, 150.0)
huffy.price()
giant = Bike("Giant", 25, 400.0)
giant.price()
schwinn = Bike("Schwinn", 20, 775.0)
schwinn.price()
trek = Bike("Trek", 30, 550.0)
trek.price()
specialized = Bike("Specialized", 22, 800.0)
specialized.price()
gt = Bike("GT", 34, 395.0)
gt.price()

jp = Customer("JP", 200)   
jp.get_cust()
print(jp.name)
print(jp.budget)
jenna = Customer("Jenna", 500)
jenna.get_cust()
print(jenna.name)
print(jenna.budget)
jaimie = Customer("Jaimie", 1000)
jaimie.get_cust()
print(jaimie.name)
print(jaimie.budget)
print(schwinn.can_purchase(jp))
jp.purchase(huffy)
print(jp.budget)
