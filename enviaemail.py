#!/usr/bin/python3

import mimetypes, time, os, smtplib, pymysql
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def listamail():
  

  db = pymysql.connect("SERVER", "NAME", "SENHA", "BD")

  cursor = db.cursor()

  cursor.execute("select email from contacts where email = 'nglauzer@gmail.com'")

  data = cursor.fetchall()

  produtodia = input("Digite o nome do produto do dia: ")
  fotoproduto = input("Digite o endereço de URL da imagem: ")
  resultadoprodutodia = "https://alidocesoficial.com/img/email/" + fotoproduto
  descricaoproduto = input("Digite a descrição do produto: ")
  tituloemail = input("Digite o título do e-mail: ")
  arq = open('email.html', 'r')
  texto = arq.read()
  replaceproduto = texto.replace("@@@produto@@@",produtodia)
  replacedescricao = replaceproduto.replace("@@@descricao@@@",descricaoproduto)
  HTML = replacedescricao.replace("@@@imagem@@@",resultadoprodutodia)

  for row in data:
    getmail = " ".join(str(x) for x in row)
    try:

      corpoemail = HTML

      print("INFO: E-mail para " + getmail + " enviado com sucesso")
      
      de = 'backup@andreyglauzer.com'
      para = [getmail]

      msg = MIMEMultipart()
      msg['From'] = de
      msg['To'] = ', '.join(para)
      msg['Subject'] = tituloemail

      # Corpo da mensagem
      msg.attach(MIMEText(corpoemail, 'html', 'utf-8'))

      raw = msg.as_string()

      smtp = smtplib.SMTP_SSL('smtp.zoho.com', 465)
      smtp.login('backup@andreyglauzer.com', 'SENHA')
      smtp.sendmail(de, para, raw)
      smtp.quit()

      time.sleep(60)
    except:
      print("ERROR: Não consegui enviar email para " + getmail + " na próxima quem sabe!")
      pass

listamail()