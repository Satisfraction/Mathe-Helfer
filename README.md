# Mathe-Helfer

Mathe Helfer ist eine interaktive Anwendung, die Kindern beim Mathe lernen hilft. Sie können verschiedene Matheaufgaben lösen und ihre Antworten überprüfen.

## Funktionen

- Generierung zufälliger Matheaufgaben (Addition, Subtraktion, Multiplikation, Division)
- Eingabe der Antwort und Überprüfung auf Richtigkeit
- Anzeige des aktuellen Punktestands

## Anforderungen

Um die Mathe Helfer-Anwendung auszuführen, müssen Sie die folgenden Abhängigkeiten installieren:

- Python 3
- PyQt5-Bibliothek

Sie können die PyQt5-Bibliothek mit dem folgenden Befehl über pip installieren:

'''
pip install pyqt5
'''

## Ausführung

Starten Sie die Anwendung `MatheHelfer.exe` oder führen Sie die Python-Datei aus.

Das Mathe Helfer-Fenster wird geöffnet, und Sie können mit dem Lösen von Matheaufgaben beginnen.

## Verwendung

1. Klicken Sie auf den "Neue Aufgabe" Button, um eine neue Matheaufgabe zu generieren.
2. Geben Sie Ihre Antwort in das Textfeld ein und drücken Sie die Eingabetaste oder klicken Sie auf den "Überprüfen" Button.
3. Die Anwendung gibt Ihnen eine Rückmeldung, ob Ihre Antwort richtig oder falsch ist.
4. Der Punktestand wird aktualisiert und angezeigt.

Viel Spaß beim Lernen und Üben von Mathe!

------------------------------------------------------------------------------------------

## Code-Beschreibung

Dieser Code importiert notwendige Module aus der PyQt5-Bibliothek und dem random-Modul. Es definiert zwei Klassen, `MathQuestion` und `MathHelpApp`.

Die `MathQuestion`-Klasse generiert zufällige Mathematikfragen mit zwei Zahlen und einem Operator (+, -, *, /). Sie berechnet die Antwort basierend auf dem Operator.

Die `MathHelpApp`-Klasse erbt von `QMainWindow` und erstellt eine GUI, die ein Frage-Label, eine Antwort-Eingabe, ein Antwort-Label, ein Score-Label und zwei Buttons enthält.

Der "Neue Aufgabe"-Button (`generate_question_button`) generiert eine neue zufällige Mathematikfrage mit der `MathQuestion`-Klasse und aktualisiert das Frage-Label.

Der "Überprüfen"-Button (`submit_button`) überprüft die Benutzereingabe gegen die richtige Antwort, die von der `MathQuestion`-Klasse generiert wird. Wenn die Antwort korrekt ist, aktualisiert er den Score, zeigt eine Nachricht im Antwort-Label an und aktualisiert das Score-Label. Wenn die Antwort falsch ist, zeigt er eine Nachricht im Antwort-Label an.

Dieses Programm hilft Benutzern, ihre mathematischen Fähigkeiten zu üben und behält ihren Score im Auge.
