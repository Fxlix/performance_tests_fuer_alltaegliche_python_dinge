"""
    For-Schleife: Die grundlegende und am häufigsten verwendete Methode.
    While-Schleife: Eine Alternative zur For-Schleife, oft mit manueller Indexverwaltung.
    List Comprehensions: Eine kompakte und oft effiziente Methode für Listen.
    Verwendung von map(): Eine funktionale Programmiermethode, oft verwendet, um eine Funktion auf jedes Element anzuwenden.
    Verwendung von filter(): Ähnlich wie map(), aber zur Auswahl von Elementen basierend auf einer Bedingung.
    Dictionary Comprehensions: Eine Methode speziell für Dictionaries, ähnlich wie List Comprehensions.

Für jede dieser Methoden werde ich ein Skript erstellen, das misst, wie lange es dauert, eine vordefinierte Anzahl von Operationen durchzuführen. Wir werden sowohl das Iterieren über eine Liste als auch über ein Dictionary testen. Beginnen wir mit der Implementierung des Skripts.

Hier sind die Ergebnisse des Performance-Tests für verschiedene Methoden zum Iterieren über Listen und Dictionaries in Python:
Iterieren über Listen

    For-Schleife: 0.0015 Sekunden
    While-Schleife: 0.0062 Sekunden
    List Comprehensions: 0.0020 Sekunden
    Verwendung von map(): 0.0049 Sekunden
    Verwendung von filter(): 0.0086 Sekunden

Iterieren über Dictionaries

    For-Schleife: 0.0013 Sekunden
    Verwendung von map(): 0.0058 Sekunden
    Dictionary Comprehensions: 0.0059 Sekunden

Analyse

    Die For-Schleife ist sowohl für Listen als auch für Dictionaries die schnellste Methode. Sie ist einfach, direkt und effizient.
    Die While-Schleife ist langsamer als die For-Schleife, insbesondere wegen der manuellen Indexverwaltung und der zusätzlichen Abfrage der Länge.
    List Comprehensions sind eine effiziente Methode für Listen, besonders wenn zusätzliche Operationen oder Filterungen erforderlich sind.
    map() und filter() sind langsamer als direkte Schleifen. Sie sind nützlich für funktionale Programmieransätze, aber in Bezug auf die reine Performance sind sie nicht optimal.
    Dictionary Comprehensions sind ähnlich effizient wie map() für Dictionaries. Sie sind praktisch, wenn Sie Schlüssel-Wert-Paare auf Basis von Bedingungen transformieren oder filtern möchten.

Basierend auf diesen Ergebnissen sind For-Schleifen für das einfache Durchlaufen von Listen und Dictionaries die effizienteste Wahl. List Comprehensions und Dictionary Comprehensions bieten eine gute Balance zwischen Lesbarkeit und Performance, insbesondere wenn Sie komplexe Operationen ausführen oder Filter anwenden möchten. map() und filter() sind für funktionale Programmierstile geeignet, aber nicht die schnellsten Optionen für das reine Durchlaufen von Datenstrukturen.
"""
import timeit
from collections import ChainMap
# Funktionen zum Iterieren über eine Liste oder ein Dictionary

# Methode 1: For-Schleife
def methode_for(iterierbar):
    for elem in iterierbar:
        pass  # Einfache Operation, um die Schleife zu durchlaufen

# Methode 2: While-Schleife
def methode_while(iterierbar):
    length = len(iterierbar)
    i = 0
    while i < length:
        elem = iterierbar[i]
        i += 1

# Methode 3: List Comprehensions (nur für Listen)
def methode_list_comprehension(lst):
    [elem for elem in lst]

# Methode 4: Verwendung von map()
def methode_map(iterierbar):
    list(map(lambda x: x, iterierbar))

# Methode 5: Verwendung von filter()
def methode_filter(iterierbar):
    list(filter(lambda x: True, iterierbar))

# Methode 6: Dictionary Comprehensions (nur für Dictionaries)
def methode_dict_comprehension(dic):
    {k: v for k, v in dic.items()}

# Methode 7: Iterieren über eine ChainMap
def methode_chainmap(chain):
    for key in chain:
        pass

# Methode 8: Iterieren über eine deque
def methode_deque(iterierbar):
    d = deque(iterierbar)
    for elem in d:
        pass


# Testdaten vorbereiten
test_liste = [i for i in range(1000)]
test_dict = {str(i): i for i in range(1000)}
#chain_map_test = ChainMap(test_dict, {str(i+1000): i for i in range(1000)})
# Performance-Tests für Listen
methoden_listen = [methode_for, methode_while, methode_list_comprehension, methode_map, methode_filter]
ergebnisse_list_iteration = {}
for methode in methoden_listen:
    time = timeit.timeit(lambda: methode(test_liste), number=100)
    ergebnisse_list_iteration[methode.__name__] = time

# Performance-Tests für Dictionaries
methoden_dicts = [methode_for, methode_map, methode_dict_comprehension]
ergebnisse_dict_iteration = {}
for methode in methoden_dicts:
    time = timeit.timeit(lambda: methode(test_dict), number=100)
    ergebnisse_dict_iteration[methode.__name__] = time

print(ergebnisse_list_iteration, ergebnisse_dict_iteration)
