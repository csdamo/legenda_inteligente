# Legenda Inteligente

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=status&message=em%20desenvolvimento&color=GREEN&style=flat)

Proposta de criação de uma legenda inteligente para uma exposição virtual, utilizando biblioteca openai

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **legenda_inteligente**
| :label: Tecnologias | python, chatgpt
| :fire: Desafio     | trabalho da disciplaina de Tópicos em Tecnologia do Curso de Análise e Desenvolvimento de Sistemas

![image](https://user-images.githubusercontent.com/64370426/230224248-ed2298f0-96c8-4311-b712-0100e8c507ab.png#vitrinedev)


## Sobre o Projeto

O projeto **legenda_inteligente**, foi um trabalho desenvolvido na disciplina de Tópicos em Tecnologia, do curso de Análise e Desenvolvimento de Sistemas, que teve como proposta fazer pesquisa e teste de uso sobre a tecnologia desenvolvida pela OpenAI, ChatGPT.


## Funcionalidades desenvolvidas
Front com um input para que o usuário faça perguntas sobre a obra exposta.

## Principais tecnologias utilizadas

![Python](https://user-images.githubusercontent.com/64370426/220479830-4eadb646-5a5f-4e98-822f-f08531868fcf.png)   


## Como instalar o projeto na sua máquina:

### Requisitos:
* Instalação do Python (a partir da versão 3.9)
> https://www.python.org/
* Instalação do Git
> https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git

### Clonando projeto para máquina local:

* Criar repositório onde será mantido o projeto e posicione-se, via terminal, dentro dele. 
* Rode o comando
```
git clone https://github.com/csdamo/legenda_inteligente.git
```

### Criando ambiente virtual de desenvolvimento:

* No prompt de comando, executar o comando
```
pip install virtualenv
```

* Pelo prompt, vá até o diretório do projeto e execute o comando a seguir. Será criada uma pasta dentro do repositório com o nome "venv"
```
virtualenv venv
``` 
* Ative o ambiente virtual de desenvolvimento: ainda no prompt de comando (dentro do repositório do projeto) execute o comando
```
venv/Scripts/activate 
```
(Windows) 
```
source venv/bin/activate
```
(Linux) 

* Para você saber se o ambiente virtual foi ativado, perceba se antes do caminho do seu diretório, aparece o nome do ambiente entre parênteses. 
> Ex.: (venv) C:\Users\seunome\desenv\django_alura_space>

### Instalando bibliotecas

* Dentro do ambiente virtual, para instalar as bibliotecas na versão correta para o projeto , rodar o comando
```
pip install -r requirements.txt
```
