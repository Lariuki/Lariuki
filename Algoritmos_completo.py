phone_book = [
    {'name': 'Alice', 'phone': '123-456-7890'},
    {'name': 'Bob', 'phone': '987-654-3210'},
    {'name': 'Charlie', 'phone': '555-555-5555'}
]
print(phone_book)

# Pesquisa linear
def linear_search(phone_book, name):
    for entry in phone_book:
        if entry['name'] == name:
            return entry['phone']
    return None

name_to_find = 'Bob'
phone_number = linear_search(phone_book, name_to_find)
print(phone_number)

# Pesquisa binária
def binary_search(phone_book, name):
    low = 0
    high = len(phone_book) - 1

    while low <= high:
        mid = (low + high) // 2
        if phone_book[mid]['name'] < name:
            low = mid + 1
        elif phone_book[mid]['name'] > name:
            high = mid - 1
        else:
            return phone_book[mid]['phone']
    return None

name_to_find = 'Charlie'
phone_number = binary_search(phone_book, name_to_find)
print(phone_number)

# Pesquisa usando um dicionário 
def create_phone_dict(phone_book):
    phone_dict = {}
    for entry in phone_book:
        phone_dict[entry['name']] = entry['phone']
    return phone_dict

phone_dict = create_phone_dict(phone_book)
name_to_find = 'Alice'
phone_number = phone_dict.get(name_to_find)
print(phone_number)

# Exibindo todos os números de telefone 
def print_all_phone_numbers(phone_book):
    for entry in phone_book:
        print(f"{entry['name']}: {entry['phone']}")
        
print_all_phone_numbers(phone_book)
