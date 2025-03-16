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
### Cliente:

1. **Pagina 1: Pagina inicial com Carousel dos produtos:**
<img src="https://github.com/Carlos-Eduardo-Guedes-01/Busca-Produtos/blob/carlos/imagens-do-projeto/01.png?raw=true" alt="Clique aqui" width="1000">
