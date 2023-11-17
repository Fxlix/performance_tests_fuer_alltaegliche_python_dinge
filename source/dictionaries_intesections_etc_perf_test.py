import timeit
from collections import ChainMap

# Test-Dictionaries erstellen
dict_a = {f'key{i}': i for i in range(1000)}
dict_b = {f'key{i}': i if i % 2 == 0 else str(i + 1)+"-" for i in range(500, 1500)}

# Methode 1: Direkte Schleifen und Set-Operationen
def methode1(a, b):
    keys_a_not_in_b = list(set(a) - set(b))
    keys_b_not_in_a = list(set(b) - set(a))
    keys_in_both_same_value = [key for key in a if key in b and a[key] == b[key]]
    keys_in_both_diff_value = [key for key in a if key in b and a[key] != b[key]]
    return keys_a_not_in_b, keys_b_not_in_a, keys_in_both_same_value, keys_in_both_diff_value

# Methode 2: List Comprehensions mit `items()`
def methode2(a, b):
    keys_a_not_in_b = [key for key in a if key not in b]
    keys_b_not_in_a = [key for key in b if key not in a]
    keys_in_both_same_value = [key for key, val in a.items() if key in b and b[key] == val]
    keys_in_both_diff_value = [key for key, val in a.items() if key in b and b[key] != val]
    return keys_a_not_in_b, keys_b_not_in_a, keys_in_both_same_value, keys_in_both_diff_value

# Methode 3: Dictionary Comprehensions
def methode3(a, b):
    keys_a_not_in_b = {key: a[key] for key in a if key not in b}
    keys_b_not_in_a = {key: b[key] for key in b if key not in a}
    keys_in_both_same_value = {key: a[key] for key in a if key in b and a[key] == b[key]}
    keys_in_both_diff_value = {key: (a[key], b[key]) for key in a if key in b and a[key] != b[key]}
    return keys_a_not_in_b, keys_b_not_in_a, keys_in_both_same_value, keys_in_both_diff_value

# Methode 4: Verwendung von `filter()` und `lambda`
def methode4(a, b):
    keys_a_not_in_b = list(filter(lambda key: key not in b, a))
    keys_b_not_in_a = list(filter(lambda key: key not in a, b))
    keys_in_both_same_value = list(filter(lambda key: key in b and a[key] == b[key], a))
    keys_in_both_diff_value = list(filter(lambda key: key in b and a[key] != b[key], a))
    return keys_a_not_in_b, keys_b_not_in_a, keys_in_both_same_value, keys_in_both_diff_value

# Methode 5: Verwendung von ChainMap
def methode5(a, b):
    chain = ChainMap(a, b)
    keys_a_not_in_b = [key for key in a if key not in b]
    keys_b_not_in_a = [key for key in b if key not in a]
    keys_in_both_same_value = [key for key in chain if key in a and key in b and a[key] == b[key]]
    keys_in_both_diff_value = [key for key in chain if key in a and key in b and a[key] != b[key]]
    return keys_a_not_in_b, keys_b_not_in_a, keys_in_both_same_value, keys_in_both_diff_value


# Performance-Test
methoden = [methode1, methode2, methode3, methode4,methode5]
ergebnisse = {}
for methode in methoden:
    time = timeit.timeit(lambda: methode(dict_a, dict_b), number=100)
    ergebnisse[methode.__name__] = time
print(ergebnisse)
"""
ergebnisse

Result
Basierend auf diesen Ergebnissen würde ich empfehlen, die erste Methode zu verwenden, wenn die Performance entscheidend ist. Sie bietet eine gute Balance zwischen Lesbarkeit und Effizienz. ​
{'methode1': 0.03611454500014588,
 'methode2': 0.04018181700007517,
 'methode3': 0.03874704000008933,
 'methode4': 0.06407406100015578,
 'methode5': 0.0505}
"""
