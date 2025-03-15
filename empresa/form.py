from dataclasses import field
from django import forms
from empresa.models import Empresa

class DadosForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nome_empresa','cidade','rua','bairro','pacote')
        '''labels={
            'nome_empresa':'',
            'tipo':'',
            'cidade':'',
            'rua': '',
            'bairro': '',
            'pacote': '',
        }'''
        widgets = {
            'nome_empresa': forms.TextInput(attrs={ 'class': 'campo', 
                                            'placeholder':'Nome da Empresa'}),
            'cidade': forms.Select(attrs={ 'class': 'campo'}),
            'pacote': forms.Select(attrs={ 'class': 'campo'}),
            'rua': forms.TextInput(attrs={ 'class': 'campo', 
                                            'placeholder':'Ex:Rua Adolfo John Terry'}),
            'bairro': forms.TextInput(attrs={ 'class': 'campo', 
                                            'placeholder':'Ex:Centro'}),
            
        }