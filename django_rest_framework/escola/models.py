from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
     ) # A letra é como vai ser representado no Banco de Dados, a palavra completa é como eu irei visualizar essa informação

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B') #Se o curso não tiver nenhuma representação, por padrão será do nivel 'B' que é o 'Básico'

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    PERIODO = {
        ('M', 'Matutino'),
        ('V', 'Vespetino'),
        ('N', 'Noturno')
    }
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) # O aluno será referenciado com a matricula através do seu id (ForeignKey)
    # O CASCADE é para caso o aluno seja excluído / desligado, a sua matricula seja automaticamente excluída 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M') 
