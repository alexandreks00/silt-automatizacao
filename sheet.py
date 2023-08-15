import pandas as pd

class Sheet:
    def __init__(self, filePath):
        self.filePath = filePath 
        pass
    
    def Import(self, sheet_name):
        try:
          self.sheet = pd.read_excel(self.filePath, sheet_name=sheet_name)
          return self.sheet
        except FileNotFoundError:
          print("O arquivo não foi encontrado.")