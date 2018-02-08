import pprint
inv={'rope':1,'tourch':6,'gold coin':42,'dagger':1,'arrow':12}

def display_inventory(inventory):
    print('inventory:')
    item_total=0

    for item in inventory.items():
        item_total=item_total+inventory[item]
        print(str(item))

display_inventory(inv)
