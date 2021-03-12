from time import time

# def somme(function):
#     def positive(a, b):
#         if a < b:
#             a, b = b, a
#             return function(a, b)
#         else:
#             return function(a, b)
#     return positive

# @somme
# def soustraction_positive(a, b):
#     return a - b

# print(soustraction_positive(4, 10))


# def display(function):
#     def intern(*args, **kwargs):
#         print(f'Entrées: {args}')
#         result = function(*args, **kwargs)
#         print(f'Sortie: {result}')

#     return intern

# @display
# def op(a, b):
#     return a + b 

# op(2, 5)

def checker(function):
    def intern(*args, **kwargs):
        value  = function(*args, **kwargs)
        if isinstance(value, (int, str)):
            raise Exception('Erreur')
        else:
            return value

    return intern

def double(number):
    return number * 2

# print(double(4.5))

def timer(function):
    def intern(*args, **kwargs):
        start = time()
        value = function(*args, **kwargs)
        end = time()
        overall = end - start
        print(f'La fonction a été exécuter en {overall}s')

    return intern

@timer
def greet(name):
    return f'Bonjour {name}'


greet(name = 'aristide')