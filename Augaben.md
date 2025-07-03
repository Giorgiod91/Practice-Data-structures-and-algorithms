from fpdf import FPDF

text = """
Python Lernplan - Woche 1 & 2

Woche 1 - Grundlagen festigen (Listen, Dictionaries, Schleifen, Bedingungen)

Tag 1 DONE !!

1. Zähle, wie viele Zahlen in der Liste [5, 12, 7, 20, 3] groesser als 10 sind.
2. Gib fuer jede Zahl in der Liste [1, 2, 3, 4, 5] aus, ob sie gerade oder ungerade ist.

Tag 2 DONE!!!

1. Berechne Summe und Durchschnitt der Zahlen [5, 10, 20, 8].
2. Finde das kleinste und groesste Element in der Liste [7, 3, 12, 9, 15] (ohne min()/max()).

Tag 3 DONE!!

1. Zaehle, wie oft jeder Buchstabe im String "hallo welt" vorkommt (Gross-/Kleinschreibung beachten).
2. Zaehle, wie oft jedes Wort im Satz "Hallo Welt hallo" vorkommt (Gross-/Kleinschreibung ignorieren).

Tag 4 DONE!!!

1. Finde das haeufigste Element in der Liste [1, 2, 2, 3, 1, 2].
2. Filtere aus der Liste [15, 22, 8, 10, 25] alle Zahlen, die groesser als 20 sind.

Tag 5 DONE!!

1. Schreibe eine Funktion, die fuer eine Liste Zahlen zurueckgibt, die groesser als der Durchschnitt sind.
2. Gib aus, wie viele Zahlen in der Liste [3, 5, 7, 9] ungerade sind.

Tag 6

1. Sortiere die Liste [4, 2, 5, 1, 3] manuell mit dem Bubble-Sort-Verfahren.
2. Schreibe eine Funktion, die prueft, ob eine Zahl gerade oder ungerade ist.

Tag 7

- Wiederhole zwei Aufgaben deiner Wahl von Tag 1 bis 6 – diesmal ohne Loesungen.

Woche 2 - Kombination & Problemloesung

Tag 8

1. Schreibe eine Funktion, die das groesste Element aus einer Liste zurueckgibt, ohne max() zu benutzen.
2. Schreibe eine Funktion, die das kleinste Element aus einer Liste zurueckgibt, ohne min() zu benutzen.

Tag 9

1. Schreibe eine Funktion, die eine Liste mit Bubble Sort sortiert.
2. Finde die drei groessten Zahlen aus der Liste [7, 2, 9, 1, 4, 8].

Tag 10

1. FizzBuzz: Fuer Zahlen von 1 bis 15 ausgeben: "Fizz" wenn durch 3 teilbar, "Buzz" wenn durch 5 teilbar, sonst Zahl.
2. Gib alle Zahlen aus der Liste [10, 15, 20, 25, 30] aus, die durch 5 teilbar sind.

Tag 11

1. Erstelle ein Dictionary, das Schuelernamen (z.B. "Anna", "Ben") und ihre Noten speichert. Berechne den Durchschnitt.
2. Gib alle Schueler aus, die besser als der Durchschnitt sind.

Tag 12

1. Finde in der Liste [5, 10, 15, 20, 25] die groesste Zahl ueber 15 und wie oft sie vorkommt.
2. Schreibe eine Funktion, die prueft, ob eine Liste leer ist.

Tag 13

- Debugging-Tag: Ich schicke dir 3 kleine fehlerhafte Codes, die du reparierst.

Tag 14

- Mini-Projekt: Temperaturdaten analysieren
  - Durchschnitt berechnen
  - Alle Temperaturen > 25 ausgeben
  - Hoechste Temperatur finden

Tipps fürs effiziente Lernen

- Mach nicht einfach alle Aufgaben hintereinander, sondern nimm dir Zeit zum Verstehen.
- Nach jeder Aufgabe: Lies die Loesung erst, wenn du wirklich feststeckst.
- Wenn du mehrere Aufgaben an einem Tag machst, versuche zwischendrin kurze Pausen einzulegen.
- Schreib Fehler und Aha-Momente auf, z. B. "Ich habe gelernt, wie man ein Dictionary benutzt, um Elemente zu zaehlen."
- Wiederhole regelmaessig, auch in den Folgetagen, Aufgaben aus der Vorwoche ohne Loesungshilfe.

Naechster Schritt nach 2 Wochen
Wenn du das geschafft hast, kann ich dir ein kleines Paket fuer den Einstieg bei LeetCode vorbereiten mit typischen "easy" Problems und Pattern-Erklaerungen.
"""
