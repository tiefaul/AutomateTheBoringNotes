inventory = {'Arrow': 12, 'Gold Coin': 42, 'Rope': 1, 'Torch': 6, 'Dagger': 1}
 
def display_inventory(items):
    print('Inventory:')
    for i, v in items.items():
        print(v, i)
    total = sum(items.values())
    print('Total number of items: ' + str(total))

display_inventory(inventory)