# Fertilizer calculator

## Anwendungsfall:

Es wird davon ausgegangen, dass das Bedürfnis besteht die Pflanzen in einem Aquarium optimal mit Nährstoffen zu versorgen. Der Nutzer hat bereits grundlegende Erfahrungen mit dem düngen eines Aquariums und hat wahrscheinlich auch ein entsprechendes Düngesystem zuhause.

So ein Düngesystem könnte z.B. von der Fa. AQUA REBEL sein und aus folgenden Einzeldüngern bestehen:

- Mikro Basic Eisen
- Makro Basic Phosphat
- Makro Basic Nitrat

Auf den jeweiligen Flaschen stehen die Inhaltsstoffe und auch eine Dosierempfehlung. 

Als Beispiel AQUA REBEL Makro Basic Phosphat:

| 1 ml in 50 l |  |
| --- | --- |
| PO4 | 0,10 mg/l |
| K | 0,04 mg/l |

|  | CO2 Zufuhr 20mg | ohne CO2 |
| --- | --- | --- |
| starkes Licht | 1 ml/Tag | 1-2 ml/Woche |
| schwaches Licht | 0,5 ml/Tag | 1-2 ml/Woche |

Ähnliche Angaben sind auch bei den anderen Düngern vorhanden (in diesem Fall Eisen und Nitrat). Das Problem ist nun, dass z.B. Kalium (K) in allen 3 Düngern vorhanden ist und das bei der Düngeempfehlung nicht berücksichtigt oder ignoriert wird. Dem Hersteller ist das bewusst und löst das Problem indem er folgende Information mitgibt:

> Wasserwechsel von 25% bis 50% pro Woche sind ratsam, damit sich keine zu hohen Konzentrationen von Mikronährstoffen im Aquarienwasser ansammeln.
> 

Wenn man nun aber 4 Aquarien mit einem Gesamtvolumen von 450l hat möchte man nicht jede Woche die Zeit investieren an 4 Aquarien einen Wasserwechsel durchzuführen und ggf. auch noch jede Woche 200l Wasser aufbereiten… und nicht zuletzt handelt es sich dabei um eine massive Trinkwasserverschwendung.

## Die Lösung - Grundlegende Funktion:

Die Web-app soll dem Nutzer bei der Berechnung von Mengen unterstützen und Ihm Hochrechnungen zur Verfügung stellen.

Funktionen:

- Bereitstellung einer Datenbank mit allen relevanten Düngesystemen
- gemessene Wasserwerte bilden die Grundlage für weitere Berechnungen
- Beleuchtungsdauer und -intensität werden berücksichtigt
- CO2-Zugabe wird berücksichtigt
- Intervallwunsch wird berücksichtigt (täglich oder wöchentlich)
- ggf. können gemessene Wasserwerte und Düngermengen bei wiederholter Nutzung der app den tatsächlichen Bedarf berechnen
- individuelle Zielwerte können berücksichtigt werden
- Wasserwechselintervall wird berücksichtigt
- Pflanzendichte wird berücksichtigt

Letztendlich sieht der Nutzer in der app ein Formular. Es gibt Felder die ausgefüllt werden müssen, da sie zwingend notwendig sind um etwas zu berechnen. Es gibt aber auch Formularfelder die optional sind, bei denen Standardwerte genutzt werden wenn das Feld leer bleibt.

Der Nutzer kann einen account einrichten, was es ermöglicht, dass Messwerte und Düngemengen in einer Datenbank gespeichert werden können. Je öfter und länger die app genutzt wird, um so genauer werden die Düngeempfehlungen um so nahe wie möglich an die Zielwerte zu kommen. Des Weiteren hat ein account den Vorteil, dass der Nutzer nicht alle Eingaben immer wieder machen muss. Die Werte für Volumen des Aquariums, Düngesystem, CO2 Zugabe, Beleuchtungsdauer und Beleuchtungsintensität werden in das Formular automatisch eingetragen wenn der Nutzer einen account hat und diese Werte schon einmal angegeben hat. Nutzer sollen auch die Möglichkeit haben mehr als 1 Aquarium anzulegen. Dafür ist es notwendig, dass der Nutzer einen Namen/Bezeichnung für das jeweilige Aquarium angibt.

## Was soll der Nutzer eingeben können oder müssen:

- Volumen des Aquariums in Liter. Der Nutzer soll eine Zahl zwischen 10 und 1000 eingeben können.
- Düngesystem (Dropdown Liste mit den verschiedenen Herstellern wie z.B. AQUA REBEL)
- Wenn der Hersteller des Düngesystems ausgewählt wurde sollen alle aktuellen Dünger, die der Hersteller anbietet, mit Checkboxen angezeigt werden, so das der Nutzer die Möglichkeit hat die Dünger auszuwählen die ihm zur Verfügung stehen (z.B. von AQUA REBEL: Mikro Basic Eisen, Makro Basic Phosphat und Makro Basic Nitrat).
- CO2 Zugabe vorhanden, ja/nein als Checkbox. Soll später bei der Berechnung der Düngermengen die Empfohlene Menge halbieren wenn kein CO2 zugeführt wird.
- Beleuchtungsdauer in Stunden. Der Nutzer soll eine Zahl zwischen 6 und 10 eingeben können. Standardwert ist 8.
- Beleuchtungsintensität. Der Nutzer soll aus einer Dropdown Liste wählen können (schwach, mittel, stark). Standardwert ist mittel.
- Pflanzendichte im Aquarium (niedrig, mittel, hoch).
- Tagesdüngung oder wöchentliche Intervalldüngung. Auswahltyp: radio.
- Wasserwerte: Der Nutzer soll die Möglichkeit haben die Wasserwerte die er zuvor gemessen hat einzutragen. Die wichtigsten Messwerte sind: Nitrat (NO3), Phosphat (PO4), Eisen (Fe) und Kalium (K). Der Standardwert ist jeweils 0 wenn keine Angabe erfolgt.
- Wasserwechselintervall in Wochen und Wasserwechselvolumen in Prozent oder Liter.

## Stack:
### Frontend:

- JavaScript - React
- ggf. formik & yup

### Backend:

- Python
- Flask
- SQLAlchemy-2.x-ORM-Struktur und Alembic für Migrationen