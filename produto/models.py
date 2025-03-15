from django.db import models
import sys
sys.path.append("")
from empresa.models import *
class secao(models.Model):
    nome_secao=models.CharField(max_length=50)
    def __str__(self):
        return self.nome_secao
class preco(models.Model):
    valor=models.FloatField(null=True)
    def __str__(self):
        return str(self.valor)
class produtos(models.Model):
    nome_produto=models.CharField(max_length=100)
    secao=models.ForeignKey(secao,on_delete=models.CASCADE,verbose_name='Seção')
    imagem=models.ImageField(upload_to='produtos/')
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    status=models.CharField(max_length=2,default='1', null=True)
    preco=models.ForeignKey(preco, on_delete=models.CASCADE, null=True)
    carousel=models.CharField(max_length=2, default='0')
    def __str__(self) -> str:
        return self.nome_produto
class relatorio(models.Model):
    produto=models.ForeignKey(produtos,on_delete=models.CASCADE, default=None)
    data_busca=models.DateField(default=None)
    def __str__(self):
        return self.produto.nome_produto