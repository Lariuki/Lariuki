# Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa binária. Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?
import math

result = math.log2(128)
print(result)

# Suponha que você duplique o tamanho da lista. Qual seria o número máximo de etapas agora?

result_dobro = math.log2(256)
print(result_dobro)

# Lista telefonica ficticia
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

# O tempo de execução de um algoritmo é medido por meio de seu crescimento e é expresso na notação Big O
# A eficiência de um algoritmo é medida principalmente pela sua complexidade de tempo e espaço, utilizando a notação Big O para descrever como essas medidas crescem com o tamanho da entrada.
import time

def sample_algorithm(n):
    # Exemplo de um algoritmo O(n)
    total = 0
    for i in range(n):
        total += i
    return total

# Medição de tempo
start_time = time.time()
sample_algorithm(1000000)
end_time = time.time()
print(f"Tempo de execução: {end_time - start_time} segundos")

# Medida do tempo usando a ferramentas de Profiling
from memory_profiler import profile

@profile
def sample_algorithm(n):
    # Exemplo de um algoritmo O(n)
    total = 0
    for i in range(n):
        total += i
    return total

sample_algorithm(1000000)