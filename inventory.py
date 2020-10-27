# inventory.py
def addToInventory(inventory, addedItems):
    for loot_item in addedItems:
        if loot_item not in inventory.keys(): #if item not in dict
            inventory[loot_item] = 1 # add it to dict
        else:
            inventory[loot_item] += 1


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(k) + " : " + str(v))
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}  #my current inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)
displayInventory(inv)
