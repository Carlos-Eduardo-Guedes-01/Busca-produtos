from django import forms
from pacotes.models import Pacote

class PacoteForm(forms.ModelForm):
    class Meta:
        model=Pacote
        fields='__all__'
        widgets={
            'nome':forms.TextInput(attrs={
                'class':'campo','placeholder':'Nome do Pacote',}),
            'custo':forms.NumberInput(attrs={ 'class': 'campo'}),
            'quant_prod':forms.NumberInput(attrs={'class':'campo','placeholder':'Quantidade de Produtos'}),
            'quant_carousel':forms.NumberInput(attrs={'class':'campo','placeholder':'Quantidade no Carousel'}),
            'descricao':forms.Textarea(attrs={
                'class':'campo','placeholder':'Descrição do Pacote'}),
        }