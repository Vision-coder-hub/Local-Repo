menu = {
    'Pizza':40,
    'Burger':25,
    'Coffee':15,
    'Cocktail':40,
    'Soup':35
}
#Greet
print("Welcome to My  Restaurant")
smiley = '\U0001F604'
print(smiley) 
print(" Pizza:40\n","Burger:25\n","Coffee:15\n","Cocktail:40\n","Soup:35") #print items in menu
user_total = 0
item_1 = input("What would you like to have: ") #ask user 
choice = (input("Do you wanna add any other in your order?(Y/N): ")) 
if choice == "Y":
    item_2 = (input("What else would you like to order: "))
    if item_1 and item_2 in menu:
        user_total += menu[item_1 + item_2]
        print(user_total)
    else:
        print("Sorry,we dont have this item") 
elif item_1 in menu:
    user_total += menu[item_1]
    print(user_total) 
'''if item_1 in menu:
    user_total += menu[item_1]
    print(f'Your Total will be {user_total}') 
else:
    print("Sorry,we don't have this item.\nTry anything else") '''

