from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QInputDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import random

OPERATORS = {
    1: '+',
    2: '-',
    3: '*',
    4: '/'
}

class MathQuestion:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.answer = self.get_answer()

    def get_answer(self):
        if self.operator=='+':
            return self.num1 + self.num2
        elif self.operator=='-':
            return self.num1 - self.num2
        elif self.operator=='*':
            return self.num1 * self.num2
        elif self.operator=='/':
            return self.num1 / self.num2

class MathHelpApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mathe Helfer')
        self.setGeometry(100, 100, 600, 400)

        # Set background color to light blue
        self.setStyleSheet('background-color: #E6F3FF;')

        # Create font for labels
        font = QFont('Arial', 12)

        # Create question label
        self.question_label = QLabel('', self)
        self.question_label.setGeometry(50, 50, 700, 30)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setFont(font)

        # Create "New Question" button
        self.generate_question_button = QPushButton('Neue Aufgabe', self)
        self.generate_question_button.setGeometry(50, 100, 200, 30)
        self.generate_question_button.clicked.connect(self.generate_question)
        self.generate_question_button.setFont(font)

        # Create "Set Number Range" button
        self.set_range_button = QPushButton('Nummernbereich festlegen', self)
        self.set_range_button.setGeometry(300, 100, 250, 30)
        self.set_range_button.clicked.connect(self.set_number_range)
        self.set_range_button.setFont(font)
        

        # Create answer input box
        self.answer_input = QLineEdit(self)
        self.answer_input.setGeometry(50, 150, 200, 30)
        self.answer_input.setFont(font)

        # Create "Check Answer" button
        self.submit_button = QPushButton('Überprüfen', self)
        self.submit_button.setGeometry(300, 150, 250, 30)
        self.submit_button.clicked.connect(self.check_answer)
        self.submit_button.setFont(font)

        # Connect returnPressed signal to clicked signal
        self.answer_input.returnPressed.connect(self.submit_button.click)

        # Create answer label
        self.answer_label = QLabel('', self)
        self.answer_label.setGeometry(50, 200, 700, 30)
        self.answer_label.setAlignment(Qt.AlignCenter)
        self.answer_label.setFont(font)

        # Create score label
        self.score_label = QLabel('Score: 0', self)
        self.score_label.setGeometry(50, 250, 200, 30)
        self.score_label.setFont(font)

        # Set score label color to green
        self.score_label.setStyleSheet('color: green;')

        # Set initial score value to 0
        self.score = 0
        self.number_range = (1, 10)

    def generate_question(self):
        num1 = random.randint(self.number_range[0], self.number_range[1])
        num2 = random.randint(self.number_range[0], self.number_range[1])
        operator = OPERATORS[random.randint(1,4)]
        self.question = MathQuestion(num1, num2, operator)
        self.question_label.setText(f"Was ist {self.question.num1} {self.question.operator} {self.question.num2}?")
        self.answer_label.setText('')

    def check_answer(self):
        user_answer=self.answer_input.text()
        try:
            user_answer=float(user_answer)
            if user_answer==self.question.answer:
                self.answer_label.setText('Richtig! Gut gemacht!')
                self.score+=1
                self.score_label.setText(f"Score: {self.score}")
            else:
                self.answer_label.setText('Falsch! Versuche es erneut.')
        except ValueError:
            self.answer_label.setText('Ungültige Eingabe. Bitte gib eine Zahl ein.')

    def set_number_range(self):
        """
        Allows the user to set the range of numbers for the random math questions.
        """
        # Prompt the user for input for the number range
        range_str, ok = QInputDialog.getText(self, 'Nummernbereich festlegen', 'Gib den Nummernbereich im Format "min-max" ein:')
        if ok:
            range_min, range_max = range_str.split('-')
            self.number_range = (int(range_min), int(range_max))



if __name__=='__main__':
    app=QApplication(sys.argv)
    math_app=MathHelpApp()
    math_app.show()
    sys.exit(app.exec_())
