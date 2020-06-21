class Application(object):
    def __init__(self):
        """constructeur de la fenétre principale"""
        self.root = Tk()
        self.root.title('Code des couleurs')
        self.dessineResistance()
        Label(self.root, text='Entrez la valeur de la résistance, en ohms:').grid(row=2, column=1, columnspan=3)
        Button(self.root, text='Montrer', command=self.changeCouleurs).grid(row=3, column=3)
        self.entree = Entry(self.root, width=14)
        self.entree.grid(row=3, column=2)
        self.cc = ['black', 'brown', 'red', 'orange', 'yellow',
                    'green', 'blue', 'purple', 'grey', 'white']
        
        self.root.mainloop()

    def dessineResistance(self):
        """Canevas avec un modéle de résistance à trois lignes colorées"""
        self.can = Canvas(self.root, width=250, height=100, bg='green')
        self.can.grid(row=1, column=1, columnspan=3, pady=5, padx=5)
        self.can.create_line(10,50,240,50,width=5)
        self.can.create_rectangle(65, 30, 185, 70, fill='light grey', width=2)
        self.ligne = []
        for x in range(85,150,24):
            self.ligne.append(self.can.create_rectangle(x,30,x+12,70, fill='black', width=0))

    def changeCouleurs(self):
        """Affichge des couleurs correspondant à la valeur entrée"""
        self.v1ch = self.entree.get()
        try:
            v = float(self.v1ch)
        except:
            err = 1
        else:
            err = 0
        if err == 1 or v<10 or v>1e11:
            self.signaleErreur()
        else:
            li = [0]*3
            logv = int(log10(v))
            ordgr = 10**logv

            li[0] = int(v/ordgr)
            decim = v/ordgr -li[0]
            li[1] = int(decim*10+.5)

            li[2] = logv-1

            for n in range(3):
                self.can.itemconfigure(self.ligne[n], fill=self.cc[li[n]])

    def signaleErreur(self):
        self.entree.configure(bg='red')
        self.root.after(1000, self.videEntree)

    def videEntree(self):
        self.entree.configure(bg='white')
        self.entree.delete(0, len(self.v1ch))

if __name__ == '__main__':
    from tkinter import *
    from math import log10

    f = Application()


































































    



















    
    
    
    
    
    
    
    
    











