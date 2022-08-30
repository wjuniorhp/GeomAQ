from cmath import sqrt
import matplotlib.pyplot as plt
import numpy as np
from GUI import *
from PyQt5.QtCore import QTimer
import os
os.system("color")

class MyWindow(Ui_MainWindow):
    # user actions
    def windowRun(self):
        # Definir a página inicial
        self.pages.setCurrentIndex(1)
        
        # Definindo ações dos botões do painel a esquerda
        self.buttonInfo.clicked.connect(lambda:
            self.pages.setCurrentIndex(0))
        self.buttonOpRetasRaizes.clicked.connect(lambda:
            self.pages.setCurrentIndex(1))
        self.buttonFx.clicked.connect(lambda:
            self.pages.setCurrentIndex(2))
        
        self.buttonGo.clicked.connect(self.clickedGo)
        
        self.buttonOxy.clicked.connect(self.clickedAnalisarOxy)
        self.buttonOpq.clicked.connect(self.clickedAnalisarOpq)
        
    def showTimedMsg(self,label,message):
        self.timer=QTimer()
        label.setText(message)
        self.timer.start(3000)
        self.timer.timeout.connect(lambda: label.setText(""))
        
    def clickedGo(self):
        self.showTimedMsg(self.infoResult,"You pressed the button")
        
        p = np.arange(self.pMin.value(), self.pMax.value(), 1e-2)
        print(self.tabX.currentIndex())
        
        if (self.tabX.currentIndex() == 1):
            xs = np.arange(self.xMin.value(), self.xMax.value(), self.xStep.value())
        elif (self.tabX.currentIndex() == 0):
            xs = np.array([self.xSingleValue.value()])
            
        retas_raiz(p,xs)

    def clickedAnalisarOpq(self):
        self.clickedAnalisarOxy(opq = True)

    def clickedAnalisarOxy(self, opq = False):
        p = self.pValue.value()
        q = self.qValue.value()
        if opq: a = self.aValue.value()
        
        xv = -p/2
        
        text = (f"Polinômio : y(x) = x² + {p}x + {q}\n"
                f"x do vértice = {xv}\n")
        
        if opq:
            area = checkArea(a,p,q)
            text += f"\nÁrea: {area}"
            if (self.checkShowGraph.isChecked()):
                ax = retas_raiz(xs = np.array([a]), show=False)
                ax.plot(p, q,'ko')
                plt.show()
        else:
            if(self.checkShowGraph.isChecked()): plot_trinomio(p,q)
        
        if (self.checkShowRaizes.isChecked()):
            text += checkRoots(p,q)
        
        self.InfoLabel.setText(text)
        print(text)
        return
    
def checkArea(a,p,q):
    area = "Undefined"
    
    ya = y(a,p,q)
    delta = discriminante(p,q)
    xv = -p/2
    x1,x2 = "",""
    aI = "a"
    
    if (ya>0 and delta>0 and xv>a):
        area = (f"A\n"
                f"As duas raízes são maiores que {aI}\n")
    elif (ya>0 and delta>0 and xv<a):
        area = (f"B\n"
                f"As duas raízes são menores que {aI}\n")
    elif (ya<0 and delta>0):
        area = (f"C\n"
                f"Uma das raízes é maior que {aI} e a outra é menor\n")
    elif (ya!=0 and delta==0):
        area = (f"Na parábola discriminante\n"
                f"A raiz é igual a {aI}\n")
    elif (ya==0 and delta!=0):
        area = (f"Na reta raiz\n"
                f"Uma das raízes é igual a {aI}\n")
    elif (ya==0 and delta==0):
        area = (f"Na interseção da parábola discriminante com a reta raiz - Ponto (-2a,a²)\n"
                f"A raiz é igual a {aI}\n")
    
    return area

def checkRoots(p,q):
    delta = discriminante(p,q)
    rootsText = ""
    
    if delta>0:
        x1 = (-p - sqrt(delta))/2
        x2 = (-p + sqrt(delta))/2
        rootsText = f"Possui 2 raízes reais: {x1:.2f} e {x2:.2f}"
    elif delta==0:
        x1 = -p/2
        rootsText = f"Possui uma raíz real: {x1:.2f}"
    else:
        rootsText = f"Não possui raízes reais"
    
    return rootsText

# p = 0.
# q = 0.
# x = 1.

# Trinômio quadrado
def y(x,p=1,q=1):
    return x**2 + p*x + q

def discriminante(p,q):
    return p*p - 4*q

def plot_trinomio(p,q):
    fig, ax = plt.subplots()
    xv = -p/2

    x = np.arange(xv-10, xv+10., 1e-2)
    plt.plot(x, y(x,p,q))
    
    
    ax.set_title("Trinômio - Plano Oxy")
    ax.set_xlabel("x")
    ax.set_ylabel("y(x)")
    plt.show()

def qRR(p, x):
    return -x*p - x**2

# retas raiz no plano de de fase (plano Opq)
def retas_raiz(p = np.arange(-10., 10., 1e-2), xs = np.arange(-2, 2, .5), ax = None, show = True):
    if ax is None:
        fig, ax = plt.subplots()
    # xs = np.array([1])
    
    parDisc = p**2/4
    
    for x in xs:
        # print(x)
        q = qRR(p, x)
        ax.plot(p, q, 'b')
        ax.text(p[-1],q[-1],f'x={x}',
                bbox=dict(boxstyle='round4',facecolor='white', alpha=0.8, edgecolor='blue'))


    ax.plot(p, parDisc, 'r')
    ax.text(p[-1]+.2,parDisc[-1],f'q = p²/4',
            bbox=dict(boxstyle='round4',facecolor='white', alpha=0.8, edgecolor='red'))
    
    if (len(xs) == 1):
        ax.fill_between(p,q,parDisc,where=p<-2*xs,facecolor='green',label="região A",alpha=0.5)
        ax.text(p[0],(q[0]+parDisc[0])/2,f'A',
                bbox=dict(boxstyle='circle' if -2*x>p[0] else 'larrow',facecolor='white', alpha=0.8, edgecolor='green'))
        
        ax.fill_between(p,q,parDisc,where=p>-2*xs,facecolor='blue',label="região B",alpha=0.5)
        ax.text(p[-1],(q[-1]+parDisc[-1])/2,f'B',
                bbox=dict(boxstyle='circle' if -2*x<p[-1] else 'rarrow',facecolor='white', alpha=0.8, edgecolor='blue'))
        
        ax.fill_between(p,np.min(q),q,facecolor='red',label="região C",alpha=0.5)
        ax.text((p[0]+p[-1])/2,np.min(q),f'C',
                bbox=dict(boxstyle='circle',facecolor='white', alpha=0.8, edgecolor='red'))
    
    if show:
        ax.set_title("Retas raízes - Plano Opq")
        ax.set_xlabel("p")
        ax.set_ylabel("q(p)")
        # ax.legend()
        plt.show()
    return ax

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWindow()
    ui.setupUi(MainWindow)

    # retas_raiz()
    ui.windowRun()   # I did this :)
    
    MainWindow.show()
    sys.exit(app.exec_())