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
from tipo_pedido import TipoPedido

import time


class Gui:
    def __init__(self, width=800, height=800):
      self.width = width
      self.height = height
      self.window = tk.Tk()
      self.window.geometry("800x800")
      self.sheet_class = Sheet(
      "C:/Users/luiz_/workspace/pessoal/infra-auto/infraAuto/silt-template.xlsx");
      self.driver = webdriver.Chrome()
      self.url_base = "https://synapcomhml2.seniorcloud.com.br/siltwms/"
      self.base_page = BasePage(self.driver)
  
    def concluir_etapa(etapa):
      etapa.config(background='green', text="✔️ " + etapa['text'])

    def create_config(self,):
          sheet_entidade = self.sheet_class.Import('entidade')
          self.driver.get(self.url_base)
          login_page = Login(self.base_page)
          login_page.Login("LUIZ.SSANTOS", "Dankicode2002")
          
          for empresa in sheet_entidade.itertuples(index=False):
              entidade_page = Entidade(self.base_page, empresa)
              entidade_page.create()

              depositante_page = Depositante(self.base_page, empresa)
              depositante_page.create()

              api_rest = Api(self.base_page, empresa)
              api_rest.create()

              sheet_ftp = self.sheet_class.Import('ftp')
              fpt = Ftp(self.base_page, empresa, sheet_ftp)
              fpt.create()

              sheet_setor = self.sheet_class.Import('setor')
            # create_setor(base_page, sheet_setor, empresa)

    def criar_linha_tempo(self):
        self.window.title("Linha do Tempo")
      # Configuração do estilo
        estilo_label = {"font": ("Helvetica", 14), "pady": 10}

        # Importação da tabela
        lbl_importacao = tk.Label(self.window, text="Importação da tabela", **estilo_label)
        lbl_importacao.pack()

        # Criação da entidade
        lbl_entidade = tk.Label(self.window, text="Criação da entidade", **estilo_label)
        lbl_entidade.pack()

        # Criação do depositante
        lbl_depositante = tk.Label(self.window, text="Criação do depositante", **estilo_label)
        lbl_depositante.pack()

        # Configuração da API
        lbl_api = tk.Label(self.window, text="Configuração da API", **estilo_label)
        lbl_api.pack()

        btn_concluir = tk.Button(self.window, text="Concluir", command=lambda: self.create_config())
        btn_concluir.pack()

        rotulos = [lbl_importacao, lbl_entidade, lbl_depositante, lbl_api]
        return rotulos    

    def main(self):
      
      def import_python_file():
        file_path = filedialog.askopenfilename(title="Selecione um arquivo Excel", filetypes=[("Arquivos Excel", "*.xlsx")])
        if file_path:
          print(file_path)
          self.sheet_class = Sheet(file_path)

    
      label = tk.Label(self.window, text="Infracomerce", font=("Arial", 24), width=30, height=10, justify="center")
      label.pack()

      self.criar_linha_tempo()

      button = tk.Button(self.window, text="Importar planilha", command=import_python_file)
      button.pack()
      pass


    

    def start(self):
      self.main()
      self.window.mainloop()
        
  


page = Gui()

page.start()
