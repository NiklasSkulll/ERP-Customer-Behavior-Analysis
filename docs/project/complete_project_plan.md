# Bachelorarbeit finales Thema ausformuliert

WIE VIEL AUFTRÄGE PRO MONAT HAT JEDER KUNDE? WIE VIELE DAVON SIND VALIDE?

---

## 1. Titel der Bachelorarbeit

**Deutscher Titel:**
- Erkennung und Typisierung erklärbarer Kaufverhaltensveränderungen bei B2B-Großhandelskunden auf Basis von ERP-Zeitreihendaten

**Englischer Titel:**
- Detection and Typology of Explainable Purchase Behavior Changes in B2B Wholesale Customers Using ERP Time Series Data

---

## 2. Kurzbeschreibung des Themas

Die Bachelorarbeit untersucht, wie sich Kaufverhaltensveränderungen bei B2B-Großhandelskunden anhand von ERP-Auftragsdaten automatisch erkennen, typisieren und erklärbar beschreiben lassen.

Im Mittelpunkt steht nicht nur die Frage, dass sich das Verhalten eines Kunden verändert, sondern was sich verändert. Dazu werden aus ERP-Daten kundenbezogene Zeitreihen gebildet, etwa zu Umsatz, Bestellfrequenz, Sortimentsbreite, Rabattquote, Warengruppenmix und Deckungsbeitrag. Erkannte Veränderungen sollen anschließend in interpretierbare Veränderungstypen eingeordnet und durch Feature-Contribution-Analysen nachvollziehbar erklärt werden.

**Die Arbeit verbindet drei Beiträge:**
1. eine Taxonomie von Verhaltensveränderungstypen aus ERP-Zeitreihendaten.
2. ein automatisches Erkennungs- und Klassifikationssystem für diese Typen.
3. eine erklärbare Feature-Contribution-Analyse pro erkannter Veränderung.

Der Anwendungskontext ist der B2B-Großhandel. Der Fokus liegt auf Verhaltensveränderungen auf Einzelkundenebene, zeitlich, multivariat, typisiert und erklärbar.

---

## 3. Hintergrund und Problemstellung

Kundenverhalten im B2B-Großhandel lässt sich nicht direkt beobachten, hinterlässt jedoch Spuren in Bestelldaten. Jede Bestellung erzeugt Datenpunkte, aus denen sich aussagekräftige Kennzahlen ableiten lassen. Diese Kennzahlen beschreiben, wie ein Kunde einkauft, wie oft er bestellt, welche Warengruppen er nutzt, wie stark er rabattabhängig ist und wie profitabel er für das Unternehmen ist.

Unternehmen im Großhandel haben viele Geschäftskunden. Manche Kunden kaufen plötzlich weniger, andere kaufen andere Produkte, wieder andere fordern zunehmend höhere Rabatte. Solche Veränderungen fallen häufig erst spät auf. Die Arbeit setzt genau hier an: Sie entwickelt ein System, das Veränderungen im Kaufverhalten frühzeitig aus Bestelldaten erkennt, benennt und erklärt, damit der Vertrieb rechtzeitig reagieren kann.

Dabei ist wichtig, dass nicht ein einzelner Wert isoliert betrachtet wird. Der Kern der Arbeit besteht darin, mehrdimensionale Muster aus mehreren Kennzahlen gleichzeitig zu analysieren. Ein Kunde kann beispielsweise gleichzeitig seltener bestellen, weniger Warengruppen kaufen und eine höhere Rabattquote aufweisen. Genau solche kombinierten Veränderungen sollen erkannt, typisiert und nachvollziehbar beschrieben werden.

Das Thema grenzt sich klar von reiner Churn Prediction und statischer Kundensegmentierung ab. Es geht nicht darum, vorherzusagen, ob ein Kunde abwandert, sondern darum, signifikante Veränderungen im aktuellen oder vergangenen Kaufverhalten zu erkennen und verständlich einzuordnen.

---

## 4. Ziel der Arbeit

Ziel der Bachelorarbeit ist die Entwicklung und Evaluation eines methodischen Ansatzes zur Erkennung, Typisierung und erklärbaren Beschreibung von Kaufverhaltensveränderungen bei B2B-Großhandelskunden auf Basis von ERP-Zeitreihendaten.

Dazu sollen aus ERP-Auftragsdaten kundenbezogene Zeitreihen erstellt werden. Auf dieser Grundlage sollen relevante Veränderungen identifiziert und in interpretierbare Typen eingeordnet werden. Für jede erkannte Veränderung soll außerdem nachvollziehbar dargestellt werden, welche Kennzahlen sich besonders stark verändert haben.

**Die Arbeit verfolgt damit drei Ziele:**
1. _Konzeptioneller Beitrag:_
	- Entwicklung einer Taxonomie von Verhaltensveränderungstypen auf Basis von ERP-Merkmalen.
2. _Methodischer Beitrag:_
	- Automatische Erkennung und Klassifikation dieser Typen pro Kunde und Zeitfenster.
3. _Erklärbarkeits-Beitrag:_
	- Darstellung, welche Feature-Dimensionen zu einer erkannten Veränderung beitragen.

---

## 5. Zentrale Forschungsfrage und Unterfragen

**Zentrale Forschungsfrage:**
- Welche Typen signifikanter Kaufverhaltensveränderungen lassen sich bei B2B-Großhandelskunden anhand von ERP-Auftragsdaten automatisch erkennen, klassifizieren und erklärbar beschreiben?

**Unterfragen:**
1. Welche Dimensionen des Kaufverhaltens, beispielsweise Frequenz, Sortimentsbreite, Rabattniveau, Umsatz, Produktgruppenfokus und Deckungsbeitrag, zeigen in realen ERP-Daten relevante Veränderungsmuster?
2. Welche Kennzahlen aus den Bestelldaten beschreiben das Kaufverhalten eines Kunden am besten?
3. Welche Detektionsmethode, insbesondere Change Point Detection oder zeitfensterbasierter Profilvergleich, erkennt diese Veränderungen früher und mit geringerer Falschalarmrate?
4. Lassen sich erkannte Veränderungen in interpretierbare Typen einteilen, die für einen Vertriebskontext handlungsrelevant sind?
5. Welche Feature-Dimensionen tragen am stärksten zu einer erkannten Veränderung bei und wie lässt sich das erklärbar darstellen?

---

## 6. Abgrenzung des Themas

Die Arbeit ist klar auf die Erkennung, Typisierung und Erklärung von Kaufverhaltensveränderungen bei B2B-Großhandelskunden ausgerichtet.

**Nicht Gegenstand der Arbeit sind:**
- Churn-Vorhersage mit einem Label "churned / not churned" als Zielvariable,
- statische Kundensegmentierung,
- Vorhersage zukünftiger Veränderungen,
- kausale Analyse, warum sich Verhalten verändert,
- Echtzeit-Monitoring oder ein produktives System,
- produktive Systemintegration,
- tiefe kausale Analyse,
- Nutzerstudien mit Vertriebsmitarbeitenden,
- mehr als zwei Detektionsmethoden im Detail,
- mehr als fünf bis sieben Veränderungstypen in der Taxonomie.

Der Fokus liegt auf der Typisierung und Erklärbarkeit von Veränderungen. Die Detektion dient als methodisches Werkzeug. Der Vergleich zwischen Change Point Detection und Fensterprofilen ist ein Nebenaspekt.

Für die Daten ist außerdem zu beachten, dass zwischen Projektgeschäft und Sortiments- beziehungsweise Bedarfsgeschäft unterschieden werden muss. Ein Projekt liegt vor, wenn einem Auftrag ein Angebot zugrunde liegt und der Umsatz eine bestimmte Größe erreicht. Angebote entstehen bei Projekten, beim Bedarfsgeschäft mit geringerem Umsatz oder bei Kunden, die Verfügbarkeiten abfragen.

---

## 7. Datenbasis der Arbeit

### 7.1 Datenbasis und Tabellen

**Datenbasis:**
- _Arbeit basiert auf ERP-Auftragsdaten:_
	- Zeitraum sollte mindestens 24 Monate umfassen und pro Kunde auf Monats- oder Wochenbasis aggregiert werden.
- _Aus den Rohdaten werden Kundenprofile als Zeitreihen gebildet:_
	- Eine Zeile beschreibt dabei einen Kunden in einem bestimmten Monat mit allen berechneten Kennzahlen.

**Notwendige Tabellen:**

| **Tabelle / Quelle** | **Benötigte Felder**                                   | **Zweck**                                                                    |
| -------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Auftragskopf         | Kunden-ID, Bestelldatum, Gesamtumsatz, Deckungsbeitrag | Zeitreihe pro Kunde, Umsatz, Bestellfrequenz, Warenkorbwert, Deckungsbeitrag |
| Auftragspositionen   | Artikel-ID, Warengruppe, Menge, Einzelpreis, Rabatt    | Sortimentsbreite, Warengruppenmix, Rabattquote                               |
| Artikelstamm         | Artikel-ID, Warengruppe / Kategorie                    | Aggregation auf Warengruppenebene                                            |
| Kundenstammdaten     | Unternehmensgröße, Branche                             | Branche und Größe für Subgruppenanalysen                                     |

**Zusätzlich hilfreiche Tabellen und Daten:**

| **Tabelle / Quelle**       | **Zweck**                                                              |
| -------------------------- | ---------------------------------------------------------------------- |
| Reporting Excel-Tabelle    | Hilfreich für Auswertungen; liegt im Vertriebsordner unter "Reporting" |
| ERP-App "Preise verwalten" | Quelle für Rabattinformationen                                         |

### 7.2 Mindestanforderungen an die Daten

| **Mindestanforderung**                                | **Begründung**                                                   |
| ----------------------------------------------------- | ---------------------------------------------------------------- |
| Mindestens 300 aktive Kunden mit Transaktionshistorie | Sonst zu wenig Varianz in Veränderungstypen                      |
| Mindestens 24 Monate Daten pro Kunde                  | Sonst sind keine stabilen Zeitreihen erkennbar                   |
| Mindestens 4–6 Bestellungen pro Kunde und Jahr        | Zu seltene Käufer erzeugen keine aussagekräftigen Zeitreihen     |
| Vollständige Warengruppen-Zuordnung                   | Ohne Kategorisierung ist keine Sortimentsbreiten-Analyse möglich |

### 7.3 Auftragskopf

Der Auftragskopf enthält die Zusammenfassung einer Bestellung. Jede Zeile entspricht einer Bestellung.

| **Feld**            | **Bedeutung**                                                          | **Verwendung**                                     |
| ------------------- | ---------------------------------------------------------------------- | -------------------------------------------------- |
| **Kunden-ID**       | Eindeutige Nummer zur Identifikation eines Kunden                      | Zusammenführung aller Bestellungen eines Kunden    |
| **Bestelldatum**    | Datum des Auftragseingangs                                             | Aufbau von Zeitreihen durch Gruppierung nach Monat |
| **Gesamtumsatz**    | Gesamtbetrag der Bestellung nach Rabatten                              | Umsatz-Datenpunkt                                  |
| **Deckungsbeitrag** | Betrag nach Abzug direkter Kosten (Einkaufspreis der Waren) vom Umsatz | Bewertung der Profitabilität                       |

### 7.4 Auftragspositionen

Die Auftragspositionen enthalten die Detailansicht jeder Bestellung. Jede Zeile entspricht einem einzelnen Artikel innerhalb einer Bestellung.

| **Feld**    | **Bedeutung**                             | **Verwendung**                                         |
| ----------- | ----------------------------------------- | ------------------------------------------------------ |
| Bestell-ID  | Verbindung zum Auftragskopf               | Zuordnung einzelner Positionen zu Bestellungen         |
| Artikel-ID  | Eindeutige Nummer eines Artikels          | Verbindung zum Artikelstamm                            |
| Warengruppe | Produktkategorie eines Artikels           | Sortimentsbreite und Warengruppenmix                   |
| Menge       | Anzahl bestellter Einheiten               | Analyse von Mengenverschiebungen                       |
| Einzelpreis | Preis pro Einheit vor Rabatt              | Berechnung des Listenpreises und tatsächlichen Preises |
| Rabatt      | Prozentualer Nachlass auf den Listenpreis | Berechnung der Rabattquote                             |

### 7.5 Artikelstamm

Der Artikelstamm ist das Produktverzeichnis und dient als Nachschlagetabelle.

| **Feld**                | **Bedeutung**                                 | **Verwendung**                                |
| ----------------------- | --------------------------------------------- | --------------------------------------------- |
| Artikel-ID              | Eindeutige Nummer eines Artikels              | Verbindung mit den Auftragspositionen         |
| Artikelname             | Name des Artikels                             | Beschreibung des Produkts                     |
| Warengruppe / Kategorie | Zuordnung des Artikels zu einer Produktgruppe | Aggregation und Analyse auf Warengruppenebene |

Wenn die Warengruppe nicht direkt in der Positionstabelle gespeichert ist, wird die Positionstabelle über die Artikel-ID mit dem Artikelstamm verknüpft.

### 7.6 Kundenstammdaten

Kundenstammdaten enthalten Informationen zum Kunden unabhängig von seinen Bestellungen.

| **Feld**   | **Bedeutung**            | **Verwendung**             |
| ---------- | ------------------------ | -------------------------- |
| Kunden-ID  | Eindeutige Kundenkennung | Verbindung zu Bestelldaten |
| Kundenname | Name des Kunden          | Identifikation             |
| Branche    | Branche des Kunden       | Subgruppenanalyse          |
| Größe      | Größenklasse des Kunden  | Subgruppenanalyse          |
| PLZ        | Postleitzahl             | Kundenattribut             |

Branche und Größe sind nicht für die Kernerkennung von Verhaltensänderungen notwendig, können aber für Subgruppenanalysen genutzt werden. So kann beispielsweise untersucht werden, ob bestimmte Verhaltenstypen in bestimmten Branchen häufiger auftreten.

---

## 8. Relevante Kennzahlen und deren Berechnung

### 8.1 Monatlicher Umsatz

**Bedeutung:**
- Der monatliche Umsatz zeigt, wie viel Geld ein Kunde in einem bestimmten Zeitraum ausgibt.

**Berechnung:**
- Summe aller Gesamtumsätze pro Kunde und Monat.

**Benötigte Felder:**
- _Auftragskopf:_
	- `Kunden-ID`, `Bestelldatum`, `Gesamtumsatz`

**Relevanz:**
- Ein sinkender Umsatz ist oft ein erstes Signal, dass sich das Kaufverhalten verändert.

### 8.2 Bestellfrequenz

**Bedeutung:**
- Die Bestellfrequenz zeigt, wie oft ein Kunde pro Monat oder Quartal bestellt.

**Berechnung:**
- Anzahl der Bestellungen pro Kunde und Monat.

**Benötigte Felder:**
- _Auftragskopf:_
	- `Kunden-ID`, `Bestelldatum`

**Relevanz:**
- Eine sinkende Frequenz kann darauf hindeuten, dass der Kunde Teile seines Bedarfs zu einem Wettbewerber verlagert, aber noch nicht vollständig abgewandert ist.

### 8.3 Durchschnittlicher Warenkorbwert

**Bedeutung:**
- Der durchschnittliche Warenkorbwert zeigt, wie viel eine durchschnittliche Bestellung kostet.

**Berechnung:**
- Gesamtumsatz ÷ Anzahl Bestellungen.

**Benötigte Felder:**
- _Auftragskopf:_
	- `Gesamtumsatz`, `Bestellfrequenz`

**Relevanz:**
- Die Kennzahl unterscheidet zwischen Kunden, die seltener bestellen, und Kunden, die pro Bestellung weniger kaufen.

### 8.4 Sortimentsbreite

**Bedeutung:**
- Die Sortimentsbreite zeigt, aus wie vielen verschiedenen Produktkategorien ein Kunde kauft.

**Berechnung:**
- Anzahl unterschiedlicher Warengruppen pro Kunde und Monat.

**Benötigte Felder:**
- _Auftragspositionen:_
	- `Warengruppe`

**Relevanz:**
- Wenn ein Kunde das Sortiment stark einschränkt, kauft er möglicherweise bestimmte Warengruppen bei einem Wettbewerber.

### 8.5 Warengruppenmix

**Bedeutung:**
- Der Warengruppenmix zeigt, welche Produktkategorien ein Kunde kauft und wie sich deren Umsatzanteile verändern.

**Berechnung:**
- Umsatzanteil je Warengruppe pro Kunde und Monat.

**Benötigte Felder:**
- _Auftragspositionen:_
	- `Warengruppe`, `Einzelpreis`, `Menge`

**Relevanz:**
- Ein Wechsel der dominanten Warengruppen kann auf eine veränderte Geschäftsstrategie des Kunden hinweisen oder darauf, dass bestimmte Produktgruppen nicht mehr beim betrachteten Unternehmen gekauft werden.

### 8.6 Rabattquote

**Bedeutung:**
- Die Rabattquote zeigt, wie viel Prozent Rabatt ein Kunde im Durchschnitt auf seine Bestellungen erhält.

**Berechnung:**
- Gesamter Rabattbetrag ÷ gesamter Listenpreis aller Positionen.

**Benötigte Felder:**
- _Auftragspositionen:_
	- `Einzelpreis`, `Menge`, `Rabatt`

**Berechnung des tatsächlichen Preises:**
- Einzelpreis × Menge × (1 − Rabatt)

**Relevanz:**
- Eine steigende Rabattquote ist ein Frühwarnzeichen für Preisdruck und potenzielle Abwanderung.

Die Rabattquote sollte gewichtet berechnet werden, da ein Rabatt auf eine hochpreisige Position stärker ins Gewicht fällt als ein gleicher prozentualer Rabatt auf eine niedrigpreisige Position.

### 8.7 Deckungsbeitrag

**Bedeutung:**
- Der Deckungsbeitrag zeigt, was nach Abzug direkter Kosten vom Umsatz übrig bleibt.

**Berechnung:**
- Summe der Deckungsbeiträge pro Kunde und Monat.

**Benötigte Felder:**
- _Auftragskopf:_
	- `Deckungsbeitrag`

**Relevanz:**
- Umsatzrückgang ist nicht gleichbedeutend mit Ertragsverlust. Der Deckungsbeitrag zeigt, wie wertvoll ein Kunde wirtschaftlich ist.

### 8.8 DB-Quote

**Bedeutung:**
- Die DB-Quote zeigt den Deckungsbeitrag im Verhältnis zum Umsatz (in %).

**Berechnung:**
- Deckungsbeitrag ÷ Umsatz.

**Benötigte Felder:**
- _Auftragskopf:_
	- `Deckungsbeitrag`, `Gesamtumsatz`

**Relevanz:**
- Ein Kunde kann aus Umsatzsicht stabil wirken, aber durch höhere Rabatte oder veränderte Produktwahl deutlich weniger profitabel werden.

### 8.9 Mengenverschiebungen

**Bedeutung:**
- Mengenverschiebungen zeigen, ob ein Kunde weniger Einheiten kauft oder ob sich die gekauften Mengen zwischen Produkten verändern.

**Berechnung:**
- Analyse der bestellten Mengen pro Kunde, Artikel, Warengruppe und Zeitraum.

**Benötigte Felder:**
- _Auftragspositionen:_
	- `Menge`

**Relevanz:**
- Mengenverschiebungen können helfen zu unterscheiden, ob ein Kunde weniger kauft oder günstigere Artikel auswählt.

### 8.10 Branche und Größe

**Bedeutung:**
- Branche und Größe beschreiben den Kunden als Stammdatenattribute.

**Berechnung:**
- Keine Berechnung erforderlich; direkte Übernahme aus dem Kundenstamm.

**Benötigte Felder:**
- _Kundenstamm:_
	- `Branche`, `Größe`

**Relevanz:**
- Branche und Größe können für Subgruppenanalysen genutzt werden. Unterschiedliche Kundengruppen können unterschiedliche normale Bestellmuster aufweisen.

### 8.11 Fertiges Monatsprofil

Aus den verknüpften Tabellen entsteht pro Kunde und Monat eine Zeile als Kundenprofil.

| **Monat** | **Kunden-ID** | **Umsatz** | **Frequenz** | **Ø Warenkorb** | **DB-Quote** | **Sortimentsbreite** | **Rabattquote** |
| --------- | ------------- | ---------: | -----------: | --------------: | -----------: | -------------------: | --------------: |
| Jan 2024  | K001          |    2.050 € |            2 |         1.025 € |       25,9 % |                    2 |           3,1 % |
| Feb 2024  | K001          |    3.200 € |            3 |         1.067 € |       24,1 % |                    3 |           4,2 % |
| Mär 2024  | K001          |      800 € |            1 |           800 € |       18,0 % |                    1 |          11,5 % |

---

## 9. Methodisches Vorgehen

### 9.1 Datenvorbereitung

Zunächst werden Rohdaten aus dem ERP-System extrahiert und bereinigt. Die Einzeltransaktionen werden pro Kunde und Monat oder Woche aggregiert. Dadurch entstehen Zeitreihen pro Kunde.

**Die Datenvorbereitung umfasst:**
- Extraktion und Bereinigung der ERP-Daten
- Verknüpfung von Auftragskopf, Auftragspositionen und Artikelstamm
- Aggregation auf Monats- oder Wochenbasis
- Berechnung von Feature-Vektoren pro Kunde
- Plausibilitätsprüfung, wie viele Kunden die Mindestanforderungen erfüllen

**Berechnete Features sind insbesondere:**
- Umsatz
- Bestellfrequenz
- durchschnittlicher Warenkorbwert
- Sortimentsbreite
- Rabattquote
- Warengruppenmix
- Deckungsbeitrag
- DB-Quote

### 9.2 Vergleich alter und neuer Zeiträume

**Die Zeitreihe eines Kunden wird in zwei Fenster aufgeteilt:**
- _Referenzzeitraum:_ vorheriger Zeitraum, zum Beispiel Monate 1–6 (1. Jahreshälfte)
- _Beobachtungszeitraum:_ späterer Zeitraum, zum Beispiel Monate 7–12 (2. Jahreshälfte)

Für beide Fenster werden Durchschnittswerte der Kennzahlen berechnet. Anschließend wird analysiert, wie stark sich die Kennzahlen verändert haben.

**Beispielhafte Veränderungsanalyse:**

| **Kennzahl**     |     **Vorher** |   **Nachher** |  **Veränderung** |
| ---------------- | -------------: | ------------: | ---------------: |
| Umsatz           |        2.800 € |         900 € |            −68 % |
| Bestellfrequenz  |    3,2 / Monat |   1,1 / Monat |            −66 % |
| Sortimentsbreite | 4 Warengruppen | 1 Warengruppe |            −75 % |
| Rabattquote      |            5 % |          14 % | +9 Prozentpunkte |

### 9.3 Taxonomie-Entwicklung

Die Taxonomie wird durch die Sichtung auffälliger Kundenprofile entwickelt. Vorgesehen ist eine manuelle Analyse von 20–30 auffälligen Kundenprofilen. Auf dieser Grundlage werden fünf bis sieben Veränderungstypen mit klaren Kriterien definiert.

Die Taxonomie bildet einen eigenen konzeptionellen Beitrag der Arbeit.

### 9.4 Detektionsansätze

**Es werden zwei Detektionsansätze betrachtet:**
- _Ansatz 1 - Change Point Detection:_
	- Change Point Detection erkennt automatisch Zeitpunkte, an denen sich der Verlauf einer Zeitreihe statistisch signifikant verändert. Dies kann auf univariaten oder multivariaten Zeitreihen erfolgen.
	- Vorgesehene Methode:
		- PELT über die `ruptures`-Library
		- gegebenenfalls BOCPD
- _Ansatz 2 - Rollierende Fensterprofile:_
	- Bei diesem Ansatz werden rollierende Zeitfenster gebildet, zum Beispiel Drei-Monats-Fenster mit Ein-Monats-Shift. Zwischen den Fenstern werden Distanzmaße berechnet.
	- Mögliche Distanzmaße:
		- Cosine-Ähnlichkeit
		- Wasserstein-Distanz

**Ziel:**
- Erkennung signifikanter Veränderungen zwischen Referenz- und Beobachtungsprofilen.

### 9.5 Klassifikation in Veränderungstypen

**Erkannte Veränderungen werden anschließend typisiert. Dafür sind zwei Varianten vorgesehen:**
1. _Regelbasiert:_
	- Wenn ein Feature um mehr als eine definierte Schwelle steigt oder sinkt, wird ein bestimmter Typ zugewiesen.
2. _Leichtgewichtiges Clustering:_
	- Clustering auf dem Veränderungsvektor, also auf der Differenz zwischen dem Profil vor und nach einem Änderungspunkt.

### 9.6 Erklärbarkeit

Für jede erkannte Veränderung wird analysiert, welche Features besonders stark zur Veränderung beitragen.

**Vorgesehene Ansätze:**
- Differenzprofil
- Feature-Contribution-Analyse
- optional SHAP-Werte auf einem Surrogate Classifier, beispielsweise einem Random Forest auf Cluster-Labels

### 9.7 Tools und Libraries

| **Aufgabe**            | **Tool / Library**                            |
| ---------------------- | --------------------------------------------- |
| Datenvorbereitung      | `pandas`, `numpy`                             |
| Change Point Detection | `ruptures` mit PELT und BOCPD                 |
| Distanzmaße            | `scipy` für Wasserstein, `sklearn` für Cosine |
| Clustering             | `sklearn` mit KMeans oder DBSCAN              |
| Erklärbarkeit          | `shap`, manuelle Differenzprofile             |
| Visualisierung         | `matplotlib`, `seaborn`, `plotly`             |
| Notebooks              | Jupyter                                       |

---

## 10. Taxonomie der Verhaltensveränderungstypen

Eine Taxonomie ist eine geordnete Liste von Veränderungstypen. Wenn das System eine Änderung erkennt, soll es diese einem verständlichen Typ zuordnen können.

Die Typen müssen nicht vollständig trennscharf sein. Ein Kunde kann gleichzeitig einen Umsatzrückgang und eine Sortimentsverengung zeigen. In der Arbeit kann entweder mit Mischtypen gearbeitet oder ein dominanter Typ zugewiesen werden, sofern dies begründet wird.

### 10.1 Beispiele von Verhaltensveränderungstypen

**Typ 1 - Umsatzrückgang:**
- _Was verändert sich?_
	- Der Gesamtumsatz des Kunden sinkt deutlich und anhaltend.
- _Welche Parameter zeigen das?_
	- Der monatliche Umsatz sinkt um mehr als 30 % über mindestens drei Monate.
- _Warum ist das für den Vertrieb relevant?_
	- Der Umsatzrückgang hat direkten Ertragseinfluss. Der Vertrieb muss verstehen, ob es sich um einen vorübergehenden Effekt, beispielsweise Saisonalität, oder um eine echte Verlagerung handelt.
- _Beispiel:_
	- Ein Kunde kauft im ersten Halbjahr durchschnittlich 8.000 € pro Monat, im zweiten Halbjahr nur noch 3.000 € pro Monat.

**Typ 2 - Frequenzrückgang:**
- _Was verändert sich?_
	- Der Kunde bestellt seltener, auch wenn der Umsatz pro Bestellung möglicherweise stabil bleibt.
- _Welche Parameter zeigen das?_
	- Die Anzahl der Bestellungen pro Monat sinkt um mehr als 50 %.
- _Warum ist das für den Vertrieb relevant?_
	- Selteneres Bestellen deutet darauf hin, dass der Kunde einen Teil seines Bedarfs woanders deckt, aber noch nicht vollständig abgewandert ist. Es handelt sich um eine frühe Warnstufe.
- _Beispiel:_
	- Ein Kunde bestellte früher viermal pro Monat, jetzt nur noch ein- bis zweimal.

**Typ 3 - Sortimentsverengung:**
- _Was verändert sich?_
	- Der Kunde kauft deutlich weniger verschiedene Produktkategorien als früher.
- _Welche Parameter zeigen das?_
	- Die Anzahl aktiver Warengruppen sinkt um mehr als 50 % im Vergleich zum Referenzzeitraum.
- _Warum ist das für den Vertrieb relevant?_
	- Der Kunde kauft möglicherweise bestimmte Kategorien bei einem Wettbewerber, auch wenn er insgesamt noch Kunde bleibt.
- _Beispiel:_
	- Ein Kunde kaufte früher aus sechs Warengruppen, jetzt nur noch aus zwei.

**Typ 4 - Warengruppenwechsel:**
- _Was verändert sich?_
	- Die Zusammensetzung des Einkaufs verschiebt sich stark. Andere Kategorien werden dominant.
- _Welche Parameter zeigen das?_
	- Die führende Warengruppe, gemessen am Umsatzanteil, wechselt oder der Umsatzanteil einer Kategorie verändert sich um mehr als 40 Prozentpunkte.
- _Warum ist das für den Vertrieb relevant?_
	- Ein Warengruppenwechsel kann auf eine Veränderung im Geschäftsmodell des Kunden hindeuten oder darauf, dass er in bestimmten Bereichen andere Lieferanten nutzt.
- _Beispiel:_
	- Früher stammten 60 % des Umsatzes aus Chemie, jetzt 70 % aus Verpackung.

**Typ 5 - Steigende Rabattabhängigkeit:**
- _Was verändert sich?_
	- Der Kunde fordert oder erhält deutlich mehr Rabatt als zuvor.
- _Welche Parameter zeigen das?_
	- Die Rabattquote steigt dauerhaft um mehr als 5–8 Prozentpunkte.
- _Warum ist das für den Vertrieb relevant?_
	- Steigende Rabattabhängigkeit ist oft ein Zeichen, dass der Kunde Preisdruck von Wettbewerbern signalisiert. Es ist ein frühes Signal, das dem Vertrieb Handlungsspielraum gibt, bevor der Kunde abwandert.
- _Beispiel:_
	- Früher lag der Kunde bei durchschnittlich 4 % Rabatt, jetzt bei durchschnittlich 13 % Rabatt.

**Typ 6 - Margenverschlechterung:**
- _Was verändert sich?_
	- Der Umsatz bleibt stabil, aber der Deckungsbeitrag sinkt, weil der Kunde verstärkt Niedrigmargen-Produkte kauft oder mehr Rabatt fordert.
- _Welche Parameter zeigen das?_
	- Der Deckungsbeitrag sinkt um mehr als 25 % bei gleichbleibendem oder leicht sinkendem Umsatz.
- _Warum ist das für den Vertrieb relevant?_
	- Ein Kunde kann aus Umsatzsicht unauffällig wirken, aber wirtschaftlich immer weniger wertvoll werden. Das ist für das Vertriebscontrolling besonders interessant.
- _Beispiel:_
	- Der Umsatz sinkt von 10.000 € auf 9.000 €, also um 10 %. Der Deckungsbeitrag sinkt jedoch von 2.500 € auf 1.000 €, also um 60 %.

---

## 11. Erkennung von Verhaltensänderungen

Eine zentrale methodische Entscheidung der Arbeit ist die Festlegung, wann eine Veränderung tatsächlich als Verhaltensänderung gilt. Ohne klare Regeln würde jede kleine monatliche Schwankung als Veränderung gelten.

### 11.1 Mögliche Arten von Betrachtungskriterien

**Es werden drei Arten von Kriterien betrachtet:**
- _Relative Schwellenwerte:_
	- Eine Kennzahl gilt als auffällig, wenn sie sich um mehr als einen definierten Prozentsatz im Vergleich zum Referenzzeitraum verändert.
	- Beispiele:
		- Umsatz sinkt um mehr als 30 %
		- Bestellfrequenz halbiert sich
		- Rabattquote steigt um mehr als 5 Prozentpunkte
	- Vorteil:
		- Relative Schwellenwerte sind einfach zu verstehen und zu erklären.
	- Nachteil:
		- Der konkrete Schwellenwert kann willkürlich wirken, wenn er nicht begründet wird.
- _Anhaltende Veränderung über mehrere Monate:_
	- Eine einzelne auffällige Bestellung ist noch kein Muster. Eine Veränderung gilt erst dann als signifikant, wenn sie über mindestens zwei bis drei Monate anhält.
	- Beispiel:
		- Ein einmaliger Umsatzrückgang wegen Betriebsurlaub des Kunden ist kein Signal. Ein Umsatzrückgang über mehrere Monate hinweg deutet dagegen auf eine echte Veränderung hin.
	- Vorteil:
		- Zufällige Ausreißer werden herausgefiltert.
	- Nachteil:
		- Es wird ausreichend Datenhistorie benötigt.
- _Change Point Detection:_
	- Change Point Detection erkennt automatisch, an welchem Zeitpunkt sich der Verlauf einer Zeitreihe statistisch signifikant verändert hat. Dadurch muss ein Schwellenwert nicht ausschließlich manuell festgelegt werden.
	- Die Methode erkennt beispielsweise einen Zeitpunkt, ab dem eine Umsatzkurve eine neue Richtung einschlägt.
	- Vorteil:
		- Die Methode ist datengetrieben und methodisch sauberer als reine Schwellenwerte.

### 11.2 Begründung der Schwellenwerte

**Die Schwellenwerte müssen wissenschaftlich begründet werden. Mögliche Begründungen sind:**
- Orientierung an bestehender Literatur
- datengetriebene Ableitung aus der Verteilung monatlicher Schwankungen
- Robustheitsanalyse mit alternativen Schwellenwerten

Eine Robustheitsanalyse kann zeigen, ob sich Ergebnisse stark verändern, wenn statt eines bestimmten Schwellenwertes leicht abweichende Werte verwendet werden.

---

## 12. Erklärbarkeit der Ergebnisse

Die Erklärbarkeit ist ein zentraler Bestandteil der Arbeit. Für jede erkannte Veränderung soll nachvollziehbar beschrieben werden, welche Kennzahlen sich wie stark verändert haben.

### 12.1 Differenzprofil

Das Differenzprofil zeigt die Veränderung der Kennzahlen vor und nach einem Änderungspunkt oder zwischen zwei Zeitfenstern.

**Beispiel:**

| **Kennzahl**     |     **Vorher** |   **Nachher** |  **Veränderung** |
| ---------------- | -------------: | ------------: | ---------------: |
| Umsatz           |        2.800 € |         900 € |            −68 % |
| Bestellfrequenz  |    3,2 / Monat |   1,1 / Monat |            −66 % |
| Sortimentsbreite | 4 Warengruppen | 1 Warengruppe |            −75 % |
| Rabattquote      |            5 % |          14 % | +9 Prozentpunkte |

Dadurch wird sichtbar, welche Merkmale den größten Beitrag zur erkannten Veränderung leisten.

### 12.2 Feature-Contribution-Analyse

Die Feature-Contribution-Analyse beschreibt für jede erkannte Veränderung, welches Feature sich wie stark verändert hat. Dadurch kann eine erkannte Veränderung verständlich erklärt werden.

**Beispielhafte Erklärung:**
- Ein Kunde hat im ersten Halbjahr regelmäßig und breit eingekauft: dreimal pro Monat, aus vier Kategorien, mit wenig Rabattdruck. Im zweiten Halbjahr kauft er fast nur noch eine Warengruppe, nur noch einmal pro Monat, und fordert deutlich höhere Rabatte. Das beschreibt eine mehrdimensionale Verhaltensveränderung.

### 12.3 Optionaler SHAP-Ansatz

Optional kann ein Surrogate Classifier, beispielsweise ein Random Forest, auf Cluster-Labels trainiert werden. SHAP-Werte können anschließend als Feature-Importance genutzt werden.

Dieser Ansatz ist optional. Die manuelle Analyse über Differenzprofile ist bereits ein erklärbarer Ansatz.

---

## 13. Evaluation

Die Evaluation ist eine zentrale Herausforderung, da kein natürlicher Ground Truth vorhanden ist. Es gibt keine gelabelten Daten, die eindeutig angeben, ob eine Veränderung tatsächlich relevant war.

Daher ist eine mehrschichtige Evaluation vorgesehen.

### 13.1 Quantitative interne Evaluation

Für die quantitative Evaluation werden synthetisch Veränderungen in reale Zeitreihen injiziert. Anschließend wird gemessen, ob die Detektionsmethode diese Veränderungen erkennt.

**Mögliche Evaluationsmetriken:**
- Precision
- Recall
- precision-recall-artige Analyse

Dieser Ansatz ist der sauberste Workaround für fehlenden Ground Truth, erfordert aber eine eigene Implementierung und eine klare Begründung.

### 13.2 Qualitative externe Evaluation

Zusätzlich kann eine qualitative Validierung durchgeführt werden.

**Mögliche Ansätze:**
- Experten-Review
- Fallbeispielanalyse bekannter Kundenverläufe
- Analyse von 5–10 Kunden mit nachvollziehbarer Verhaltensänderung

Ziel ist zu prüfen, ob die erkannten Typen für den Vertrieb handlungsrelevant sind.

### 13.3 Optionale retrospektive Validierung

Optional kann eine rückblickende Validierung an Kunden erfolgen, die nachweislich abgewandert sind.

Historische Churn-Labels sind dafür hilfreich, aber nicht notwendig. Die Arbeit ist keine Churn Prediction, sondern nutzt solche Informationen lediglich optional zur retrospektiven Validierung.

---

## 14. Risiken und Gegenmaßnahmen

| **Risiko**                                                                       | **Wahrscheinlichkeit** | **Auswirkung**                          | **Gegenmaßnahme**                                                                                            |
| -------------------------------------------------------------------------------- | ---------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Kein Ground Truth für Evaluation                                                 | Hoch                   | Mittel                                  | Synthetische Injektion von Veränderungen als Testdaten                                                       |
| Datenverfügbarkeit                                                               | Hoch                   | Sehr hoch                               | ERP-Datenzugang vor Themenauswahl klären                                                                     |
| Daten zu dünn, beispielsweise zu wenige Kunden mit langer Historie               | Mittel                 | Mittel                                  | Mindestanforderungen definieren; Fallback auf aggregiertere Zeitreihen                                       |
| Datenqualität                                                                    | Mittel                 | Mittel                                  | Datenbeschaffung und -bereinigung früh beginnen                                                              |
| Typenbildung wird zu subjektiv oder nicht reproduzierbar                         | Mittel                 | Mittel                                  | Regelbasierte Definition der Typen vorab; alternativ Clustervalidierung                                      |
| Verwechslung mit Churn Prediction                                                | Niedrig                | Mittel                                  | In Einleitung und Related Work explizit abgrenzen                                                            |
| Scope-Creep durch CPD, Fenstervergleich, Taxonomie, Erklärbarkeit und Evaluation | Mittel                 | Mittel                                  | Klare Priorisierung: Taxonomie und Typisierung als Kern, Detektion als Werkzeug, Erklärbarkeit als Ergänzung |
| ERP-Datenschutz / DSGVO                                                          | Nicht beziffert        | Zeitaufwand und Abstimmungsbedarf       | Kundendaten anonymisieren und Abstimmung früh einplanen                                                      |
| Fehlende Warengruppen-Zuordnungen oder inkonsistente Artikelnummern              | Nicht beziffert        | Beeinträchtigung der Feature-Berechnung | Datenqualität prüfen und Bereinigung früh durchführen                                                        |
| Kein öffentlicher B2B-ERP-Datensatz mit vergleichbarer Tiefe                     | Hoch                   | Sehr hoch                               | Unternehmensanbindung und ERP-Datenzugang früh klären                                                        |

### 14.1 Abhängigkeiten

| **Abhängigkeit**                             | **Bewertung**                                                      |
| -------------------------------------------- | ------------------------------------------------------------------ |
| ERP-Datenzugang                              | Sehr hoch                                                          |
| Expertenfeedback für qualitative Validierung | Optional, erhöht aber die Qualität                                 |
| Labels / Ground Truth                        | Nicht notwendig, da Workaround über synthetische Injektion möglich |

### 14.2 Machbarkeit

Technisch ist das Thema für eine Bachelorarbeit machbar, wenn die erforderlichen Daten vorhanden sind. Die größten Hürden liegen in der Datenbeschaffung, Datenqualität und Evaluation ohne natürlichen Ground Truth.

---

## 15. Erwartete Gliederung der Bachelorarbeit

| **Kapitel**                                  | **Inhalt**                                                                                             |           **Umfang** |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------: |
| 1. Einleitung                                | Motivation, Problemstellung, Forschungsfragen, Abgrenzung                                              |           3–4 Seiten |
| 2. Grundlagen                                | Zeitreihenanalyse, Change Point Detection, Kaufverhaltensmerkmale im B2B-Großhandel                    |           5–6 Seiten |
| 3. Verwandte Arbeiten                        | Dynamische Segmentierung, CPD in Transaktionsdaten, Erklärbarkeit, klare Abgrenzung zur eigenen Arbeit |           4–5 Seiten |
| 4. Datenbasis und Feature Engineering        | ERP-Datenstruktur, Aggregation, Feature-Definitionen, Datenqualität                                    |           4–5 Seiten |
| 5. Taxonomie der Verhaltensveränderungstypen | Konzeptioneller Beitrag: Definition und Kriterien der Typen                                            |           4–5 Seiten |
| 6. Detektions- und Klassifikationsmethodik   | CPD vs. Fensterprofile, Schwellenwert-Tuning, Typenzuordnung                                           |           6–7 Seiten |
| 7. Erklärbarkeit                             | Differenzprofile, Feature-Contribution pro Typ, gegebenenfalls SHAP                                    |           3–4 Seiten |
| 8. Evaluation                                | Synthetische Injektion, Fallbeispiele, Qualitätsmetriken                                               |           4–5 Seiten |
| 9. Diskussion                                | Interpretation, Limitationen, Praxisrelevanz                                                           |           3–4 Seiten |
| 10. Fazit und Ausblick                       | Zusammenfassung, offene Fragen                                                                         |             2 Seiten |
| **Gesamt**                                   |                                                                                                        | **ca. 38–42 Seiten** |

---

## 16. Zusammenfassung des finalen Themas

Die Bachelorarbeit beschäftigt sich mit der Erkennung, Typisierung und erklärbaren Beschreibung von Kaufverhaltensveränderungen bei B2B-Großhandelskunden anhand von ERP-Zeitreihendaten.

Aus ERP-Auftragsdaten werden kundenbezogene Monats- oder Wochenprofile gebildet. Diese Profile enthalten Kennzahlen wie Umsatz, Bestellfrequenz, durchschnittlichen Warenkorbwert, Sortimentsbreite, Warengruppenmix, Rabattquote, Deckungsbeitrag und DB-Quote. Durch den Vergleich von Referenz- und Beobachtungszeiträumen sowie durch Change Point Detection sollen signifikante Veränderungen im Kaufverhalten erkannt werden.

Die erkannten Veränderungen werden in eine Taxonomie interpretierbarer Typen eingeordnet. Dazu gehören Umsatzrückgang, Frequenzrückgang, Sortimentsverengung, Warengruppenwechsel, steigende Rabattabhängigkeit und Margenverschlechterung. Für jede erkannte Veränderung wird zusätzlich erklärt, welche Kennzahlen sich besonders stark verändert haben.

Die Evaluation erfolgt mehrschichtig. Da kein natürlicher Ground Truth vorliegt, werden synthetisch injizierte Veränderungen für eine quantitative Evaluation genutzt. Ergänzend können Fallbeispielanalysen, Experten-Reviews oder retrospektive Validierungen an nachweislich abgewanderten Kunden eingesetzt werden.

Der wissenschaftliche Beitrag der Arbeit liegt in der Kombination aus Taxonomie, automatischer Erkennung und Erklärbarkeit im Kontext des B2B-Großhandels. Das Thema ist geeignet, wenn ausreichende ERP-Daten vorhanden sind.