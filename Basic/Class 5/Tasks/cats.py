amount_of_cats = int(input("How many cat's? "))

if amount_of_cats == 1:
    print(f"Alice has {amount_of_cats} cat.")
elif 1 < amount_of_cats < 20:
    print(f"Alice has {amount_of_cats} cats.")
elif amount_of_cats >= 20:
    print(f"Alice has a cat shelter.")
else:
    print("Alice have a dead cats.")