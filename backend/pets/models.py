from django.db import models

class Pet(models.Model):
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível para adoção'),
        ('ADOTADO', 'Já adotado'),
        ('TRATAMENTO', 'Em tratamento médico'),
    ]

    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.IntegerField(help_text="Idade em meses")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL')

    def __str__(self):
        return self.nome