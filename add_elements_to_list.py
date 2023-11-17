from collections import deque
import timeit

"""
    Verwendung von append(): Zum Hinzufügen einzelner Elemente am Ende der Liste.
    Verwendung von extend(): Zum Hinzufügen mehrerer Elemente am Ende der Liste.
    List Comprehensions: Zum Erstellen einer neuen Liste durch das Hinzufügen von Elementen.
    += Operator: Zum Hinzufügen von Elementen oder Listen am Ende der vorhandenen Liste.
    collections.deque: Eine Alternative aus dem collections Modul, effizient für Operationen am Anfang der Liste.


Hier sind die Ergebnisse des Performance-Tests für verschiedene Methoden zum Hinzufügen von Elementen zu einer Liste in Python:

    Methode append(): 0.0074 Sekunden
    Methode extend(): 0.0009 Sekunden
    List Comprehensions: 0.0080 Sekunden
    += Operator: 0.0002 Sekunden
    collections.deque: 0.0020 Sekunden

Analyse

    Der += Operator ist die schnellste Methode, was ihn ideal für das Hinzufügen mehrerer Elemente zu einer Liste macht.
    extend() ist ebenfalls sehr schnell und effizient, besonders im Vergleich zu append(), wenn es darum geht, mehrere Elemente hinzuzufügen.
    collections.deque bietet eine gute Performance, insbesondere für Operationen am Anfang der Liste, aber in diesem Szenario, wo wir Elemente am Ende hinzufügen, ist es weniger effizient als += und extend().
    List Comprehensions sind langsamer als die anderen Methoden. Sie sind jedoch nützlich, wenn Sie eine neue Liste basierend auf der vorhandenen Liste erstellen möchten, insbesondere wenn Bedingungen oder Transformationen erforderlich sind.
    append() ist für das Hinzufügen einzelner Elemente geeignet, aber für das Hinzufügen einer großen Anzahl von Elementen nicht so effizient wie extend() oder +=.

Basierend auf diesen Ergebnissen sind für das schnelle Hinzufügen vieler Elemente zu einer Liste der += Operator und extend() die besten Optionen. deque aus dem collections Modul ist eine gute Alternative, wenn Sie häufig Elemente am Anfang der Liste hinzufügen oder entfernen müssen, da es in solchen Szenarien optimiert ist. 
"""



# Anzahl der Elemente zum Hinzufügen definieren
elemente_zum_hinzufuegen = [i for i in range(1000)]

# Methode 1: Verwendung von append()
def methode_append(lst, elemente):
    for elem in elemente:
        lst.append(elem)

# Methode 2: Verwendung von extend()
def methode_extend(lst, elemente):
    lst.extend(elemente)

# Methode 3: List Comprehensions
def methode_list_comprehension(lst, elemente):
    return [elem for elem in lst] + [elem for elem in elemente]

# Methode 4: += Operator
def methode_plus_equal(lst, elemente):
    lst += elemente

# Methode 5: collections.deque
def methode_deque(lst, elemente):
    d = deque(lst)
    d.extend(elemente)
    return list(d)

# Performance-Tests
methoden = [methode_append, methode_extend, methode_list_comprehension, methode_plus_equal, methode_deque]
ergebnisse_list_addition = {}
for methode in methoden:
    start_liste = [i for i in range(1000)]  # Startliste für jeden Test
    time = timeit.timeit(lambda: methode(start_liste, elemente_zum_hinzufuegen), number=100)
    ergebnisse_list_addition[methode.__name__] = time

print(ergebnisse_list_addition)
