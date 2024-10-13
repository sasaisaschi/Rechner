from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout, QPushButton

# Define the payment amounts in a dictionary
payment_amounts = {
    'A': {
        'In den ersten drei Monaten': {
            'stationäre Einrichtung': {"mittellos": "194,00 €", "nicht mittellos": "200,00 €"},
            'andere Wohnform': {"mittellos": "208,00 €", "nicht mittellos": "298,00 €"}
        },
        'Im vierten bis sechsten Monat': {
            'stationäre Einrichtung': {"mittellos": "129,00 €", "nicht mittellos": "158,00 €"},
            'andere Wohnform': {"mittellos": "170,00 €", "nicht mittellos": "208,00 €"}
        },
        'Im siebten bis zwölften Monat': {
            'stationäre Einrichtung': {"mittellos": "124,00 €", "nicht mittellos": "140,00 €"},
            'andere Wohnform': {"mittellos": "151,00 €", "nicht mittellos": "192,00 €"}
        },
        'Im 13. bis 24. Monat': {
            'stationäre Einrichtung': {"mittellos": "87,00 €", "nicht mittellos": "91,00 €"},
            'andere Wohnform': {"mittellos": "122,00 €", "nicht mittellos": "158,00 €"}
        },
        'Ab dem 25. Monat': {
            'stationäre Einrichtung': {"mittellos": "62,00 €", "nicht mittellos": "78,00 €"},
            'andere Wohnform': {"mittellos": "105,00 €", "nicht mittellos": "130,00 €"}
        }
    },
    'B': {
        'In den ersten drei Monaten': {
            'stationäre Einrichtung': {"mittellos": "241,00 €", "nicht mittellos": "249,00 €"},
            'andere Wohnform': {"mittellos": "258,00 €", "nicht mittellos": "370,00 €"}
        },
        'Im vierten bis sechsten Monat': {
            'stationäre Einrichtung': {"mittellos": "158,00 €", "nicht mittellos": "196,00 €"},
            'andere Wohnform': {"mittellos": "211,00 €", "nicht mittellos": "258,00 €"}
        },
        'Im siebten bis zwölften Monat': {
            'stationäre Einrichtung': {"mittellos": "154,00 €", "nicht mittellos": "174,00 €"},
            'andere Wohnform': {"mittellos": "188,00 €", "nicht mittellos": "238,00 €"}
        },
        'Im 13. bis 24. Monat': {
            'stationäre Einrichtung': {"mittellos": "107,00 €", "nicht mittellos": "113,00 €"},
            'andere Wohnform': {"mittellos": "151,00 €", "nicht mittellos": "196,00 €"}
        },
        'Ab dem 25. Monat': {
            'stationäre Einrichtung': {"mittellos": "78,00 €", "nicht mittellos": "96,00 €"},
            'andere Wohnform': {"mittellos": "130,00 €", "nicht mittellos": "161,00 €"}
        }
    },
    'C': {
        'In den ersten drei Monaten': {
            'stationäre Einrichtung': {"mittellos": "317,00 €", "nicht mittellos": "327,00 €"},
            'andere Wohnform': {"mittellos": "339,00 €", "nicht mittellos": "486,00 €"}
        },
        'Im vierten bis sechsten Monat': {
            'stationäre Einrichtung': {"mittellos": "208,00 €", "nicht mittellos": "257,00 €"},
            'andere Wohnform': {"mittellos": "277,00 €", "nicht mittellos": "339,00 €"}
        },
        'Im siebten bis zwölften Monat': {
            'stationäre Einrichtung': {"mittellos": "202,00 €", "nicht mittellos": "229,00 €"},
            'andere Wohnform': {"mittellos": "246,00 €", "nicht mittellos": "312,00 €"}
        },
        'Im 13. bis 24. Monat': {
            'stationäre Einrichtung': {"mittellos": "141,00 €", "nicht mittellos": "149,00 €"},
            'andere Wohnform': {"mittellos": "198,00 €", "nicht mittellos": "257,00 €"}
        },
        'Ab dem 25. Monat': {
            'stationäre Einrichtung': {"mittellos": "102,00 €", "nicht mittellos": "127,00 €"},
            'andere Wohnform': {"mittellos": "171,00 €", "nicht mittellos": "211,00 €"}
        }
    }
}

def calculate():
    group = combo_group.currentText()
    duration = combo_duration.currentText()
    location = combo_location.currentText()
    wealth = combo_wealth.currentText()

    # Get the payment amount from the dictionary
    payment = payment_amounts[group][duration][location][wealth]
    label_result.setText(f"Vergütung: {payment}")

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

combo_group = QComboBox()
combo_group.addItems(['A', 'B', 'C'])
layout.addWidget(QLabel('Vergütungsgruppe:'))
layout.addWidget(combo_group)

combo_duration = QComboBox()
combo_duration.addItems(
    ['In den ersten drei Monaten', 'Im vierten bis sechsten Monat', 'Im siebten bis zwölften Monat',
     'Im 13. bis 24. Monat', 'Ab dem 25. Monat'])
layout.addWidget(QLabel('Dauer der Betreuung:'))
layout.addWidget(combo_duration)

combo_location = QComboBox()
combo_location.addItems(['stationäre Einrichtung', 'andere Wohnform'])
layout.addWidget(QLabel('Gewöhnlicher Aufenthaltsort:'))
layout.addWidget(combo_location)

combo_wealth = QComboBox()
combo_wealth.addItems(['mittellos', 'nicht mittellos'])
layout.addWidget(QLabel('Vermögensstatus:'))
layout.addWidget(combo_wealth)

button_calculate = QPushButton('Berechnen')
button_calculate.clicked.connect(calculate)
layout.addWidget(button_calculate)

label_result = QLabel('Vergütung: ')
layout.addWidget(label_result)

window.setLayout(layout)
window.show()

app.exec_()