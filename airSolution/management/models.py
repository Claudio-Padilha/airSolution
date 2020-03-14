from django.db import models
from enum import Enum

# Enum used to give acess level to users
class AcessLevel(Enum):                            
    ADMIN = 1
    TECHNICIAN = 2
    SELLER = 3
    CLIENT = 4

##################################################################################################

    ## System Users ##
class Gerente(models.Model):
    name = models.CharField(max_length=40)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=15)
    birth_date = models.DateField()
    adress = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    salary = models.FloatField()
    acess_level = models.IntegerField()

    def __str__(self):
        return "Gerente: " + self.name

class Tecnico(models.Model):
    name = models.CharField(max_length=40)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=15)
    birth_date = models.DateField()
    adress = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    salary = models.FloatField()
    acess_level = models.IntegerField()

    def __str__(self):
        return "Técnico: " + self.name

class Cliente(models.Model):
    name = models.CharField(max_length=40)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=15)
    birth_date = models.DateField()
    adress = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    acess_level = models.IntegerField()
    payed = models.BooleanField()

    def __str__(self):
        return "Cliente: " + self.name

class Vendedor(models.Model):
    name = models.CharField(max_length=40)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=15)
    birth_date = models.DateField()
    adress = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    salary = models.FloatField()
    acess_level = models.IntegerField()

    def __str__(self):
        return "Vendedor: " + self.name


    ## Statistics helping structures
class VisitaTecnica(models.Model):
    technician = models.ForeignKey('Tecnico', on_delete=models.CASCADE,)
    scheduled = models.DateTimeField()
    observations = models.CharField(max_length=200)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    rating = models.FloatField()

    def __str__(self):
        return "Técnico da visita: " + self.technician.name + ".\n Data da visita: " + str(self.check_in)

class VisitaVenda(models.Model):
    seller = models.ForeignKey('Vendedor', on_delete=models.CASCADE,)
    client_name = models.CharField(max_length=40)
    client_phone = models.CharField(max_length=15)
    client_email = models.EmailField()
    adress = models.CharField(max_length=80)
    scheduled = models.DateTimeField()
    observations = models.CharField(max_length=200)
    was_sale = models.BooleanField()
    rating = models.FloatField()

    def __str__(self):
        return "Vendedor da visita: " + self.seller.name + ".\n Data da visita: " + str(self.scheduled)

    ## Objects on the system
class Maquina(models.Model):
    install_date = models.DateTimeField(auto_now_add=True)
    manufacturer = models.CharField(max_length=40)
    serial_number = models.CharField(max_length=30)                                   # Qual tamanho do numero de serie?
    potency = models.FloatField()                                                     # Preciso de um Float?
    model = models.CharField(max_length=30)
    client = models.ForeignKey('Cliente', on_delete=models.CASCADE,)
    qrcode = models.CharField(max_length=260)
    pipe_amount = models.FloatField()                                                     # Preciso de um Float?

    def __str__(self):
        return "Fabricante: " + self.manufacturer + ", Modelo: " + self.model + "\nProprietário: " + self.client.name

class Produto(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    conditions = models.CharField(max_length=400)
    services = models.CharField(max_length=400)

    def __str__(self):
        return "Produto: " + self.name