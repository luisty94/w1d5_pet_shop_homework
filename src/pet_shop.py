# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
    

#1

def get_total_cash(pet_shop):
    total_cash = pet_shop["admin"]["total_cash"]
    return(total_cash)

#2 , #3

def add_or_remove_cash(pet_shop, cash):
    money = pet_shop["admin"]["total_cash"]
    new_cash = money + cash
    pet_shop["admin"]["total_cash"] = new_cash
    return(new_cash)

#4

def get_pets_sold(pet_shop):
    pets_sold = pet_shop["admin"]["pets_sold"]
    return(pets_sold)

#5

def increase_pets_sold(pet_shop, pets):
    pets_in_shop = pet_shop["admin"]["pets_sold"]
    total_pets_sold = pets_in_shop + pets
    pet_shop["admin"]["pets_sold"] = total_pets_sold
    return(total_pets_sold)

#6

def get_stock_count(pet_shop):
    total_pets = len(pet_shop["pets"])
    return(total_pets)

#7, #8

def get_pets_by_breed(pet_shop, breed):
    breed_pet = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_pet.append(pet)
    return(breed_pet)

#9

def find_pet_by_name(pet_shop, pet_name):
    find_name = None
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            find_name = pet
    return(find_name)

#10

