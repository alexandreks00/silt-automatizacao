import tkinter as tk
from tkinter import filedialog
from basePage import BasePage

from sheet import Sheet
from login import Login
from entidade import Entidade
from depositante import Depositante
from api import Api
from setor import Setor
from ftp import Ftp
from selenium import webdriver
from orPy import Or
from padrao_integracao import PadraoIntegracao
from setor_padrao import SetorPadrao
from  tipo_pedido import TipoPedido
import time

sheet_class = Sheet(
    "C:/Users/luiz_/workspace/pessoal/infra-auto/infraAuto/silt-template.xlsx")

def import_python_file():
  file_path = filedialog.askopenfilename(title="Selecione um arquivo Excel", filetypes=[("Arquivos Excel", "*.xlsx")])
  if file_path:
    print(file_path)
  
def concluir_etapa(etapa):
    etapa.config(background='green', text="✔️ " + etapa['text'])

def criar_linha_tempo(window):
    window.title("Linha do Tempo")
   # Configuração do estilo
    estilo_label = {"font": ("Helvetica", 14), "pady": 10}

    # Importação da tabela
    lbl_importacao = tk.Label(window, text="Importação da tabela", **estilo_label)
    lbl_importacao.pack()

    # Criação da entidade
    lbl_entidade = tk.Label(window, text="Criação da entidade", **estilo_label)
    lbl_entidade.pack()

    # Criação do depositante
    lbl_depositante = tk.Label(window, text="Criação do depositante", **estilo_label)
    lbl_depositante.pack()

    # Configuração da API
    lbl_api = tk.Label(window, text="Configuração da API", **estilo_label)
    lbl_api.pack()

    # Botão para concluir a etapa
    # btn_concluir = tk.Button(window, text="Concluir", command=lambda: concluir_etapa(lbl_api))
    # btn_concluir.pack()

    rotulos = [lbl_importacao, lbl_entidade, lbl_depositante, lbl_api]
    return rotulos    

window = tk.Tk()
window.geometry("800x800") 

label = tk.Label(window, text="Infracomerce", font=("Arial", 24), width=30, height=10, justify="center")
label.pack()


button = tk.Button(window, text="Importar planilha", command=import_python_file)
button.pack()

rotulos = criar_linha_tempo(window)

# Inicia o loop principal da interface gráfica
window.mainloop()
