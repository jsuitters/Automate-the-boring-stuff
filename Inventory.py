stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    for i in added_items:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1


print("ORIGINAL INVENTORY:")
display_inventory(stuff)

dragon_loot = ['gold coin', "dagger", 'gold coin', "gold coin", "ruby"]

add_to_inventory(stuff, dragon_loot)
print(" ")
print(" ")
print("UPDATED INVENTORY:")
display_inventory(stuff)
