import sys
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []


        self.sound = QSound('a.wav', self)
        self.a_1.clicked.connect(self.sound.play)
        self.sound = QSound('b.wav', self)
        self.b_1.clicked.connect(self.sound.play)
        self.sound = QSound('c.wav', self)
        self.c_1.clicked.connect(self.sound.play)
        self.sound = QSound('d.wav', self)
        self.d_1.clicked.connect(self.sound.play)
        self.sound = QSound('e.wav', self)
        self.e_1.clicked.connect(self.sound.play)
        self.sound = QSound('f.wav', self)
        self.f_1.clicked.connect(self.sound.play)
        self.sound = QSound('g.wav', self)
        self.g_1.clicked.connect(self.sound.play)
        self.sound = QSound('h.wav', self)
        self.h_1.clicked.connect(self.sound.play)
        self.sound = QSound('i.wav', self)
        self.i_1.clicked.connect(self.sound.play)
        self.sound = QSound('j.wav', self)
        self.j_1.clicked.connect(self.sound.play)
        self.sound = QSound('k.wav', self)
        self.k_1.clicked.connect(self.sound.play)
        self.sound = QSound('l.wav', self)
        self.l_1.clicked.connect(self.sound.play)
        self.sound = QSound('m.wav', self)
        self.m_1.clicked.connect(self.sound.play)
        self.sound = QSound('n.wav', self)
        self.n_1.clicked.connect(self.sound.play)
        self.sound = QSound('o.wav', self)
        self.o_1.clicked.connect(self.sound.play)
        self.sound = QSound('p.wav', self)
        self.p_1.clicked.connect(self.sound.play)
        self.sound = QSound('q.wav', self)
        self.q_1.clicked.connect(self.sound.play)
        self.sound = QSound('r.wav', self)
        self.r_1.clicked.connect(self.sound.play)
        self.sound = QSound('s.wav', self)
        self.s_1.clicked.connect(self.sound.play)
        self.sound = QSound('t.wav', self)
        self.t_1.clicked.connect(self.sound.play)
        self.sound = QSound('u.wav', self)
        self.u_1.clicked.connect(self.sound.play)
        self.sound = QSound('v.wav', self)
        self.v_1.clicked.connect(self.sound.play)
        self.sound = QSound('w.wav', self)
        self.w_1.clicked.connect(self.sound.play)
        self.sound = QSound('x.wav', self)
        self.x_1.clicked.connect(self.sound.play)
        self.sound = QSound('y.wav', self)
        self.y_1.clicked.connect(self.sound.play)
        self.sound = QSound('z.wav', self)
        self.z_1.clicked.connect(self.sound.play)


    def initUI(self):
        self.setGeometry(300, 300, 340, 400)
        self.setWindowTitle("Изучаем английский алфавит")
        self.setWindowIcon(QIcon('иконка.jpg'))
        self.setStyleSheet("background: rgb(43,255,155);")


        self.label = QLabel(self)
        self.label.setText('Hello my friend!')
        self.label.setStyleSheet("background: rgb(255,255,0);")
        self.label.resize(225, 70)
        self.label.move(50, 10)

        self.a_1 = QPushButton('A', self)
        self.a_1.setStyleSheet("background: rgb(254,155,0);")
        self.a_1.resize(50, 50)
        self.a_1.move(5, 100)

        self.b_1 = QPushButton('B', self)
        self.b_1.setStyleSheet("background: rgb(231,0,255);")
        self.b_1.resize(50, 50)
        self.b_1.move(65, 100)

        self.c_1 = QPushButton('C', self)
        self.c_1.setStyleSheet("background: rgb(231,0,255);")
        self.c_1.resize(50, 50)
        self.c_1.move(120, 100)

        self.d_1 = QPushButton('D', self)
        self.d_1.setStyleSheet("background: rgb(231,0,255);")
        self.d_1.resize(50, 50)
        self.d_1.move(175, 100)

        self.e_1 = QPushButton('E', self)
        self.e_1.setStyleSheet("background: rgb(254,155,0);")
        self.e_1.resize(50, 50)
        self.e_1.move(230, 100)

        self.f_1 = QPushButton('F', self)
        self.f_1.setStyleSheet("background: rgb(231,0,255);")
        self.f_1.resize(50, 50)
        self.f_1.move(285, 100)

        self.g_1 = QPushButton('G', self)
        self.g_1.setStyleSheet("background: rgb(231,0,255);")
        self.g_1.resize(50, 50)
        self.g_1.move(5, 155)

        self.h_1 = QPushButton('H', self)
        self.h_1.setStyleSheet("background: rgb(231,0,255);")
        self.h_1.resize(50, 50)
        self.h_1.move(65, 155)

        self.i_1 = QPushButton('I', self)
        self.i_1.setStyleSheet("background: rgb(254,155,0);")
        self.i_1.resize(50, 50)
        self.i_1.move(120, 155)

        self.j_1 = QPushButton('J', self)
        self.j_1.setStyleSheet("background: rgb(231,0,255);")
        self.j_1.resize(50, 50)
        self.j_1.move(175, 155)

        self.k_1 = QPushButton('K', self)
        self.k_1.setStyleSheet("background: rgb(231,0,255);")
        self.k_1.resize(50, 50)
        self.k_1.move(230, 155)

        self.l_1 = QPushButton('L', self)
        self.l_1.setStyleSheet("background: rgb(231,0,255);")
        self.l_1.resize(50, 50)
        self.l_1.move(285, 155)

        self.m_1 = QPushButton('M', self)
        self.m_1.setStyleSheet("background: rgb(231,0,255);")
        self.m_1.resize(50, 50)
        self.m_1.move(5, 210)

        self.n_1 = QPushButton('N', self)
        self.n_1.setStyleSheet("background: rgb(231,0,255);")
        self.n_1.resize(50, 50)
        self.n_1.move(65, 210)

        self.o_1 = QPushButton('O', self)
        self.o_1.setStyleSheet("background: rgb(254,155,0);")
        self.o_1.resize(50, 50)
        self.o_1.move(120, 210)

        self.p_1 = QPushButton('P', self)
        self.p_1.setStyleSheet("background: rgb(231,0,255);")
        self.p_1.resize(50, 50)
        self.p_1.move(175, 210)

        self.q_1 = QPushButton('Q', self)
        self.q_1.setStyleSheet("background: rgb(231,0,255);")
        self.q_1.resize(50, 50)
        self.q_1.move(230, 210)

        self.r_1 = QPushButton('R', self)
        self.r_1.setStyleSheet("background: rgb(231,0,255);")
        self.r_1.resize(50, 50)
        self.r_1.move(285, 210)

        self.s_1 = QPushButton('S', self)
        self.s_1.setStyleSheet("background: rgb(231,0,255);")
        self.s_1.resize(50, 50)
        self.s_1.move(5, 265)

        self.t_1 = QPushButton('T', self)
        self.t_1.setStyleSheet("background: rgb(231,0,255);")
        self.t_1.resize(50, 50)
        self.t_1.move(65, 265)

        self.u_1 = QPushButton('U', self)
        self.u_1.setStyleSheet("background: rgb(254,155,0);")
        self.u_1.resize(50, 50)
        self.u_1.move(120, 265)

        self.v_1 = QPushButton('V', self)
        self.v_1.setStyleSheet("background: rgb(231,0,255);")
        self.v_1.resize(50, 50)
        self.v_1.move(175, 265)

        self.w_1 = QPushButton('W', self)
        self.w_1.setStyleSheet("background: rgb(231,0,255);")
        self.w_1.resize(50, 50)
        self.w_1.move(230, 265)

        self.x_1 = QPushButton('X', self)
        self.x_1.setStyleSheet("background: rgb(231,0,255);")
        self.x_1.resize(50, 50)
        self.x_1.move(285, 265)

        self.y_1 = QPushButton('Y', self)
        self.y_1.setStyleSheet("background: rgb(254,155,0);")
        self.y_1.resize(100, 50)
        self.y_1.move(20, 320)

        self.z_1 = QPushButton('Z', self)
        self.z_1.setStyleSheet("background: rgb(231,0,255);")
        self.z_1.resize(100, 50)
        self.z_1.move(125, 320)

        self.Del = QPushButton('Выход', self)
        self.Del.setStyleSheet("background: rgb(255,0,91);")
        self.Del.clicked.connect(QCoreApplication.instance().quit)
        self.Del.resize(80, 50)
        self.Del.move(230, 320)

        self.a_1.clicked.connect(self.a)
        self.b_1.clicked.connect(self.b)
        self.c_1.clicked.connect(self.c)
        self.d_1.clicked.connect(self.d)
        self.e_1.clicked.connect(self.e)
        self.f_1.clicked.connect(self.f)
        self.g_1.clicked.connect(self.g)
        self.h_1.clicked.connect(self.h)
        self.i_1.clicked.connect(self.i)
        self.j_1.clicked.connect(self.j)
        self.k_1.clicked.connect(self.k)
        self.l_1.clicked.connect(self.l)
        self.m_1.clicked.connect(self.m)
        self.n_1.clicked.connect(self.n)
        self.o_1.clicked.connect(self.o)
        self.p_1.clicked.connect(self.p)
        self.q_1.clicked.connect(self.q)
        self.r_1.clicked.connect(self.r)
        self.s_1.clicked.connect(self.s)
        self.t_1.clicked.connect(self.t)
        self.u_1.clicked.connect(self.u)
        self.v_1.clicked.connect(self.v)
        self.w_1.clicked.connect(self.w)
        self.x_1.clicked.connect(self.x)
        self.y_1.clicked.connect(self.y)
        self.z_1.clicked.connect(self.z)


    def enterValue(self):
        if self.label.text() == 'Hello my friend!':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)


    def a(self):
        self.label.setText('')
        self.my_input = 'A a'
        self.enterValue()


    def b(self):
        self.label.setText('')
        self.my_input = 'B b'
        self.enterValue()

    def c(self):
        self.label.setText('')
        self.my_input = 'C c'
        self.enterValue()

    def d(self):
        self.label.setText('')
        self.my_input = 'D d'
        self.enterValue()

    def e(self):
        self.label.setText('')
        self.my_input = 'E e'
        self.enterValue()

    def f(self):
        self.label.setText('')
        self.my_input = 'F f'
        self.enterValue()

    def g(self):
        self.label.setText('')
        self.my_input = 'G g'
        self.enterValue()

    def h(self):
        self.label.setText('')
        self.my_input = 'H h'
        self.enterValue()

    def i(self):
        self.label.setText('')
        self.my_input = 'I i'
        self.enterValue()

    def j(self):
        self.label.setText('')
        self.my_input = 'J j'
        self.enterValue()

    def k(self):
        self.label.setText('')
        self.my_input = 'K k'
        self.enterValue()

    def l(self):
        self.label.setText('')
        self.my_input = 'L l'
        self.enterValue()

    def m(self):
        self.label.setText('')
        self.my_input = 'M m'
        self.enterValue()

    def n(self):
        self.label.setText('')
        self.my_input = 'N n'
        self.enterValue()

    def o(self):
        self.label.setText('')
        self.my_input = 'O o'
        self.enterValue()

    def p(self):
        self.label.setText('')
        self.my_input = 'P p'
        self.enterValue()

    def q(self):
        self.label.setText('')
        self.my_input = 'Q q'
        self.enterValue()

    def r(self):
        self.label.setText('')
        self.my_input = 'R r'
        self.enterValue()

    def s(self):
        self.label.setText('')
        self.my_input = 'S s'
        self.enterValue()

    def t(self):
        self.label.setText('')
        self.my_input = 'T t'
        self.enterValue()

    def u(self):
        self.label.setText('')
        self.my_input = 'U u'
        self.enterValue()

    def v(self):
        self.label.setText('')
        self.my_input = 'V v'
        self.enterValue()

    def w(self):
        self.label.setText('')
        self.my_input = 'W w'
        self.enterValue()

    def x(self):
        self.label.setText('')
        self.my_input = 'X x'
        self.enterValue()

    def y(self):
        self.label.setText('')
        self.my_input = 'Y y'
        self.enterValue()

    def z(self):
        self.label.setText('')
        self.my_input = 'Z z'
        self.enterValue()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())