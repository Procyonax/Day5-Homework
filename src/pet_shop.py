# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(total):
    return total["admin"]["total_cash"]

def add_or_remove_cash(retotal, addition):
     retotal["admin"]["total_cash"] += addition

def get_pets_sold(sold):
    return sold["admin"]["pets_sold"] 

def increase_pets_sold(sold, addition):
    sold["admin"]["pets_sold"] += addition 

def get_stock_count(count):
    return len(count["pets"]) 

def get_pets_by_breed(shop, breed):
    breed_search = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            breed_search.append(pet)
    return breed_search

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet
    else:
        return None

def remove_pet_by_name(shop, name):
    match = None
    for index in range(len(shop["pets"])):
        if shop["pets"][index]["name"] == name:
            match = index
    if match is not None:
        shop["pets"].pop(match)

def add_pet_to_stock(shop, newpet):
    shop["pets"].append(newpet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, newpet):
    customer["pets"].append(newpet)