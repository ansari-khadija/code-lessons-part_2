# F. Date and time widgets
'''
QCalendarWidget — displays a calendar.
QDateEdit — edits a date.
QTimeEdit — edits a time.
QDateTimeEdit — edits a date and time.'''


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QCalendarWidget, QDateEdit, QTimeEdit, QDateTimeEdit
)
from PyQt5.QtCore import QDate, QTime, QDateTime


class DateTimeDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Date and Time Widgets")
        self.setGeometry(200, 100, 450, 550)

        layout = QVBoxLayout()

        # 1. QCalendarWidget
        layout.addWidget(QLabel("1. QCalendarWidget"))

        calendar = QCalendarWidget()
        calendar.setSelectedDate(QDate.currentDate())
        calendar.selectionChanged.connect(
            lambda: self.calendar_label.setText(
                "Selected Date: "
                + calendar.selectedDate().toString("dd-MM-yyyy")
            )
        )
        layout.addWidget(calendar)

        self.calendar_label = QLabel(
            "Selected Date: "
            + calendar.selectedDate().toString("dd-MM-yyyy")
        )
        layout.addWidget(self.calendar_label)

        # 2. QDateEdit
        layout.addWidget(QLabel("2. QDateEdit"))

        date_edit = QDateEdit()
        date_edit.setDate(QDate.currentDate())
        date_edit.setCalendarPopup(True)
        date_edit.setDisplayFormat("dd-MM-yyyy")

        self.date_label = QLabel()
        date_edit.dateChanged.connect(
            lambda date: self.date_label.setText(
                "Date: " + date.toString("dd-MM-yyyy")
            )
        )
        self.date_label.setText(
            "Date: " + date_edit.date().toString("dd-MM-yyyy")
        )

        layout.addWidget(date_edit)
        layout.addWidget(self.date_label)

        # 3. QTimeEdit
        layout.addWidget(QLabel("3. QTimeEdit"))

        time_edit = QTimeEdit()
        time_edit.setTime(QTime.currentTime())
        time_edit.setDisplayFormat("HH:mm:ss")

        self.time_label = QLabel()
        time_edit.timeChanged.connect(
            lambda time: self.time_label.setText(
                "Time: " + time.toString("HH:mm:ss")
            )
        )
        self.time_label.setText(
            "Time: " + time_edit.time().toString("HH:mm:ss")
        )

        layout.addWidget(time_edit)
        layout.addWidget(self.time_label)

        # 4. QDateTimeEdit
        layout.addWidget(QLabel("4. QDateTimeEdit"))

        datetime_edit = QDateTimeEdit()
        datetime_edit.setDateTime(QDateTime.currentDateTime())
        datetime_edit.setCalendarPopup(True)
        datetime_edit.setDisplayFormat("dd-MM-yyyy HH:mm:ss")

        self.datetime_label = QLabel()
        datetime_edit.dateTimeChanged.connect(
            lambda dt: self.datetime_label.setText(
                "Date and Time: "
                + dt.toString("dd-MM-yyyy HH:mm:ss")
            )
        )
        self.datetime_label.setText(
            "Date and Time: "
            + datetime_edit.dateTime().toString(
                "dd-MM-yyyy HH:mm:ss"
            )
        )

        layout.addWidget(datetime_edit)
        layout.addWidget(self.datetime_label)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = DateTimeDemo()
window.show()
sys.exit(app.exec_())
