

print("Hello. What do you want?")
is_running = True
while is_running :
    user_choose = input("""
        a) I want to get acquainted with the assortment of the store 
        b) I want to shop in your store 
        c) I want to become your regular customer (registration)
        d) I want to autorisation
        e) I want to know who owns the store
        f) Call the manager
        g) I want to know who your regular customers are
        j) I want to leave your store
        
    I want : """)

    if user_choose == "a" :
        from shop.products import get_products
        

    elif user_choose == "b":
        print("Unfortunately, this feature is still under development. Choose something else.")

    elif user_choose == "c":
        print("Unfortunately, this feature is still under development. Choose something else.")

    elif user_choose == "d" :
        print("Unfortunately, this feature is still under development. Choose something else.")

    elif user_choose == "e" :
        from shop.owner import get_owner

    elif user_choose == "f" :
        from shop.owner import get_manager

    elif user_choose == "g":
        from shop.customers import get_customers

    elif user_choose == "j" :
        is_running = False
        print("Goodby")
    else :
        continue





#def main():
#    pass

#if __name__ = "__main__":
#     main()