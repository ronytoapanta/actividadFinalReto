


# CONSULTA Y EXTRACIÓN DE DATOS DE YAHOO FINANCE DONDE SE EXTRAE EL VALOR EN LA BOLSA DE LAS 4 EMPRESAS MÁS COTIZADAS
# ALMACENANDO LA INFORMACIÓN EN VARIABLES Y MOSTRANDOLA POR EL METODO GET EN EL SERVIDOR

# RONY TOAPANTA 

from flask import Flask
from bs4 import BeautifulSoup
import requests
 	
app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
	return "Servidor fuera de servicio, lamentamos los inconvenientes"

@app.route('/', methods=['GET'])
def index():
	#Link desde yahoo finance
	microsoft='https://finance.yahoo.com/quote/MSFT?p=MSFT'
	apple ='https://finance.yahoo.com/quote/AAPL?p=AAPL'
	cisco='https://finance.yahoo.com/quote/CSCO?p=CSCO'
	oracle='https://finance.yahoo.com/quote/ORCL?p=ORCL'

	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

	
	respmicrosoft=requests.get(microsoft,headers=headers)
	
	respapple=requests.get(apple,headers=headers)
	
	respcisco=requests.get(cisco,headers=headers)
	
	resporacle=requests.get(oracle,headers=headers)

	stgmicrosfot=BeautifulSoup(respmicrosoft.text,'lxml')
	
	stgapple=BeautifulSoup(respapple.text,'lxml')
	
	stgcisco=BeautifulSoup(respcisco.text,'lxml')
	
	stgoracle=BeautifulSoup(resporacle.text,'lxml')
	
	empmicrosoft=stgmicrosfot.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	
	empapple=stgapple.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	
	empcisco=stgcisco.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	
	emporacle=stgoracle.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	
	return 'COTIZACIÓN EN BOLSA DE EMPRESAS TECNOLÓGICAS: ' + 'EMPRESA MICROSOFT' +empmicrosoft +' EMPRESA APPLE $'+empapple+' EMPRESA CISCO $'+empcisco+ ' EMPRESA ORACLE $'+emporacle
	
	

if __name__ == '__main__':
	app.run(port = PORT,debug = DEBUG)
