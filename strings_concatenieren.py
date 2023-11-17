import random
import timeit
import string

def create_random_string(max_length):
    length = random.randint(1, max_length)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
# Test-Strings erstellen

test_strings = [create_random_string(1500) for _ in range(200)]

# Methode 1: Verwendung des + Operators
def methode1(strings):
    result = ""
    for s in strings:
        result += s
    return result

# Methode 2: Verwendung von str.join()
def methode2(strings):
    return "".join(strings)

# Methode 3: String Interpolation / f-Strings
def methode3(strings):
    return ''.join([f'{s}' for s in strings])

# Methode 4: String Formatting mit %
def methode4(strings):
    result = ""
    for s in strings:
        result = "%s%s" % (result, s)
    return result

# Methode 5: Verwendung von str.format()
def methode5(strings):
    result = ""
    for s in strings:
        result = "{}{}".format(result, s)
    return result

#Weitere Methoden
def methode2_realeres_setting(strings):
    return "".join([*strings])

def methode_belaemmert(strings):
     return "".join([''.join([s for s in st]) for st in strings])

# Performance-Test
methoden = [methode1, methode2, methode3, methode4, methode5,methode_belaemmert,methode2_realeres_setting]
ergebnisse_strings = {}
for methode in methoden:
    time = timeit.timeit(lambda: methode(test_strings), number=100)
    ergebnisse_strings[methode.__name__] = time

print(ergebnisse_strings)
print(methode2_realeres_setting(["käse","kuchen"]))
