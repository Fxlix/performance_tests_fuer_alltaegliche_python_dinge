import timeit
import collections
import itertools

# Erstellen von zwei Beispielwörterbüchern
dict1 = {f"key{i}": i for i in range(1000)}
dict2 = {f"key{i+1000}": i for i in range(1000)}

# Definieren der Funktionen für die verschiedenen Methoden
def merge_with_update():
    temp = dict1.copy()
    temp.update(dict2)
    return temp

def merge_with_unpacking():
    return {**dict1, **dict2}

def merge_with_chainmap():
    return collections.ChainMap({}, dict1, dict2)

def merge_with_itertools_chain():
    return dict(itertools.chain(dict1.items(), dict2.items()))

def merge_with_dict_comprehension():
    return {k: dict2[k] if k in dict2 else dict1[k] for k in set(dict1) | set(dict2)}

def merge_with_adding_values():
    result = {}
    for key in set(dict1) | set(dict2):
        result[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return result

# Messen der Laufzeit für jede Methode
methods = [merge_with_update, merge_with_unpacking, merge_with_chainmap,
           merge_with_itertools_chain, merge_with_dict_comprehension, 
           merge_with_adding_values]

for method in methods:
    time_taken = timeit.timeit(method, number=1000)
    print(f"{method.__name__}: {time_taken:.5f} Sekunden")
