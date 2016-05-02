class Shop(object):
    #inventory = {"Huffy": 3, "Giant":2, "Schwinn": 5, "Trek": 7, "Specialized": 2, "GT": 4}

    def __init__(self, shop_name, inventory):
        self.shop_name = shop_name
        self.inventory = inventory

class Bike(object):
    model_name = ""
    
    def __init__(self, model_name, weight, p_cost):
        self.model_name = model_name
        self.weight = weight
        self.p_cost = p_cost
        self.s_cost = p_cost * 1.2
   
    def price(self):
        print("A", self.model_name, "costs " + str(self.s_cost), "dollars.")

    #not sure how to get the model names and prices into dictionary
    def can_purchase(self, customer):
        if customer.budget > self.s_cost:
            return True
        return False

class Customer(object):
    name = ""

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    
    def get_cust(self):
        print(self.name, "has a budget of " + str(self.budget), "dollars.")

    def purchase(self, bike):
        self.budget = self.budget - bike.s_cost
