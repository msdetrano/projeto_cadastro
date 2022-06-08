from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sqlite3


#################### Criando tabela #####################

#Criar conexão e cursor
con = sqlite3.connect('clientes.db')
cur = con.cursor()
#Criar tabela clientes
cur.execute("""CREATE TABLE IF NOT EXISTS clientes (
            nome VARCHAR,
            telefone VARCHAR PRIMARY KEY,
            endereco VARCHAR,
            comp VARCHAR)""")




###################################### Função Entrar ###################################


def entrar():
    log = str(ent1.get())
    se = str(ent2.get())

    if log == "admin" and se =="admin":
        janela.destroy()
        
    else:
        messagebox.showinfo("Login", "Acesso Negado")
        exit
    
     
        

###################### Tela Login  ################################# 

janela = Tk()
corFundo = "grey"
corLetra = "black"

button_image = PhotoImage(file="login.png")

lbt = Label(janela, text="Area de Login dos Usuarios", bg=corFundo, fg="grey", font=("Verdana"),image=button_image)
lbt.place(x=50, y=20)

ent1 = Entry(janela)
ent1.place(x=80, y=100)

ent2 = Entry(janela, show="*")
ent2.place(x=80, y=140)

lblog = Label(janela, text="Login:",bg=corFundo,fg=corLetra)
lblog.place(x=30,y=100)

lbsenha = Label(janela, text="Senha",bg=corFundo,fg=corLetra)
lbsenha.place(x=30,y=140)

bt = Button(janela,text="Entra",bg="yellow",fg="black",command = entrar)
bt.place(x=100,y=220)



janela.title("Software - Marcos Detrano")
janela.geometry("300x300")
janela.configure(background=corFundo)
janela.mainloop()


#-----------------------------------------FUNÇÕES-----------------------------------------------------------#

#-----------------------------------------FUNÇÕES DE CADASTRO-----------------------------------------------------------#

def cadastraclientes(self):
        nome=self.entnome.get()
        idade=self.entidade.get()
        cpf=self.entcpf.get()
        email=self.entemail.get()
        fone=self.entfone.get()
        cidade=self.entcidade.get()
        
        try:
            cur.execute("INSERT INTO clientes VALUES(?,?,?,?,?,?)",
                    (nome,idade,cpf,email,fone,cidade))
        except:
            tkMessageBox.showinfo('Aviso!','Telefone ja cadastrado')  
        con.commit()
        self.fone.delete(0,END)
        

def limpaclientes(self):
        self.entnome.delete(0,END)
        self.entidade.delete(0,END)
        
def mostraclientes(self):
        self.mostra1.delete(0.0,END)
        fonec = self.fonec.get()
        cur.execute("SELECT * FROM clientes WHERE telefone = '%s'" %fonec)
        consulta = cur.fetchall()
        for i in consulta:
            self.mostra1.insert(END,'''Nome:{}
        End:{}
        Complemento:{}'''.format(i[0],i[2],i[3]))
    
# Função q aceita eventos do teclado, apenas chama a função mostraclientes quando a tecla Enter é pressionada
def mostraclientes_a(self,event):
        self.mostraclientes()


       
#--------------------------------------TKINTER INTERFACE------------------------------------------------#

################################# Tela Cadastro ####################
def teladecadastro():
    janela = Tk()

    lbtca = Label(janela,text="Area de Cadastro de Clientes")
    lbtca.place(x=50,y=20)


    lbnome = Label(janela, text="Nome:")
    lbnome.place(x=30,y=100)

    entnome = Entry(janela)
    entnome.place(x=80,y=100)

    lbidade = Label(janela, text="Idade:")
    lbidade.place(x=30,y=140)

    entidade = Entry(janela)
    entidade.place(x=80,y=140)

    lbcpf = Label(janela, text="CPF:")
    lbcpf.place(x=30,y=160)

    entcpf = Entry(janela)
    entcpf.place(x=80,y=160)

    lbemail = Label(janela, text="Email:")
    lbemail.place(x=30,y=180)

    entemail = Entry(janela)
    entemail.place(x=80,y=180)

    lbfone = Label(janela, text="Fone:")
    lbfone.place(x=30,y=200)

    entfone = Entry(janela)
    entfone.place(x=80,y=200)

    lbcidade = Label(janela, text="Cidade:")
    lbcidade.place(x=30,y=220)

    entcidade = Entry(janela)
    entcidade.place(x=80,y=220)

        
    bt = Button(janela,text="Cadastrar",bg="#511",fg="white")
    bt.place(x=150,y=240)

       

    janela.title('Cadastro')
    janela.geometry("400x400")
    janela.configure(background='white')
    janela.mainloop()



######################### Tela Menu ##################################

tela = Tk()
menubar = Menu(tela)
tela.config(menu=menubar)
tela.title('Software - Cadastro')
tela.geometry('720x480')

filemenu = Menu(menubar)
filemenu2 = Menu(menubar)
filemenu3 = Menu(menubar)
filemenu4 = Menu(menubar)

menubar.add_cascade(label='Cliente', menu=filemenu)
menubar.add_cascade(label='Fornecedor', menu=filemenu2)
menubar.add_cascade(label='Valor Dólar',menu=filemenu4)
menubar.add_cascade(label='Ajuda', menu=filemenu3)
def Quit(): root.destroy()
def Help(): messagebox.showinfo("Ajuda", "Qualquer duvida entre em contato com desenvolvedor")
def Sobre(): messagebox.showinfo("Sobre", "Desenvolvido por Marcos")
def dolar(): messagebox.showinfo("Dolar Hoje","Valor do Dólar Hoje: R$3.21")
filemenu.add_command(label='Cadastrar..',command=teladecadastro)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=Quit)
filemenu3.add_command(label='Ajuda', command=Help)
filemenu4.add_command(label='Cotação',command=dolar)
tela.iconbitmap('icone.ico')
tela.mainloop()
################## Fim Tela Menu #############################

