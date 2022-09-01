#! python3
# by Victour Bue
# Fantasy Game Inventory - either display or add to a fantasy game inverntory

usrinv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def addToInventory(inv, loot):
    print("")
    for i in loot:
        inv.setdefault(i, 0)
        inv[i] += 1
        print(f"added {i}")
    print("All loot added!\n")
    return inv

def displayInventory(inv):
    print("\nInventory:")
    item_total = 0
    for k, v in inv.items():
        print(str(v) + ' ' + k)
        item_total += v
    print(f"Total number of items: {str(item_total)} \n")

def prompt():
    print("What would you like to do? [Display] inventory or [Add] loot?")
    cmd = input()
    if not cmd:
        return cmd
    if cmd.lower() == "display" or cmd.lower() == "add":
        return cmd
    else:
        print("That is not a valid input. Please type either 'display' or 'add'.")
        return prompt()

def main(usrinv):
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    cmd = prompt()
    if not cmd:
        return

    if cmd == "Display" or cmd == "display":
        displayInventory(usrinv)
    else:
        usrinv = addToInventory(usrinv, dragon_loot)
    
    return main(usrinv)


main(usrinv)