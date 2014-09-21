# -*- coding: iso-8859-1 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
from compactar import *
import tkMessageBox
from threading import Thread

class main:
#----------------------------INTERFACE-----------------------------------------    
    def __init__(self,master):
        self.botao_add = Button(master,text='Adicionar',font=('Arial','20'),
                                fg='green',command=self.adicionar)
        self.botao_add.place(relx=0.10,rely=0.08)
        self.botao_apaga = Button(master,text='Apagar',font=('Arial','20'),
                                fg='red',command=self.apagar)
        self.botao_apaga.place(relx=0.70,rely=0.08)
        self.lista = Listbox(master, selectmode=EXTENDED)
        self.lista.place(relx=0,rely=0.25,width=595,height=230)
        self.rolagemy = Scrollbar(master)
        self.rolagemy.place(relx=0.98,rely=0.25,height=230)
        self.rolagemx = Scrollbar(master,orient=HORIZONTAL)
        self.rolagemx.place(relx=0.0,rely=0.84,width=597)
        self.lista.config(yscrollcommand=self.rolagemy.set)
        self.lista.config(xscrollcommand=self.rolagemx.set)
        self.rolagemy.config(command=self.lista.yview)
        self.rolagemx.config(command=self.lista.xview)
        self.botao_compactar=Button(master,text='Espremer',font=('Arial','20'),
                                    fg='green',command=self.compactar)
        self.botao_compactar.place(relx=0.39,rely=0.89)
#---------------------------FUNÇÃO ADICIONAR ARQUIVO---------------------------
    def adicionar(self):
        arquivo = askopenfilename()
        if arquivo != '':
            self.lista.insert(END,arquivo)
#--------------------------FUNÇÃO APAGAR ARQUIVO-------------------------------
    def apagar(self):
        itens = self.lista.curselection()
        if len(itens) == 0:
            tkMessageBox.showinfo('Aviso', 'Selecione pelo menos 1 cabra!')
        else:
            posicao = 0
            for i in itens:
                item_pos = int(i) - posicao
                self.lista.delete(item_pos,item_pos)
                posicao = posicao + 1
#---------------------------FUNÇÃO COMPACTAR------------------------------------
    def compactar(self):
        arquivos = self.lista.get(0,END)
        if len(arquivos) == 0:
            tkMessageBox.showinfo("Aviso",'Adicione algum arquivo para ser compactado')
            return
        def executar():
            self.botao_compactar.configure(state=DISABLED)
            compactador=Compactador()
            compactador.compactar(arquivos)
            self.botao_compactar.configure(state=NORMAL)
        t = Thread(target=executar)
        t.start()

root = Tk()
#root.iconbitmap(default='zip.ico')
root.title(u"Espremedor da Muléstia 0.1")
root.geometry("600x400")
root.resizable(width=FALSE, height=FALSE)
main(root)
root.mainloop()
