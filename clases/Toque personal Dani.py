class Vehiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        
    def info(self):
        print(f"""
              modelo: {self.modelo}
              ano: {self.ano}
              """)
        
# class Coche(Vehiculo):
#     def __init__(self, modelo, ano, combustible):
#         super().__init__(modelo, ano)
#         self.combustible = combustible

class Acuatico(Vehiculo):
    def __init__(self, modelo, ano, num_velas):
        Vehiculo.__init__(self, modelo, ano)
        self.num_velas = num_velas
        
    def info(self):
        print(f"""
              modelo: {self.modelo}
              ano: {self.ano}
              num velas: {self.num_velas}
              """)
        
class Terrestre(Vehiculo):
    def __init__(self, modelo, ano, num_ruedas):
        Vehiculo.__init__(self, modelo, ano)
        self.num_ruedas = num_ruedas
        
    def info(self):
        print(f"""
              modelo: {self.modelo}
              ano: {self.ano}
              num velas: {self.num_ruedas}
              """)
        
class Anfibio(Terrestre, Acuatico):
    def __init__(self, modelo, ano, num_ruedas, num_velas):
        Terrestre.__init__(self, modelo, ano, num_ruedas)
        Acuatico.__init__(self, modelo, ano, num_velas)
        
    def info(self):
        print(f"""
              modelo: {self.modelo}
              ano: {self.ano}
              num ruedas: {self.num_ruedas}
              num velas: {self.num_velas}
              """)
        
Anfibio1 = Anfibio("Rana", "1953", "6", "12")
print(vars(Anfibio1))
Anfibio1.info()