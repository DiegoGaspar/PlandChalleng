import math
from django.db import models

#Criação do Modelo do carro
class Modelo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

#Classe objeto carro
class Car(models.Model):
    placa = models.CharField(max_length=7)
    km_atual = models.IntegerField()
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    Capacidade_Tanque = models.DecimalField(max_digits= 5, decimal_places=2)
    Comb_Atual = models.DecimalField(max_digits= 5, decimal_places=2)

    #Estado do tanque em Porcentagem
    def calc_tanque(self):
        estado = (self.Comb_Atual / self.Capacidade_Tanque) * 100
        return estado

    def estado_combustivel(self):
        return str("%.f" % self.calc_tanque()) + ' %'

    def reabastecer(self, litros):
        self.Comb_Atual += litros
        self.Comb_Atual.save()
        return self.Comb_Atual

    def __str__(self):
       return self.modelo.nome + ' - ' + self.placa

#Criação do Pneu
class Tyre(models.Model):
    estado_degradacao =  models.IntegerField(default=0)
    carro = models.ForeignKey(Car, on_delete=models.CASCADE)

    # retorno do estado em porcentagem
    def calc_estado_pneu(self):
        if self.estado_degradacao <=100:
            deg = (self.estado_degradacao/100) * 100
        return deg

    def est_pneu(self):
        return str("%.f" % self.calc_estado_pneu()) + ' %'

    def __str__(self):
        return 'pneu do carro '+self.carro.placa

#Modelo de Viajem
class Viajem(models.Model):
    veiculo = models.ForeignKey(Car, on_delete=models.CASCADE)
    distancia = models.IntegerField()

    def km_final(self):
        self.veiculo.km_atual += self.distancia
        self.veiculo.save()
        return self.veiculo.km_atual

    def est_pne(self):
        pass





