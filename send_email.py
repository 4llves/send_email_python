import glob
import os
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from decouple import config

# Credenciais de login
EMAIL = config('EMAIL', default='')
PASSWORD = config('PASSWORD', default='')

# Configuração do servidor SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Lê o arquivo excel que contém os diretórios e os e-mails correspondentes
diretorios_df = pd.read_excel('LIST.xlsx')

# Cria uma lista contendo o e-mail e os diretórios correspondentes
destinatarios = []
for index, row in diretorios_df.iterrows():
    diretorio = row['DIRETORIES']
    email = row['EMAIL']
    titulo_do_email = row['TITULO']
    corpo_do_email = row['CORPO']    
    destinatarios.append({
        'email': email,
        'diretorio': diretorio,
        'titulo': titulo_do_email,
        'corpo': corpo_do_email
    })

# Percorre cada destinatário na lista e envia os arquivos correspondentes
for destinatario in destinatarios:
    arquivos = []
    diretorio = destinatario['diretorio']
    email = destinatario['email']
    titulo = destinatario['titulo']
    corpo = destinatario['corpo']    
    # Usa glob para encontrar todos os arquivos no diretório que correspondem ao padrão *.pdf
    files = glob.glob(f"{diretorio}\\*.pdf")
    arquivos.extend(files)

    # Cria o DataFrame contendo o nome do arquivo e o diretório
    df = pd.DataFrame({'arquivo': arquivos, 'diretorio': [diretorio] * len(arquivos)})

    # Cria o objeto para a mensagem de e-mail
    msg = MIMEMultipart()

    # Adiciona o endereço do remetente e destinatário
    msg['From'] = EMAIL
    msg['To'] = email

    # Adiciona o assunto da mensagem
    msg['Subject'] = titulo

    # Adiciona o corpo da mensagem
    body = corpo
    msg.attach(MIMEText(body, 'plain'))        

    # Percorre cada arquivo encontrado no DataFrame e adiciona como anexo
    for index, row in df.iterrows():
        # Define o caminho completo do arquivo
        file_path = os.path.join(row['diretorio'], row['arquivo'])

        # Abre o arquivo em modo binário
        with open(file_path, 'rb') as attachment:
            # Cria um objeto MIME para o arquivo
            att = MIMEBase('application', 'octet-stream')
            att.set_payload(attachment.read())
            encoders.encode_base64(att)
            #att.add_header('Content-Disposition', f'attachment; filename="{row["arquivo"]}"')
            att.add_header('Content-Disposition', f'attachment; filename="{row["arquivo"].split(os.path.sep)[-1]}"')
            msg.attach(att)

    # Envia a mensagem de e-mail
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, email, msg.as_string())
    server.quit()