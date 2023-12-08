def displayinv(inventory):
    print('Inventory:')
    for k, v in inventory.items():
        print(v, k)
    total = sum(inventory.values())
    print('Total number of items: ' + str(total))
    

def addinventory(inventory, addItems):
    for items in addItems:
        inventory.setdefault(items, 0)
        inventory[items] += 1

char_inv = {'gold coin': 42, 'rope': 1}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addinventory(char_inv, loot)
displayinv(char_inv)