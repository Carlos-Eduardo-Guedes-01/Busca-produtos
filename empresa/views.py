from django.urls import reverse
from django.shortcuts import render
from .models import *
from .form import DadosForm
from django.contrib.auth.decorators import login_required
#Variáveis não comentadas já foram explicadas
# Método da página home
@login_required(login_url='accounts:login')
def template_cad(request):
    # Dicionário que para os templates
    data = {}
    # Caso tenha dados do formulário
    if request.method == 'POST':
        #Dados preenchidos pelo formulário
        form = DadosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['msg'] = 'Empresa cadastrada com sucesso!'
            data['class'] = 'alert-success'

        else:
            data['msg'] = 'Formato de imagem não suportado.'
            data['class'] = 'alert-danger'
    #Caso não tenha dados
    else:
        #variável do formulário
        form = DadosForm()
    #Para se tornar mais fácil de usar
    data['form'] = form
    #Este variável ficará na tag <title>
    data['title'] = 'Cadastro de empresas'
    data['link_form'] = '123'
    #Este dado é o que fica na barra verde
    data['titulo'] = 'Cadastro Empresa'
    return render(request, '../../empresa/templates/cad_em.html', data)

#Listagem de empresas ATIVAS
@login_required(login_url='accounts:login')
def lista_empresa(request):
    data={}
    data['title']='Lista de Empresas'
    #Gambiarra de verificação presente no arquivo lista_empresa.html
    data['t1']='v'
    data['titulo']='Lista de Empresa'
    #Busca de empresas com status ativo e ordenado por nome_empresa
    data['empresas']=Empresa.objects.filter(status=1).order_by('nome_empresa')
    #Variável de mensagem da janela modal
    data['msn']='desativar'
    #Texto do botão da janela modal
    data['btn']='Desativar'
    return render(request,'../../empresa/templates/lista_empresa.html',data)
# Método que chama template de alterar dados da empresa que recebe o id
# como parâmetro
# Direciona a templates/editar_dados.html
@login_required(login_url='accounts:login')
def alterar_dados(request, id):
    data={}
    #Buscando dados atuais da empresa
    data['empresa']=Empresa.objects.get(id=id)
    #Busca por todos os tipos de empresas para a tag select
    data['pacotes']=Pacote.objects.all()
    #Buscando as cidades para a tag select
    data['cidades']=Cidade.objects.all()
    data['title']='Editando Empresas'
    return render(request,'../../empresa/templates/editar_dados.html',data)
# Método que faz o update dos dados
@login_required(login_url='accounts:login')
def alterando(request):
    data={}
    # Recebendo dados do formulário
    nome=request.POST.get('nome_empresa')
    cidade=request.POST.get('cidade')
    rua=request.POST.get('rua')
    bairro=request.POST.get('bairro')
    id=request.POST.get('id')
    data['title']='Editando Empresas'
    # Buscando os dados da empresa para filtragem
    data['empresa']=Empresa.objects.get(id=id)
    # Efetivando alterações
    emp=Empresa.objects.filter(id=id).update(nome_empresa=nome,cidade=cidade,rua=rua,bairro=bairro)
    # Verificando se alteração funcionou ou não
    if(emp):
        data['msg'] = 'Empresa editada com sucesso!'
        data['class'] = 'alert-success'
    else:
        data['class'] = 'alert-danger'
        data['msg']='Falha ao alterar dados!'
    data['cidades']=Cidade.objects.all()
    data['empresa']=Empresa.objects.get(id=id)
    return render(request,'../../empresa/templates/editar_dados.html',data)
# Buscando template das empresas desativadas
@login_required(login_url='accounts:login')
def empresa_desact(request):
    data={}
    data['t2']='v'
    data['msn']='ativar'
    data['btn']='Ativar'
    data['title']='Empresas desativadas'
    data['titulo']='Empresas desativadas'
    data['empresas']=Empresa.objects.filter(status=0).order_by('nome_empresa')
    return render(request,'../../empresa/templates/lista_empresa.html',data)
# Alteração dos status das empresas
# Esta função funciona tanto pra ativar quanto para desativar empresas
@login_required(login_url='accounts:login')
def upd_status(request):
    data={}
    # Recebendo id
    id=request.POST.get('id')
    # Buscando os dados da empresa pelo id
    empresa=Empresa.objects.get(id=id)
    # Verificando qual o status recebido para fazer alterações
    # Caso seja ativado
    if(empresa.status==1):
        # Aqui temos muitas gambiarras
        data['title']='Lista de Empresas'
        data['titulo']='Lista de Empresa'
        data['t1']='v'
        data['msn']='desativar'
        data['btn']='Desativar'
        data['empresas']=Empresa.objects.filter(status=1).order_by('nome_empresa')
        emp=Empresa.objects.filter(id=id).update(status=0)
        if(emp):
            data['msg'] = 'Empresa Desativada!'
            data['class'] = 'alert-success'
        else:
            data['class'] = 'alert-danger'
            data['msg']='Algum erro aconteceu, por favor tente novamente!'
    # Caso o status seja desativado
    elif(empresa.status==0):
        data['title']='Empresas Desativadas'
        data['nome']='Voltar'
        data['titulo']='Empresas  desativadas'
        data['t2']='v'
        data['msn']='ativar'
        data['btn']='Ativar'
        data['empresas']=Empresa.objects.filter(status=0).order_by('nome_empresa')
        emp=Empresa.objects.filter(id=id).update(status=1)
        # Caso tenha sucesso ao atualizar o status
        if(emp):
            data['msg'] = 'Empresa Reativada!'
            data['class'] = 'alert-success'
        # Caso tenha algum problema
        else:
            data['class'] = 'alert-danger'
            data['msg']='Algum erro aconteceu, por favor tente novamente!'
    return render(request,'../../empresa/templates/lista_empresa.html',data)
