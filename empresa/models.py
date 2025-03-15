from django.db import models
import sys
sys.path.append("")
from pacotes.models import Pacote

class Estado(models.Model):
   nome_estado = models.CharField(max_length=100)
   uf = models.CharField(max_length=3)
   def __str__(self) -> str:
      return self.uf

class Cidade(models.Model):
   nome_cidade = models.CharField(max_length=100)
   uf = models.ForeignKey(Estado, on_delete=models.CASCADE)
   def __str__(self):
      return ''+str(self.nome_cidade)+'-'+str(self.uf)
   

class Empresa(models.Model):
   nome_empresa = models.CharField(max_length=100)
   
   cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
   rua = models.CharField(max_length=255)
   bairro = models.CharField(max_length=255)
   quant_prod=models.IntegerField(default=0)
   pacote=models.ForeignKey(Pacote,on_delete=models.CASCADE, null=True,verbose_name='Selecione o Pacote')
   status=models.IntegerField(default=1)
   def __str__(self) -> str:
      return self.nome_empresa
   
   
