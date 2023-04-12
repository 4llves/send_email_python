<h1 align="center">
  🤖send_email_python
</h1>

<p></p>
## 💻 Sobre o projeto

Onde trabalho faço muito envio de emails com diversos anexos e vários remetentes, da necessidade de agilizar esse trabalho tive a ideia de criar esse projeto ^^

## 🚀 Como executar o projeto

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas: [Git](https://git-scm.com) e [Python](https://www.python.org/). Além disto ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

#### 🧭 Rodando a aplicação

1. Clone este repositório

  ```bash
  git clone https://github.com/4llves/send_email_python
  ```

2. Acesse a pasta do projeto no seu *vscode*
	
3. Instale as libs

  ```bash
  pip install pandas
  ```
  
  
  ```bash
  pip install openpyxl
  ```
  
  
  ```bash
  pip install python-decouple
  ```

4. Gerar a key do gmail que será usada no .env

  <img alt="Generate Key" src="https://github.com/4llves/send_email_python/blob/main/.github/generate_key.gif" />

5. Preencha a planilha com os dados necessários.

6. Execute a aplicação 

windows: python .\send_email

linux: python send_email

#### 📌 Importante

- Crie um .env e use o a key gerada no item 4 acima e seu email, use o **.env.example** como modelo.

- Como o projeto ainda é novo e está em fase de testes aconselho enviar o email para si mesmo antes de testar enviar para outra pessoa ^^
