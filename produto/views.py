import os
from django.shortcuts import render,redirect
from django.templatetags.static import static
import io
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from datetime import date
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle,Image
from core import settings
from produto.forms import ProdutoForm,PrecoForm
from .models import *
from django.shortcuts import get_object_or_404
import sys
sys.path.append("")
from produto.models import *
from empresa.models import *
from accounts.models import *
from .models import preco,secao
from django.contrib.auth.decorators import login_required
import magic
from PIL import Image as PILImage
from .models import *
from django.db.models import Max, Min
import unicodedata

def trata_busca(busca):
    """
    Função para tratar a string de busca.
    - Remove acentuação
    - Converte para minúsculas
    """
    # Remover acentuação
    busca = ''.join(c for c in unicodedata.normalize('NFD', busca)
                    if unicodedata.category(c) != 'Mn')

    # Converter para minúsculas
    busca = busca.lower()

    return busca


@login_required(login_url='accounts:login')
def cad_prod(request):
    data = {}
    data['title'] = 'Cadastro de Produtos'

    if request.POST:
        data['form'] = ProdutoForm(request.POST, request.FILES)
        form = data['form']
        if form.is_valid():
            nome = Empresa.objects.get(id=request.POST.get('empresa'))
            quant = nome.quant_prod
            r1 = Pacote.objects.get(nome=nome.pacote)
            pac = r1.quant_prod
            if quant < pac:
                quant += 1
                Empresa.objects.filter(nome_empresa=nome).update(quant_prod=quant)
                produto = form.save(commit=False)
                img = request.FILES.get('imagem')

                # Verificação de tipo de imagem usando o Pillow
                try:
                    if img:
                        # Verifica se a imagem é do tipo correto
                        img = PILImage.open(img)
                        img.verify()  # Verifica se o arquivo é uma imagem válida
                        if img.format not in ['JPEG', 'PNG']:
                            data['msg'] = 'Formato de imagem não suportado.'
                            data['class'] = 'alert-danger'
                        else:
                            form.save()
                            data['msg'] = 'Produto Cadastrado com Sucesso!'
                            data['class'] = 'alert-success'
                    else:
                        data['msg'] = 'Nenhuma imagem foi enviada.'
                        data['class'] = 'alert-danger'

                except Exception as e:
                    data['msg'] = f'Erro ao verificar imagem: {str(e)}'
                    data['class'] = 'alert-danger'
            else:
                data['msg'] = 'Limite do pacote atingido.'
                data['class'] = 'alert-danger'
        else:
            data['msg'] = 'Formulário inválido.'
            data['class'] = 'alert-danger'

    else:
        data['form'] = ProdutoForm()
        data['formpreco'] = PrecoForm()

    data['link_form'] = "{% url 'accounts:index' %}"
    data['nome'] = 'Voltar'
    data['titulo'] = 'Cadastro Produtos'

    return render(request, '../../produto/templates/cadastro_prod.html', data)
@login_required(login_url='accounts:login')
def cad_preco(request):
    data={}
    data['title']='Cadastro de Produtos'
    if(request.POST):
        data['formpreco']=PrecoForm(request.POST)
        precos=request.POST.get('valor')
        precos=preco.objects.filter(valor=precos)
        if(len(precos)==0):
            teste=data['formpreco'].save()
            if(teste):
                data['msg'] = 'Preço Cadastrado com Sucesso!'
                data['class'] = 'alert-success'''
            else:
                data['msg'] = 'Formulário inválido.'
                data['class'] = 'alert-danger'''
        elif(len(precos)>0):
            data['msg'] = 'Este preço já existe.'
            data['class'] = 'alert-danger'''

    data['form']=ProdutoForm()
    data['formpreco']=PrecoForm()
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro Produtos'
    return render(request,'../../produto/templates/cadastro_prod.html',data)


def busca_prod(request):
    data = {}
    data['title'] = 'Cadastro de empresas'
    data['link_form'] = '123'
    data['title'] = 'Pesquisa'
    data['titulo'] = 'Cadastro Empresa'

    busca_bruta = request.GET.get('search', '')
    busca_tratada = trata_busca(busca_bruta)
    # Filtra os produtos com base na busca
    '''data['produtos'] = produtos.objects.raw(
        "SELECT produto.id, produto.nome_produto, secao.nome_secao, empresa.nome_empresa, "
        "MAX(preco.valor) AS maior_preco, MIN(preco.valor) AS menor_preco, produto.imagem "
        "FROM produto_produtos AS produto "
        "INNER JOIN produto_secao AS secao ON produto.secao_id = secao.id "
        "INNER JOIN empresa_empresa AS empresa ON produto.empresa_id = empresa.id "
        "INNER JOIN produto_preco AS preco ON produto.preco_id = preco.id "
        "WHERE produto.status = 1 "
        "GROUP BY produto.nome_produto"
    )'''
    data['produtos'] = produtos.objects.filter(nome_produto__icontains=busca_tratada).raw("SELECT produto.id, produto.nome_produto, secao.nome_secao, empresa.nome_empresa, "
        "MAX(preco.valor) AS maior_preco, MIN(preco.valor) AS menor_preco, produto.imagem "
        "FROM produto_produtos AS produto "
        "INNER JOIN produto_secao AS secao ON produto.secao_id = secao.id "
        "INNER JOIN empresa_empresa AS empresa ON produto.empresa_id = empresa.id "
        "INNER JOIN produto_preco AS preco ON produto.preco_id = preco.id "
        "WHERE produto.status = 1 "
        "GROUP BY produto.nome_produto")
    data['busca'] = busca_bruta
    return render(request, '../../produto/templates/lista_produtos.html', data)
def secoes(request, v):
    data = {}
    data['title'] = 'Cadastro de empresas'
    data['link_form'] = '123'
    data['title'] = 'Pesquisa'
    data['titulo'] = 'Cadastro Empresa'
    busca = secao.objects.get(nome_secao=v)
    print(busca)
    data['produtos'] = produtos.objects.raw(
        "SELECT produto.id, produto.nome_produto, secao.nome_secao, empresa.nome_empresa, "
        "MAX(preco.valor) AS maior_preco, MIN(preco.valor) AS menor_preco, produto.imagem "
        "FROM produto_produtos AS produto "
        "INNER JOIN produto_secao AS secao ON produto.secao_id = secao.id "
        "INNER JOIN empresa_empresa AS empresa ON produto.empresa_id = empresa.id "
        "INNER JOIN produto_preco AS preco ON produto.preco_id = preco.id "
        "WHERE secao.nome_secao LIKE %s AND produto.status = 1 "
        "GROUP BY produto.nome_produto",
        ['%' + busca.nome_secao + '%']
    )
    
    return render(request, '../../produto/templates/lista_produtos.html', data)

def listagem(request):
    data={}
    data['adm']='ok'
    data['btn']='Desativar'
    data['msn']='desativar'
    data['t1']='s'
    data['produtos']=produtos.objects.filter(status=1).order_by('nome_produto')
    return render(request, '../../produto/templates/lista_adm.html',data)
@login_required(login_url='accounts:login')
def upd_status(request):
    data={}
    data['btn']='Desativar'
    id=request.POST.get('id')
    desct=produtos.objects.filter(id=id).update(status=0)
    
    return redirect('produto:lista-produtos')
@login_required(login_url='accounts:login')
def template_altera(request,id):
    data={}
    query=produtos.objects.get(id=id)
    data['form']=ProdutoForm(instance=query)
    data['formpreco']=PrecoForm()
    if(request.POST):
        form=ProdutoForm(request.POST)
        if(form.is_valid()):
            sv=form.save()
            if(sv):
                data['msg'] = 'Produto Alterado com sucesso!'
                data['class'] = 'alert-success'''
            else:
                data['msg'] = 'Produto Não Alterado.'
                data['class'] = 'alert-danger'''
        elif(not form.is_valid()):
            data['msg'] = "O produto não foi alterado \n Formulário inválido ." 
            data['class'] = 'alert-danger'''
    data['id']=id
    return render(request,'../../produto/templates/edita_prod.html',data)
def detalhes(request,titulo,id):
    data = {}
    data['title'] = 'Cadastro de empresas'
    produto = get_object_or_404(produtos, pk=id)
    rel = relatorio(produto=produto, data_busca=date.today())
    rel.save()
    data['link_form'] = '123'
    data['title'] = 'Pesquisa'
    data['titulo'] = 'Cadastro Empresa'
    data['empresas']=produtos.objects.filter(nome_produto=titulo)
    data['produto']=get_object_or_404(produtos,pk=id)
    return render(request,'detalhe_prod.html',data)
def generate_report(request):
     # Cria um file-like buffer para receber os dados do PDF
     
    buffer = io.BytesIO()
    mes=request.POST.get('mes')
    ano=request.POST.get('ano')
    produtos = relatorio.objects.raw(
    "SELECT relatorio.id, relatorio.produto_id, COUNT(relatorio.produto_id) AS total "
    "FROM produto_relatorio AS relatorio, produto_produtos AS produto "
    "WHERE substr(relatorio.data_busca, 6, 2) = %s "
    "AND substr(relatorio.data_busca, 1, 4) = %s "
    "AND relatorio.produto_id = produto.id "
    "GROUP BY relatorio.produto_id ORDER BY total DESC",
    [mes, ano]
)

    # Cria o objeto PDF usando o buffer como "arquivo"
    doc = SimpleDocTemplate(buffer, pagesize=letter,topMargin=20)

    # Lista para armazenar os elementos do relatório
    elements = []
    # Obtém o estilo de amostra para os estilos de parágrafo
    styles = getSampleStyleSheet()
    logo_path = os.path.join(settings.BASE_DIR, 'accounts', 'static', 'img', 'logo.png')

    # Verifica se o arquivo da logo existe
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=100, height=100)
        elements.append(logo)
    else:
        pass
    # Adiciona um título ao relatório
    title_text = "Relatório de Produtos RBC"
    title = Paragraph("<b>{}</b>".format(title_text), styles['Title'])
    elements.append(title)

    # Adiciona um parágrafo de introdução

    # Adiciona uma tabela ao relatório
    data = [['Produto', 'Quantidade']]
    
    for produto in produtos:
        produto_data = [produto.produto.nome_produto, produto.total]
        data.append(produto_data)

    column_widths = [300, 100, 100]  # Defina os valores desejados para a largura de cada coluna

    # Cria a tabela e define as larguras das colunas
    table = Table(data, colWidths=column_widths)

    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('FONTSIZE', (0, 0), (-1, 0), 14),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('ALIGN', (-1, 1), (-1, -1), 'CENTER'),
                               ]))
    elements.append(table)

    # Gera o relatório
    doc.build(elements)

    # Coloca o ponteiro do buffer no início
    buffer.seek(0)

    # Cria a resposta HTTP com o conteúdo do arquivo PDF
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'

    return response