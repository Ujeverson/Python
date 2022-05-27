from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import time

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
url = "https://www.google.com.br/search?q=euro&sxsrf=ALiCzsaRS599iDcWNwoeV90enizKL9qb4A%3A1653657615921&source=hp&ei=D9CQYsuANpmp1sQP6t2soAw&iflsig=AJiK0e8AAAAAYpDeH1dG_oDtedxQpAstAcbUiAs00mcg&ved=0ahUKEwiLxJnW4v_3AhWZlJUCHeouC8QQ4dUDCAc&uact=5&oq=euro&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIECCMQJzIECCMQJzILCC4QgAQQsQMQ1AIyCAgAEIAEELEDMgsILhCABBCxAxDUAjILCAAQgAQQsQMQgwEyCwguEIAEELEDENQCMgUIABCABDIICAAQgAQQsQM6DgguEIAEELEDEMcBEKMCOhEILhCABBCxAxCDARDHARDRAzoICC4QgAQQsQNQAFiMBmC9EmgAcAB4AIABrwGIAYAEkgEDMC40mAEAoAEB&sclient=gws-wiz"

pagina = requests.get(url, headers=header)

soup = BeautifulSoup(pagina.content, 'html.parser')

atributos = {'class':'DFlfde SwHCTb'}
euro = soup.find_all("span", attrs= atributos)[0]
data = soup.find_all("div", class_="k0Rg6d hqAUc")[0]

valor_euro = euro.text
dia = data.text[0:9]
hora_pesquisa = time.strftime('%H:%M:%S', time.localtime())

print("\n",valor_euro, "\n")
print("\n",euro['data-value'], "\n")
print("\n",dia, "\n")
print("\n",hora_pesquisa, "\n")
