# Sistema de Busca de Produtos

Este projeto é um sistema web desenvolvido em **Django**, com frontend em **HTML, CSS e JavaScript**, utilizando **SQLite3** como banco de dados. O objetivo do sistema é permitir que os clientes busquem produtos disponíveis nos estabelecimentos cadastrados, filtrando por nome ou seção.

## 📌 Tecnologias Utilizadas
- **Django** (Backend e gerenciamento de dados)
- **HTML, CSS e JavaScript** (Frontend)
- **SQLite3** (Banco de dados)
- **MediaQuery** (Responsividade para dispositivos móveis)

---

## 📋 Funcionalidades

### 🔍 Parte do Cliente
- **Página Inicial com Carrossel**: Destaques e promoções dos produtos.
- **Busca de Produtos**: Permite pesquisar produtos por nome.
- **Filtros por Seção**: Facilita a navegação pelos produtos disponíveis.
- **Exibição Agrupada**: Os produtos são agrupados de forma organizada para melhor visualização.

### ⚙️ Parte do Administrador
- **Gerenciamento de Produtos**: Cadastro, edição e exclusão de produtos.
- **Gerenciamento de Seções**: Criação e organização das categorias de produtos.
- **Cadastro de Tipos de Pacotes**: Define embalagens e formatos disponíveis.
- **Gestão de Estabelecimentos**: Administração dos locais que disponibilizam os produtos.

---

## 📸 Imagens do Sistema
(Inserir capturas de tela das principais funcionalidades)

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório**:
```bash
git clone https://github.com/Carlos-Eduardo-Guedes-01/Busca-produtos
```
2. **Acesse a pasta do projeto:**
```bash
cd Busca-produtos
```
3. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```
4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```
5. **Realize as migrações do banco de dados:**
```bash
python manage.py migrate
```
6. **Crie um superusuário para acessar a área administrativa:**
```bash
python manage.py createsuperuser
```
7. **Inicie o servidor:**
```bash
python manage.py runserver
```
#
# IMAGENS DO PROJETO
<h1>Cliente:</h1>


1. **Pagina 1: Pagina inicial com Carousel dos produtos:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/01.png?raw=true" alt="Clique aqui" width="1000">

2. **Pagina 2: Página de contato:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/02.png?raw=true">

3. **Pagina 3: Página de sobre:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/03.png?raw=true">

4. **Pagina 4: Página de filtro por seção:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/04.png?raw=true">

5. **Pagina 5: Página de busca por nome do produto:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/05.png?raw=true">

#
<h1>Administrador:</h1>
A página de administrador tem um link específico e um login nesse link por razões de segurança.

1. **Pagina 1: Página de login:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/adm/01.png?raw=true">

2. **Pagina 2: Página inicial do Administrador onde tem todas as funções de cadastro e caminho par alterações:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/adm/02.png?raw=true">

3. **Pagina 3: Página que mostra as empresas e funções de editar e remove-las:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/adm/03.png?raw=true">

4. **Pagina 4: Página que mostra os pacotes de cadastro de produtos e opções de editá-los, este pacote limita a quantidade de produtos e a quantidade no carousel da página inicial:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/adm/04.png?raw=true">

5. **Pagina 5: Página de listagem dos produtos, assim como os estabelecimentos, tem as opções de editar e remover:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/adm/05.png?raw=true">

6. **Pagina 6: Página de cadastro de outros administradores:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/adm/06.png?raw=true">

7. **Pagina 7: Página de cadastro de empresas:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/adm/07.png?raw=true">

8. **Pagina 8: Cadastro de Produtoes:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/adm/08.png?raw=true">

9. **Pagina 9: Página de cadastro de pacotes:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/adm/09.png?raw=true">



