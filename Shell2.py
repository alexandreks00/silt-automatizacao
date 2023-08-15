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
from transportadora import Transportadora

import tkinter as tk
from tkinter import filedialog

import time


class InfraAuto:
    def __init__(self):
        self.sheet_class = Sheet("")
        self.base_page = None
        self.setor = None
        self.block = True
        self.url = "https://synapcomhml2.seniorcloud.com.br/siltwms/"
        self.ambiente = 0  # 0 - Homolog 1 - Production
        self.userName = "luiz.ssantos"

    def import_python_file(self):
        window = tk.Tk()
        window.geometry("800x800")
        window.title("Importador Silt")

        def close_window():
            window.destroy()

        def import_python_file():
            file_path = filedialog.askopenfilename(
                title="Selecione um arquivo Excel", filetypes=[("Arquivos Excel", "*.xlsx")])

            if file_path:
                self.sheet_class = Sheet(file_path)
                self.block = False
                label_status["text"] = "Planilha importada com sucesso!"
                infra_auto.start()
                close_window()
                infra_auto.run()

        def update_settings(*args):
            selected_ambiente_value = selected_ambiente.get()

            if selected_ambiente_value == "Production":
                self.url = "https://wms.synapcom.com.br/siltwms/"
                self.userName = "LUIZ.SSANTOS"
            else:
                self.url = "https://synapcomhml2.seniorcloud.com.br/siltwms/"
                self.userName = "luiz.ssantos"
        selected_ambiente = tk.StringVar()
        selected_ambiente.set("homolog")

        radio_homolog = tk.Radiobutton(
            window, text="Homolog", variable=selected_ambiente, value="homolog")
        radio_homolog.pack()

        radio_production = tk.Radiobutton(
            window, text="Production", variable=selected_ambiente, value="Production")
        radio_production.pack()

        selected_ambiente.trace("w", update_settings)

        button = tk.Button(window, text="Importar planilha",
                           command=import_python_file)
        button.pack()

        label_status = tk.Label(window, text="")
        label_status.pack()
        button_close = tk.Button(window, text="Fechar", command=close_window)
        button_close.pack()
        window.mainloop()

    def start(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        self.base_page = BasePage(driver)
        self.base_page.driver.maximize_window()

        login_page = Login(self.base_page)
        login_page.Login(self.userName, "silt123")

        time.sleep(2)

    def create_entidade(self):
        print('Creating 1 Entidade')
        sheet_entidade = self.sheet_class.Import('entidade')

        for empresa in sheet_entidade.itertuples(index=False):
            entidade_page = Entidade(self.base_page, empresa)
            entidade_page.create()
            
            self.base_page.reaload()
            time.sleep(5)
            depositante_page = Depositante(self.base_page, empresa)
            depositante_page.create()

            self.base_page.reaload()
            time.sleep(5)

            api_rest = Api(self.base_page, empresa)
            api_rest.create()
            time.sleep(5)
            sheet_ftp = self.sheet_class.Import('ftp')
            fpt = Ftp(self.base_page, empresa, sheet_ftp)
            fpt.create()

        time.sleep(5)
        self.base_page.closeAll()
        self.base_page.reaload()

    def create_setor(self):
        print('Creating 2 Setor')
        sheet_setor = self.sheet_class.Import('setor')
        sheet_entidade = self.sheet_class.Import('entidade')

        for setor_data in sheet_setor.itertuples(index=False):
            self.setor = Setor(self.base_page, setor_data, sheet_entidade)
            self.setor.create()

        time.sleep(30)
        self.base_page.reaload()

    def create_depositante(self):
        print('Creating 3 Depositante')
        sheet_setor = self.sheet_class.Import('setor')
        sheet_entidade = self.sheet_class.Import('entidade')

        for setor_data in sheet_setor.itertuples(index=False):
            self.setor = Setor(self.base_page, setor_data, sheet_entidade)
            self.setor.createDepositante()

        time.sleep(10)

        self.base_page.closeAll()
        self.base_page.reaload()

    def create_tipo_recebimento(self):
        print('Creating 4 Recebimento')
        sheet_setor = self.sheet_class.Import('setor')
        sheet_entidade = self.sheet_class.Import('entidade')

        for setor_data in sheet_setor.itertuples(index=False):
            self.base_page.reaload()

            self.setor = Setor(self.base_page, setor_data, sheet_entidade)

            if isinstance(setor_data.tipo_recebimento, str):
                tipos_recebimentos = setor_data.tipo_recebimento.split(";")
                self.setor.tipo_recebimento(tipos_recebimentos)
            else:
                self.setor.tipo_recebimento([])

        time.sleep(3)
        self.base_page.closeAll()
        self.base_page.reaload()

    def create_regiao_armazenagem(self):
        print('Creating 5 Armazenamento')
        sheet_setor = self.sheet_class.Import('setor')
        sheet_entidade = self.sheet_class.Import('entidade')

        for setor_data in sheet_setor.itertuples(index=False):
            setor = Setor(self.base_page, setor_data, sheet_entidade)
            sheet_regiao_armazenagem = self.sheet_class.Import(
                'regiao_armazenagem')

            for regiao in sheet_regiao_armazenagem.itertuples(index=False):
                setor.regiao_armazenagem(regiao)

            break
        time.sleep(3)
        self.base_page.closeAll()
        self.base_page.reaload()

    def create_or(self):
        print('Creating 6 Or')
        sheet_or = self.sheet_class.Import('or')
        sheet_setor = self.sheet_class.Import('setor')
        sheet_entidade = self.sheet_class.Import('entidade')

        or_page = Or(self.base_page, sheet_setor, sheet_or, sheet_entidade)
        or_page.create()
        time.sleep(3)
        print("Create - Or")
        self.base_page.closeAll()
        self.base_page.reaload()

    def create_padrao_integracao(self):
        print('Creating 7 Intergrecao')
        sheet_setor = self.sheet_class.Import('setor')
        sheet_padroa_integracao = self.sheet_class.Import('padrao_integracao')
        sheet_entidade = self.sheet_class.Import('entidade')

        padrao_integracao_page = PadraoIntegracao(
            self.base_page, sheet_setor, sheet_padroa_integracao, sheet_entidade)
        padrao_integracao_page.create()
        time.sleep(3)
        print("Create - Padrão Integração ")
        self.base_page.closeAll()
        self.base_page.reaload()

    def create_setor_padrao(self):
        print('Creating 8 Setor Padrao')
        sheet_setor_padrao = self.sheet_class.Import('setor_padrao')
        sheet_empresa = self.sheet_class.Import('entidade')
        setor_padrao_page = SetorPadrao(
            self.base_page, sheet_setor_padrao, sheet_empresa)
        setor_padrao_page.create()
        time.sleep(3)
        print("Create - Setor Padrão")
        self.base_page.closeAll()
        self.base_page.reaload()

    def create_tipo_pedido(self):
        print('Creating 9 Pedido')
        sheet_tipo_pedido = self.sheet_class.Import('tipo_pedido')
        sheet_setor = self.sheet_class.Import('setor')
        tipo_pedido_page = TipoPedido(
            self.base_page, sheet_tipo_pedido, sheet_setor)
        tipo_pedido_page.create()
        time.sleep(3)
        print("Create - Tipo de Pedido")
        self.base_page.closeAll()
        self.base_page.reaload()

    def create_transportadora(self):
        print('Creating 10 Transportadora')
        sheet_transportadora = self.sheet_class.Import('transportadora')
        sheet_entidade = self.sheet_class.Import('entidade')
        sheet_transportadora['cnpj_transportadora'] = sheet_transportadora['cnpj_transportadora'].apply(
            lambda item: item.replace(" ", "")
        )

        create_transportadora = Transportadora(
            self.base_page, sheet_transportadora, sheet_entidade)
        create_transportadora.create_transportadora()
        time.sleep(3)
        print("Create - Transportadora")

        self.base_page.closeAll()
        self.base_page.reaload()


    def run(self):
        while True:
            print("Bem Vindo")
            print("1 - Criar Entidade e suas configurações")
            print("2 - Criar Setor")
            print("3 - Criar Depositante")
            print("4 - Criar Tipo Recebimento")
            print("5 - Criar Regiao Armazenagem")
            print("6 - Criar Or")
            print("7 - Criar Padrão Integração")
            print("8 - Criar Setor Padrão")
            print("9 - Criar Tipo Pedido")
            print("10 - Criar transportadora")
            print("15 - Cadastro completo")

            op = 0

            while True:
                user_input = input(": ")
                try:
                    op = int(user_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            if op == 1:
                self.create_entidade()
            elif op == 2:
                self.create_setor()
            elif op == 3:
                self.create_depositante()
            elif op == 4:
                self.create_tipo_recebimento()
            elif op == 5:
                self.create_regiao_armazenagem()
            elif op == 6:
                self.create_or()
            elif op == 7:
                self.create_padrao_integracao()
            elif op == 8:
                self.create_setor_padrao()
            elif op == 9:
                self.create_tipo_pedido()
            elif op == 10:
                self.create_transportadora()
            elif op == 15:
                self.create_entidade()
                time.sleep(5)
                self.create_setor()
                time.sleep(5)
                self.create_depositante()
                time.sleep(5)
                self.create_tipo_recebimento()
                time.sleep(5)
                self.create_regiao_armazenagem()
                time.sleep(5)
                self.create_or()
                time.sleep(5)
                self.create_padrao_integracao()
                time.sleep(5)
                self.create_setor_padrao()
                time.sleep(5)
                self.create_tipo_pedido()
            elif op == 0:
                break


infra_auto = InfraAuto()
infra_auto.import_python_file()
