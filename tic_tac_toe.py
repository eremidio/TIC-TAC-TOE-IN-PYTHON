#Vamos criar um jogo da velha usando gui em Python
#
#
#

#Importando bibliotecas
import tkinter as tk
import tkinter.ttk as ttk

#CRIAÇÃO DE JANELA E CONFIGURAÇÕES GERAIS DO APP
#Abrindo uma janela
janela=tk.Tk()
janela.resizable(True, True)
janela.title("JOGO DA VELHA")
janela.geometry("480x540")

#Configurando linhas e colunas
for i in range(5):
 for j in range(3):
  janela.columnconfigure(j, weight=1, minsize=40)
  janela.rowconfigure(i, weight=1, minsize=40)

#BACK-END DO APP (DEFINIÇÃO DE VARIÁVEIS E FUNÇÕES ÚTEIS)
#Variáveis TK
# Variáveis de preenchimento do tabuleiro
um=tk.StringVar()
dois=tk.StringVar()
tres=tk.StringVar()
quatro=tk.StringVar()
cinco=tk.StringVar()
seis=tk.StringVar()
sete=tk.StringVar()
oito=tk.StringVar()
nove=tk.StringVar()

#Símbolos associados a cada jogador
player1=tk.StringVar()
player2=tk.StringVar()


#Função que define o turno em que cada jogador efetua sua jogada ()
primeiro=tk.BooleanVar()
segundo=tk.BooleanVar()

#Funções úteis
#Funções de uso geral
def sair():
 '''Função para sair do app'''
 quit()


def iniciar_jogo():
 '''Função que define a ordem das jogadas'''
 global primeiro
 global segundo
 global player1
 global player2
 primeiro=True
 segundo=False
 player1='X'
 player2='O'


def resetar_jogo():
 '''Função que reseta o jogo, preparando-o para uma nova partida, ajustando as variáveis TK e resetando a tela do app'''
 global primeiro
 global segundo
 global um
 global dois
 global tres
 global quatro
 global cinco
 global seis
 global sete
 global oito
 global nove
 primeiro = True
 segundo = False
 um = ' '
 dois = ' '
 tres = ' '
 quatro = ' '
 cinco = ' '
 seis = ' '
 sete = ' '
 oito = ' '
 nove = ' '
 botao1.configure(text=' ')
 botao2.configure(text=' ')
 botao3.configure(text=' ')
 botao4.configure(text=' ')
 botao5.configure(text=' ')
 botao6.configure(text=' ')
 botao7.configure(text= ' ')
 botao8.configure(text= ' ')
 botao9.configure(text= ' ')
 rotulo.configure(text=' ')


def vitoria():
 '''Função que determina se há um vencedor no jogo e assinala este fator na tela do aoo'''
 global dois
 global tres
 global quatro
 global cinco
 global seis
 global sete
 global oito
 global nove

 if(um==dois==tres=='X' or um==quatro==sete=='X' or um==cinco==nove=='X' or dois==cinco==oito=='X' or tres==seis==nove=='X' or tres==cinco==sete=='X' or quatro==cinco==seis=='X' or sete==oito==nove=='X'):
  rotulo.configure(text="O JOGADOR 1 VENCEU A PARTIDA. PARABÉNS!!!\n")
 rotulo.after(80, vitoria)
 if(um==dois==tres=='O' or um==quatro==sete=='O' or um==cinco==nove=='O' or dois==cinco==oito=='O' or tres==seis==nove=='O' or tres==cinco==sete=='O' or quatro==cinco==seis=='O' or sete==oito==nove=='O'):
  rotulo.configure(text="O JOGADOR 2 VENCEU A PARTIDA. PARABÉNS!!!\n")


#Função de ativação dos botões do tabuleiro
def botao1_clique():
 '''Função de ativação de um botão do tabuleiro do app'''
 global primeiro
 global segundo
 global player1
 global player2
 global um
 if(primeiro==True and segundo==False):
  botao1.configure(text=player1)
  um=player1
  primeiro=False
  segundo=True
  vitoria()
  return
 if(primeiro==False and segundo==True):
  botao1.configure(text=player2)
  um=player2
  primeiro=True
  segundo=False
  vitoria()
  return


def botao2_clique():
 '''Função de ativação de um botão do tabuleiro do app'''
 global primeiro
 global segundo
 global player1
 global player2
 global dois
 if(primeiro==True and segundo==False):
  botao2.configure(text=player1)
  dois=player1
  primeiro=False
  segundo=True
  vitoria()
  return
 if(primeiro==False and segundo==True):
  botao2.configure(text=player2)
  dois=player2
  primeiro=True
  segundo=False
  vitoria()
  return

def botao3_clique():
 '''Função de ativação de um botão do tabuleiro do app'''
 global primeiro
 global segundo
 global player1
 global player2
 global tres
 if(primeiro==True and segundo==False):
  botao3.configure(text=player1)
  tres=player1
  primeiro=False
  segundo=True
  vitoria()
  return
 if(primeiro==False and segundo==True):
  botao3.configure(text=player2)
  tres=player2
  primeiro=True
  segundo=False
  vitoria()
  return

def botao4_clique():
 '''Função de ativação de um botão do tabuleiro do app'''
 global primeiro
 global segundo
 global player1
 global player2
 global quatro
 if(primeiro==True and segundo==False):
  botao4.configure(text=player1)
  quatro=player1
  primeiro=False
  segundo=True
  vitoria()
  return
 if(primeiro==False and segundo==True):
  botao4.configure(text=player2)
  quatro=player2
  primeiro=True
  segundo=False
  vitoria()
  return

def botao5_clique():
 '''Função de ativação de um botão do tabuleiro do app'''
 global primeiro
 global segundo
 global player1
 global player2
 global cinco
 if(primeiro==True and segundo==False):
  botao5.configure(text=player1)
  cinco=player1
  primeiro=False
  segundo=True
  vitoria()
  return
 if(primeiro==False and segundo==True):
  botao5.configure(text=player2)
  cinco=player2
  primeiro=True
  segundo=False
  vitoria()
  return

def botao6_clique():
 '''Função de ativação de um botão do tabuleiro do app'''
 global primeiro
 global segundo
 global player1
 global player2
 global seis
 if(primeiro==True and segundo==False):
  botao6.configure(text=player1)
  seis=player1
  primeiro=False
  segundo=True
  vitoria()
  return
 if(primeiro==False and segundo==True):
  botao6.configure(text=player2)
  seis=player2
  primeiro=True
  segundo=False
  vitoria()
  return

def botao7_clique():
 '''Função de ativação de um botão do tabuleiro do app'''
 global primeiro
 global segundo
 global player1
 global player2
 global sete
 if(primeiro==True and segundo==False):
  botao7.configure(text=player1)
  sete=player1
  primeiro=False
  segundo=True
  vitoria()
  return
 if(primeiro==False and segundo==True):
  botao7.configure(text=player2)
  sete=player2
  primeiro=True
  segundo=False
  vitoria()
  return

def botao8_clique():
 '''Função de ativação de um botão do tabuleiro do app'''
 global primeiro
 global segundo
 global player1
 global player2
 global oito
 if(primeiro==True and segundo==False):
  botao8.configure(text=player1)
  oito=player1
  primeiro=False
  segundo=True
  vitoria()
  return
 if(primeiro==False and segundo==True):
  botao8.configure(text=player2)
  oito=player2
  primeiro=True
  segundo=False
  vitoria()
  return

def botao9_clique():
 '''Função de ativação de um botão do tabuleiro do app'''
 global primeiro
 global segundo
 global player1
 global player2
 global nove
 if(primeiro==True and segundo==False):
  botao9.configure(text=player1)
  nove=player1
  primeiro=False
  segundo=True
  vitoria()
  return
 if(primeiro==False and segundo==True):
  botao9.configure(text=player2)
  nove=player2
  primeiro=True
  segundo=False
  vitoria()
  return

#PARTE GRÁFICA DO APP
#Adicionando os widgets
#Frames para acondicionar o teclado oinde sera jogado o jogo
frame1=tk.Frame(relief=tk.SUNKEN, height=60, width=40)
frame1.grid(row=0, column=0)
frame2=tk.Frame(relief=tk.SUNKEN, height=60, width=40)
frame2.grid(row=0, column=1)
frame3=tk.Frame(relief=tk.SUNKEN, height=60, width=40)
frame3.grid(row=0, column=2)
frame4=tk.Frame(relief=tk.SUNKEN, height=60, width=40)
frame4.grid(row=1, column=0)
frame5=tk.Frame(relief=tk.SUNKEN, height=60, width=40)
frame5.grid(row=1, column=1)
frame6=tk.Frame(relief=tk.SUNKEN, height=60, width=40)
frame6.grid(row=1, column=2)
frame7=tk.Frame(relief=tk.SUNKEN, height=60, width=40)
frame7.grid(row=2, column=0)
frame8=tk.Frame(relief=tk.SUNKEN, height=60, width=40)
frame8.grid(row=2, column=1)
frame9=tk.Frame(relief=tk.SUNKEN, height=60, width=40)
frame9.grid(row=2, column=2)
frame10=tk.Frame(relief=tk.FLAT, height=60, width=40)
frame10.grid(row=3, column=0, rowspan=1, columnspan=3)
frame11=tk.Frame(relief=tk.FLAT, height=60, width=40)
frame11.grid(row=4, column=0)
frame12=tk.Frame(relief=tk.FLAT, height=60, width=40)
frame12.grid(row=4, column=1)
frame13=tk.Frame(relief=tk.FLAT, height=60, width=40)
frame13.grid(row=4, column=2)

#Adicionando os botões e rótulos do app
#Tabuleiro
botao1=tk.Button(master=frame1, relief=tk.SUNKEN, bg='white', fg='blue', font=('Arial', 60), height=80, width=80, command=botao1_clique)
botao1.pack(fill=tk.BOTH, expand=True)
botao2=tk.Button(master=frame2, relief=tk.SUNKEN, bg='white', fg='blue', font=('Arial', 60), height=80, width=80, command=botao2_clique)
botao2.pack(fill=tk.BOTH, expand=True)
botao3=tk.Button(master=frame3, relief=tk.SUNKEN, bg='white', fg='blue', font=('Arial', 60), height=80, width=80, command=botao3_clique)
botao3.pack(fill=tk.BOTH, expand=True)
botao4=tk.Button(master=frame4, relief=tk.SUNKEN, bg='white', fg='blue', font=('Arial', 60), height=80, width=80, command=botao4_clique)
botao4.pack(fill=tk.BOTH, expand=True)
botao5=tk.Button(master=frame5, relief=tk.SUNKEN, bg='white', fg='blue', font=('Arial', 60), height=80, width=80, command=botao5_clique)
botao5.pack(fill=tk.BOTH, expand=True)
botao6=tk.Button(master=frame6, relief=tk.SUNKEN, bg='white', fg='blue', font=('Arial', 60), height=80, width=80, command=botao6_clique)
botao6.pack(fill=tk.BOTH, expand=True)
botao7=tk.Button(master=frame7, relief=tk.SUNKEN, bg='white', fg='blue', font=('Arial', 60), height=80, width=80, command=botao7_clique)
botao7.pack(fill=tk.BOTH, expand=True)
botao8=tk.Button(master=frame8, relief=tk.SUNKEN, bg='white', fg='blue', font=('Arial', 60), height=80, width=80, command=botao8_clique)
botao8.pack(fill=tk.BOTH, expand=True)
botao9=tk.Button(master=frame9, relief=tk.SUNKEN, bg='white', fg='blue', font=('Arial', 60), height=80, width=80, command=botao9_clique)
botao9.pack(fill=tk.BOTH, expand=True)

#Rótulo exeibindo o status do jogo
rotulo=tk.Label(master=frame10, bg='white', fg='black', justify=tk.CENTER)
rotulo.pack(fill=tk.BOTH, expand=True)

#Botões de uso geral
botao11=tk.Button(master=frame11, relief=tk.RAISED, bg='gray', fg='black', font=('Arial', 12), height=80, width=80, text="Iniciar", command=iniciar_jogo)
botao11.pack(fill=tk.BOTH, expand=True)
botao12=tk.Button(master=frame12, relief=tk.RAISED, bg='gray', fg='black', font=('Arial', 12), height=80, width=80, text="Resetar", command=resetar_jogo)
botao12.pack(fill=tk.BOTH, expand=True)
botao13=tk.Button(master=frame13, relief=tk.RAISED, bg='gray', fg='black', font=('Arial', 12), height=80, width=80, text='Sair', command=sair)
botao13.pack(fill=tk.BOTH, expand=True)

#Exibindo o app
janela.mainloop() 
