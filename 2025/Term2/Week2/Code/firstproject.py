def calculating_prices():
    #First I'm going to define prices as shown from example in assignment
    itemprice1 = 200.0 
    itemprice2 = 400.0
    itemprice3 = 600.0

    total = 0
    
    #Interactivity for fun
    print("Welcome to Bjorn's Python store!")
    print("I sell 3 items:")
    print("Item 1 = $200")
    print("Item 2 = $400")
    print("Item 3 = $600")
    print("")
    print("Type 1 to buy an item or 0 to skip it.")
    print("For example:")
    print(" - Enter 1 0 0 to buy only Item 1")
    print(" - Enter 1 1 0 to buy 1 and 2 (combo pack)")
    print(" - Enter 1 1 1 to buy all three items (gift pack)")
    print("")
    
    #adding input from user
    item1 = int(input("Buy Item 1? (1 = yes, 0 = no): "))
    item2 = int(input("Buy Item 2? (1 = yes, 0 = no): "))
    item3 = int(input("Buy Item 3? (1 = yes, 0 = no): "))
    
    #I want to add the prices if selected (1 = selected, 0 = not selected)
    if item1 == 1:
        total = total + itemprice1
    if item2 == 1:
        total = total + itemprice2 
    if item3 == 1:
        total = total + itemprice3
        
    #Counting how many items were purchased.
    count = item1 + item2 + item3 
    
    #apply discounts
    if count == 1:
        discount = 0
    elif count == 2:
        discount = .10
    elif count == 3:
        discount = .25
    else:
        discount = 0
        
    #add all items and include discounts (final total)
    final_total = total - (total * discount)
    
    print("")
    print("Items purchased:", count)
    print("Total before discount:", total)
    print("Discount applied:", discount * 100, "%")
    print("Final total after discount:", final_total)
    print("Thanks for shopping at Bjorn's Python store!")
    
calculating_prices()