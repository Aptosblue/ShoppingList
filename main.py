shopping_list = []

print('Welcome to your shopping list.')

def add_item():
    user_prompt = str(input('Type an item to add or type "Done" to return to main menu: '))
    while user_prompt != 'Done'.lower():
        shopping_list.append(user_prompt)
        print(f'You have added {user_prompt} to your shopping list')
        print(f'Your list now contains: ')
        for item in shopping_list:
            print(f'-{item.capitalize()}')
        user_prompt = str(input('Type an item to add or type "Done" to return to main menu: ')).lower()


def remove_item():
    print(shopping_list)
    item_choice = str(input('Which item would you like to remove?')).lower()
    for item in shopping_list:
        if item == item_choice.lower():
            shopping_list.remove(item)
            print(f'{item.capitalize()} has been removed from the shopping list')
        else:
            break

print("1. Add Item\n2. Remove Item\n3. View Shopping List.")
user_selection = int(input('Please select an option: '))

while user_selection != 4:
    if user_selection == 1:
        add_item()
    if user_selection == 2:
        remove_item()
    if user_selection == 3:
        for item in shopping_list:
            print(f'-{item}')
    print("1. Add Item\n2. Remove Item\n3. View Shopping List.")
    user_selection = int(input('Please select an option: '))

try:
    with open('shoppinglist.text', 'w') as s:
        for item in shopping_list:
            s.write(item + '\n')

finally:
    s.close()