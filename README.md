# WEB TESTES AGIBANK

## Webe tests AGIBANK ultilizando BDD testes com Python, Pytest e Selenium frameworks

## Proposta
  * Levantar ao menos dois dos cenários mais relevantes para a automação dos testes.


## Cenários:

* Pesquisa sentenca
  + Pesquisa de sentenca correta
    - Busca pelo artigo do texto no campo pesquisa
    - Resultado esperado pagina de resultado somente com artigo pesquisado

  + Pesquisa de sentenca incorreta
    - Busca por uma frase inválida no campo pesquisa
    - Resultado espera mensagem: "Lamentamos, mas nada foi encontrado para sua pesquisa"

## Ferrmaentas e Linguagem

* Python 3.8
* VSCode

## Passos para executar testes localmente

### Clonar o repositório do Git

```bash
#!/bin/bash
git clone https://gitlab.com/lznunes/web_test_blog_agibank.git
```

### Abrir VSCode no diretório do projeto

### Abrir o terminal prompt

### Configurar ambiente virtual com comandos abaixo

```bash
#!/bin/bash
  python3 -m venv .venv
```

```bash
#!/bin/bash
  source .venv/bin/activate
```

### Instalar dependências com comando abaixo

```bash
#!/bin/bash
 pip install -r requirements.txt
```

## Executar testes 

### Configuração para habilitar Browser no modo gráfico

#### Por padrão o modo gráfico está desabilitado editar o arquivo utils/webdriver.py

- Comentar a linha 9 colocando '#' no ínicio da linha

- Remover comentario da linha 10 apagando '#' no inicio da linha

- Salvar o arquivo

#### Executar teste com comando abaixo

```bash
#!/bin/bash
python -m pytest
```

## Executar teste

* Acessar: [Teste Web AGIBANK](https://github.com/lznunes/web_test_blog_agibank/actions/workflows/main.yml)
* Clicar no botão á direita da tecla "Run workflow" depois botão verde "Run workflow"

## Relatório

  * Acessar relatório dos testes:

  [Resultado dos testes](https://github.com/lznunes/web_test_blog_agibank/blob/main/reports/report.html)



## Referências

  * [Pytest Documentaion](https://docs.pytest.org)
  * [Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/)
