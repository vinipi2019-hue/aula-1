class Corrida:
    def __init__(self, origem, destino, distancia_km):

        self.origem = origem
        self.destino = destino
        self.distancia_km = distancia_km
        self.valor = 0

    def calcular_valor(self):
        if self.distancia_km <= 5:
            self.valor = 10
        elif self.distancia_km <= 10:
            self.valor = 15
        else:
            self.valor = 20

    def exibir_resumo(self):
        print(f"Origem: {self.origem}")
        print(f"Destino: {self.destino}")
        print(f"Distância: {self.distancia_km} km")
        print(f"Valor: R$ {self.valor:.2f}")


 # depois de completar a classe, teste assim:
corrida1 = Corrida ("Praça do Ferreira","Beira Mar", 8)
corrida1. calcular_valor()
corrida1. exibir_resumo()