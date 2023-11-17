"""
    Verwendung von remove(): Entfernt das erste Vorkommen eines bestimmten Elements.
    List Comprehensions: Erzeugt eine neue Liste, die nur die gewünschten Elemente enthält.
    del-Statement: Entfernt Elemente an einem bestimmten Index oder in einem bestimmten Bereich.
    Verwendung von filter(): Erzeugt einen Iterator, der nur die Elemente enthält, die eine bestimmte Bedingung erfüllen.
    Einsatz von pop(): Entfernt ein Element an einem bestimmten Index.
Hier sind die Ergebnisse des Performance-Tests für verschiedene Methoden zum Entfernen von Elementen aus einer Liste in Python:

    Methode remove(): 0.0020 Sekunden
    List Comprehensions: 0.0075 Sekunden
    del-Statement: 0.00002 Sekunden
    Verwendung von filter(): 0.0105 Sekunden
    Einsatz von pop(): 0.00011 Sekunden

Analyse

    Das del-Statement ist die schnellste Methode, um ein Element an einem bestimmten Index zu entfernen. Es ist effizient, da es direkt auf den Index zugreift und das Element entfernt, ohne die Liste zu durchlaufen.
    pop() ist ebenfalls sehr schnell und ähnlich effizient wie del, mit dem zusätzlichen Vorteil, dass es das entfernte Element zurückgibt.
    remove() bietet eine gute Performance, wenn Sie ein bestimmtes Element entfernen müssen und dessen Index nicht kennen. Es ist jedoch langsamer als del und pop, da es die Liste durchsuchen muss, um das Element zu finden.
    List Comprehensions sind langsamer als die direkten Methoden, da sie eine neue Liste erstellen. Sie sind jedoch nützlich, wenn Sie mehrere Elemente basierend auf einer Bedingung entfernen möchten.
    filter() ist die langsamste Methode in diesem Test. Es ist nützlich für bedingte Filterungen, aber nicht so effizient wie die anderen Methoden für einfache Entfernungsaufgaben.

Basierend auf diesen Ergebnissen sind das del-Statement und pop() die effizientesten Methoden zum Entfernen von Elementen aus einer Liste, insbesondere wenn der Index des zu entfernenden Elements bekannt ist. Für das Entfernen von Elementen basierend auf ihrem Wert oder einer Bedingung sind remove(), List Comprehensions oder filter() geeignet, wobei remove() für einzelne Elemente und List Comprehensions oder filter() für bedingte Entfernungen bevorzugt werden sollten.
    
    
"""

# Funktionen zur Entfernung von Elementen aus einer Liste
import timeit
# Methode 1: Verwendung von remove()
def methode_remove(lst, element):
    try:
        lst.remove(element)
    except ValueError:
        pass

# Methode 2: List Comprehensions
def methode_list_comprehension(lst, element):
    return [x for x in lst if x != element]

# Methode 3: del-Statement
def methode_del(lst, index):
    del lst[index]

# Methode 4: Verwendung von filter()
def methode_filter(lst, element):
    return list(filter(lambda x: x != element, lst))

# Methode 5: Einsatz von pop()
def methode_pop(lst, index):
    lst.pop(index)

# Methode 9: Entfernen von Blöcken mit Slices
def methode_remove_slice(lst, start, end):
    del lst[start:end]

# Testdaten vorbereiten
test_liste = [i for i in range(1000)]  # Liste mit 1000 Elementen
zu_entfernendes_element = 500  # Ein Element in der Mitte der Liste
index_zum_entfernen = 500  # Index in der Mitte der Liste

# Performance-Tests
methoden = [methode_remove, methode_list_comprehension, methode_del, methode_filter, methode_pop]
ergebnisse_list_removal = {}
for methode in methoden:
    # Kopie der Testliste für jeden Test, um Seiteneffekte zu vermeiden
    kopierte_liste = test_liste.copy()
    time = timeit.timeit(lambda: methode(kopierte_liste, zu_entfernendes_element if methode != methode_del and methode != methode_pop else index_zum_entfernen), number=100)
    ergebnisse_list_removal[methode.__name__] = time

print(ergebnisse_list_removal)
