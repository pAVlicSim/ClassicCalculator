from decimal import Decimal

from PyQt5 import QtWidgets

import my_calculator


class MyWindow(QtWidgets.QWidget, my_calculator.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.display_str = []
        self.v_stack = [0]
        self.INPUT_d = 0
        self.action_mach = []

        self.pushButton_n0.clicked.connect(self.clicked_button0)
        self.pushButton_n1.clicked.connect(self.clicked_button1)
        self.pushButton_n2.clicked.connect(self.clicked_button2)
        self.pushButton_n3.clicked.connect(self.clicked_button3)
        self.pushButton_n4.clicked.connect(self.clicked_button4)
        self.pushButton_n5.clicked.connect(self.clicked_button5)
        self.pushButton_n6.clicked.connect(self.clicked_button6)
        self.pushButton_n7.clicked.connect(self.clicked_button7)
        self.pushButton_n8.clicked.connect(self.clicked_button8)
        self.pushButton_n9.clicked.connect(self.clicked_button9)
        self.pushButton_comma.clicked.connect(self.clicked_button_comma)
        self.pushButton_add.clicked.connect(self.clicked_add)
        # self.pushButton_result.clicked.connect(self.calculation_all)
        self.pushButton_clear.clicked.connect(self.clear_all)
        self.pushButton_subtract.clicked.connect(self.clicked_subtract)
        self.pushButton_multiply.clicked.connect(self.clicked_multiply)
        self.pushButton_divide.clicked.connect(self.clicked_divide)

    def clicked_button0(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '0'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '0'
            self.input_display(v)

    def clicked_button1(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '1'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '1'
            self.input_display(v)

    def clicked_button2(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '2'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '2'
            self.input_display(v)

    def clicked_button3(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '3'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '3'
            self.input_display(v)

    def clicked_button4(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '4'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '4'
            self.input_display(v)

    def clicked_button5(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '5'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '5'
            self.input_display(v)

    def clicked_button6(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '6'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '6'
            self.input_display(v)

    def clicked_button7(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '7'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '7'
            self.input_display(v)

    def clicked_button8(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '8'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '8'
            self.input_display(v)

    def clicked_button9(self):
        if Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]):
            self.INPUT_d = 0
            v = '9'
            self.input_display_1(v)
        else:
            self.INPUT_d = 0
            v = '9'
            self.input_display(v)

    def clicked_button_comma(self):
        v = '.'
        self.input_display(v)

    def clicked_action(self):
        result_action = None
        if len(self.action_mach) >= 2:
            if self.action_mach[-2] == '+':
                result_action = Decimal(self.v_stack[-1]) + Decimal(self.lcdNumber.value())
            elif self.action_mach[-2] == '-':
                result_action = Decimal(self.v_stack[-1]) - Decimal(self.lcdNumber.value())
            elif self.action_mach[-2] == '*':
                result_action = Decimal(self.v_stack[-1]) * Decimal(self.lcdNumber.value())
            elif self.action_mach[-2] == '/':
                result_action = Decimal(self.v_stack[-1]) / Decimal(self.lcdNumber.value())
            self.lcdNumber.display(str(result_action))
            self.v_stack.append(result_action)
        else:
            self.input_display_2(self.lcdNumber.value())
        print(self.v_stack)

    def clicked_add(self):
        self.action_mach.append('+')
        self.clicked_action()
        return self.action_mach

    def clicked_subtract(self):
        self.action_mach.append('-')
        self.clicked_action()
        return self.action_mach

    def clicked_multiply(self):
        self.action_mach.append('*')
        self.clicked_action()
        return self.action_mach

    def clicked_divide(self):
        self.action_mach.append("/")
        self.clicked_action()
        return self.action_mach

    # def calculation_all(self):
    #     result_action = None
    #     if self.action_mach == '+':
    #         result_action = Decimal(self.v_stack[-1]) + Decimal(self.lcdNumber.value())
    #     elif self.action_mach == '-':
    #         result_action = Decimal(self.v_stack[-1]) - Decimal(self.lcdNumber.value())
    #     elif self.action_mach == '*':
    #         result_action = Decimal(self.v_stack[-1]) * Decimal(self.lcdNumber.value())
    #     elif self.action_mach == '/':
    #         result_action = Decimal(self.v_stack[-1]) / Decimal(self.lcdNumber.value())
    #     self.lcdNumber.display(str(result_action))
    #     self.v_stack.append(result_action)

    def clear_all(self):
        self.v_stack.clear()
        self.display_str.clear()
        self.input_display('0')

    def input_display_2(self, v):
        self.v_stack.append(v)
        self.display_str.clear()
        self.lcdNumber.display('')

    def input_display_1(self, v):
        self.display_str.clear()
        self.display_str.append(v)
        self.lcdNumber.display('')
        self.lcdNumber.display(''.join(self.display_str))

    def input_display(self, v):
        if self.INPUT_d == 0:
            self.display_str.append(v)
            self.lcdNumber.display(''.join(self.display_str))
        elif Decimal(self.lcdNumber.value()) == Decimal(self.v_stack[-1]) & self.INPUT_d == 1:
            self.display_str.clear()
            self.display_str.append(v)
            self.lcdNumber.display('')
            self.lcdNumber.display(''.join(self.display_str))
        elif self.INPUT_d == 1:
            self.lcdNumber.display('0')

    def calculation_result(self):
        pass


if __name__ == "__main__":
    import sys  # импорт модуля

    app = QtWidgets.QApplication(sys.argv)  # создаём экземпляр QApplication
    window = MyWindow()  # Создаем экземпляр класса
    # window.setStyleSheet(open("data/taxi_salary_1.qss", "r").read())  # добавляем .qss
    # window.setAutoFillBackground(True)  # настраиваем заполнение
    desktop = QtWidgets.QApplication.desktop()  # экземпляр рабочего стола
    window.move(desktop.availableGeometry().center() - window.rect().center())  # помещаем окно программы в центр
    # window.setWindowIcon(ico)  # добавляем иконку
    window.show()  # Отображаем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
