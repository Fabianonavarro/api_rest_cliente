from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("O", "Outros")
    )
    nome = models.CharField(max_length=60, null=False, blank=False)
    cpf = models.CharField(max_length=12, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    #sexo = models.CharField(max_length=2)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=14, blank=False)
    endereco = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=40, blank=True)
    cidade = models.CharField(max_length=40, blank=True )
    estado = models.CharField(max_length=3, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    
      
    
    def __str__(self):
        return self.nome
    
    

