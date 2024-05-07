import pandas as pd
from os import system
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIntValidator
import design


def convert_Ui():
    system('pyuic5 design.ui -o design.py')

convert_Ui()


class MyApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.ball = None
        self.grade = None
        self.unit = None
        
        self.btnConvert.setFlat(True)
        style = '''
QPushButton {
	background-color: #6384ff;
	color: #fff;
	border: none;
	min-width: 30px;
	border-radius: 5px;
}

QPushButton::flat {
	background-color: transparent;
	border: none;
	color: #000;
	border-radius: 5px;
}

QPushButton::disabled {
	background-color: #606060;
	color: #959595;
	border: none;
	border-radius: 10px;
}

QPushButton::hover {
	background-color: #718fff;
	border: 2px solid #718fff;
	border-radius: 10px;
}

QPushButton::pressed {
	background-color: #446cff;
	border: 1px solid #446cff;
	border-radius: 10px;
}

QPushButton::checked {
	background-color: #3761ff;
	border: 1px solid #3761ff;
	border-radius: 10px;
}
'''
        self.btnConvert.setStyleSheet(style)
        style = '''
QLineEdit {
    color: #ff0000;
    border-radius: 10px;
    border: 1px solid #ff0000;
}        
        '''
        self.leBall.setStyleSheet(style)
        style = '''
QLineEdit {
    color: #137000;
    border-radius: 10px;
    border: 1px solid #137000;
}        
        '''
        self.leGrade.setStyleSheet(style)

        self.leBall.setValidator(QIntValidator(0, 100, self))
        self.leGrade.setValidator(QIntValidator(0, 10, self))
        try:
            self.df = pd.read_excel('Баллы.xlsx', index_col=0, sheet_name='Баллы')
            self.statusBar.showMessage('Чтение из файла   © СШ №32 г.Бреста')         
        except:
            self.df = pd.DataFrame([
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1,1,1,1,1],
                [2,1,1,1,1,2,2,2,2,1,1,2],
                [3,2,2,2,1,2,3,3,3,2,2,3],
                [4,2,2,2,1,3,3,3,3,2,2,3],
                [5,2,2,2,1,3,3,3,3,2,2,3],
                [6,2,2,2,1,3,3,3,4,3,3,3],
                [7,3,3,2,2,3,3,3,4,3,3,4],
                [8,3,3,2,2,4,4,3,4,3,3,4],
                [9,3,3,2,2,4,4,3,4,3,3,4],
                [10,3,3,3,2,4,4,3,4,4,4,4],
                [11,3,3,3,2,4,4,4,4,4,4,4],
                [12,3,3,3,2,4,4,4,4,4,4,4],
                [13,3,3,3,2,4,4,4,4,4,4,5],
                [14,3,3,3,2,5,4,4,4,4,4,5],
                [15,4,4,3,2,5,4,4,4,4,4,5],
                [16,4,4,3,3,5,4,4,4,4,4,5],
                [17,4,4,3,3,5,4,4,4,4,4,5],
                [18,4,4,3,3,5,4,4,5,4,4,5],
                [19,4,4,4,3,5,4,4,5,4,4,5],
                [20,4,4,4,3,5,5,4,5,5,5,5],
                [21,4,4,4,3,5,5,5,5,5,5,5],
                [22,4,4,4,3,5,5,5,5,5,5,5],
                [23,4,4,4,3,5,5,5,5,5,5,6],
                [24,4,4,4,3,5,5,5,5,5,5,6],
                [25,4,4,4,4,5,5,5,5,5,5,6],
                [26,5,5,4,4,6,5,5,5,5,5,6],
                [27,5,5,4,4,6,5,5,6,5,5,6],
                [28,5,5,4,4,6,5,5,6,5,5,6],
                [29,5,5,5,4,6,5,5,6,5,5,6],
                [30,5,5,5,4,6,6,6,6,6,6,6],
                [31,5,5,5,4,6,6,6,6,6,6,6],
                [32,5,5,5,4,6,6,6,6,6,6,6],
                [33,6,6,5,5,6,6,6,6,6,6,7],
                [34,6,6,5,5,7,6,6,6,6,6,7],
                [35,6,6,5,5,7,6,6,6,6,6,7],
                [36,6,6,5,5,7,6,6,6,6,6,7],
                [37,6,6,5,5,7,6,6,7,6,6,7],
                [38,6,6,6,5,7,7,7,7,6,6,7],
                [39,6,6,6,5,7,7,7,7,6,6,7],
                [40,6,6,6,5,7,7,7,7,7,7,7],
                [41,6,6,6,5,7,7,7,7,7,7,7],
                [42,7,7,6,6,7,7,7,7,7,7,8],
                [43,7,7,6,6,7,7,7,7,7,7,8],
                [44,7,7,6,6,7,7,7,7,7,7,8],
                [45,7,7,6,6,7,7,7,7,7,7,8],
                [46,7,7,7,6,7,7,7,7,7,7,8],
                [47,7,7,7,7,7,7,7,8,7,7,8],
                [48,7,7,7,7,7,8,8,8,7,7,8],
                [49,7,7,7,7,8,8,8,8,7,7,8],
                [50,7,7,7,7,8,8,8,8,8,8,8],
                [51,7,7,7,8,8,8,8,8,8,8,8],
                [52,7,7,7,8,8,8,8,8,8,8,8],
                [53,7,7,7,8,8,8,8,8,8,8,8],
                [54,8,8,7,8,8,8,8,8,8,8,9],
                [55,8,8,8,8,8,8,8,8,8,8,9],
                [56,8,8,8,8,8,8,8,8,8,8,9],
                [57,8,8,8,8,8,8,8,9,8,8,9],
                [58,8,8,8,8,8,8,8,9,8,8,9],
                [59,8,8,8,8,8,9,8,9,8,8,9],
                [60,8,8,8,8,8,9,8,9,9,9,9],
                [61,8,8,8,8,8,9,8,9,9,9,9],
                [62,8,8,8,9,8,9,8,9,9,9,9],
                [63,8,8,8,9,8,9,8,9,9,9,9],
                [64,8,8,9,9,8,9,8,9,9,9,9],
                [65,8,8,9,9,9,9,8,9,9,9,9],
                [66,8,8,9,9,9,9,9,9,9,9,9],
                [67,8,8,9,9,9,9,9,9,9,9,9],
                [68,9,9,9,9,9,9,9,9,9,9,9],
                [69,9,9,9,9,9,9,9,9,9,9,9],
                [70,9,9,9,9,9,9,9,10,9,9,9],
                [71,9,9,9,9,9,9,9,10,9,9,9],
                [72,9,9,9,9,9,9,9,10,9,9,10],
                [73,9,9,9,9,9,9,9,10,9,9,10],
                [74,9,9,9,9,9,9,9,10,9,9,10],
                [75,9,9,9,9,9,9,9,10,10,10,10],
                [76,9,9,9,9,9,9,9,10,10,10,10],
                [77,9,9,10,9,9,9,9,10,10,10,10],
                [78,9,9,10,9,9,9,9,10,10,10,10],
                [79,9,9,10,10,9,10,9,10,10,10,10],
                [80,9,9,10,10,9,10,10,10,10,10,10],
                [81,9,9,10,10,9,10,10,10,10,10,10],
                [82,10,10,10,10,9,10,10,10,10,10,10],
                [83,10,10,10,10,9,10,10,10,10,10,10],
                [84,10,10,10,10,9,10,10,10,10,10,10],
                [85,10,10,10,10,10,10,10,10,10,10,10],
                [86,10,10,10,10,10,10,10,10,10,10,10],
                [87,10,10,10,10,10,10,10,10,10,10,10],
                [88,10,10,10,10,10,10,10,10,10,10,10],
                [89,10,10,10,10,10,10,10,10,10,10,10],
                [90,10,10,10,10,10,10,10,10,10,10,10],
                [91,10,10,10,10,10,10,10,10,10,10,10],
                [92,10,10,10,10,10,10,10,10,10,10,10],
                [93,10,10,10,10,10,10,10,10,10,10,10],
                [94,10,10,10,10,10,10,10,10,10,10,10],
                [95,10,10,10,10,10,10,10,10,10,10,10],
                [96,10,10,10,10,10,10,10,10,10,10,10],
                [97,10,10,10,10,10,10,10,10,10,10,10],
                [98,10,10,10,10,10,10,10,10,10,10,10],
                [99,10,10,10,10,10,10,10,10,10,10,10],
                [100,10,10,10,10,10,10,10,10,10,10,10]],
                columns = ['Балл','Белорусский язык','Русский язык','Математика',
                           'Физика','Химия','Биология','Иностранный язык','История Беларуси',
                           'Обществоведение','География','Всемирная история'])
            self.df.drop (self.df.columns [0], axis= 1 , inplace= True )
            self.df.index.rename('Балл', inplace= True )
            self.statusBar.showMessage('Версия данных: 2022   ©СШ №32 г.Бреста')
            
        self.cbUnit.addItems(self.df.columns.values.tolist())
        if self.cbUnit.count()>0:
            self.unit = self.cbUnit.itemText(0)
        

        self.leBall.textEdited.connect(self.do_clear)
        self.leBall.editingFinished.connect(self.do_convert)
        self.cbUnit.currentIndexChanged.connect(self.do_convert)
        self.btnConvert.clicked.connect(self.do_convert)

    def get_grade(self):
        try:
            if self.ball>=0 and self.ball<=100:
                self.grade = self.df.at[self.ball, self.unit]
                return self.grade
            else:
                self.grade = None
                return '-'
        except:
            self.grade = None
            return ''
                
    def do_clear(self):
        self.grade = None
        self.leGrade.clear()    
    
    def do_convert(self):
        self.unit = self.cbUnit.currentText()
        try:
            self.ball = int(self.leBall.text())
        except:
            self.ball = None
        self.leGrade.setText(str(self.get_grade()))

def main():
    app = QApplication([])  # Новый экземпляр QApplication
    window = MyApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == "__main__":
    main()
