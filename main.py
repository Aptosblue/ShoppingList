shopping_list = []

print('Welcome to your shopping list.')

def add_item():
    user_prompt = str(input('Type an item to add or type "Done" to return to main menu: '))
    while user_prompt != 'Done'.lower():
        shopping_list.append(user_prompt)
        print(f'You have added {user_prompt} to your shopping list')
        print(f'Your list now contains: ')
        for i in shopping_list:
            print(f'-{i.capitalize()}')
        user_prompt = str(input('Type an item to add or type "Done" to return to main menu: ')).lower()


def remove_item():
    print(shopping_list)
    item_choice = str(input('Which item would you like to remove?')).lower()
    for i in shopping_list:
        if i == item_choice.lower():
            shopping_list.remove(i)
            print(f'{i.capitalize()} has been removed from the shopping list')
        else:
            break

print("1. Add Item\n2. Remove Item\n3. View Shopping List\n4. Exit and write list to file")

user_selection = 0
while user_selection != 4:
    try:
        user_selection = int(input('Please select an option: '))
        if user_selection == 1:
            add_item()
        if user_selection == 2:
            remove_item()
        if user_selection == 3:
            for item in shopping_list:
                print(f'-{item}')
        if user_selection > 4:
            print('The option you selected simply does not exist')
        print("1. Add Item\n2. Remove Item\n3. View Shopping List\n4. Exit and write list to file")
    except ValueError:
        print('The selection you made was not a valid choice.')

try:
    with open('shoppinglist.text', 'w') as file:
        for item in shopping_list:
            file.write(item + '\n')

finally:
    file.close()