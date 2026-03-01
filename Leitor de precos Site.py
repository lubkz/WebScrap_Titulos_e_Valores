import requests
from bs4 import BeautifulSoup

print("INICIANDO...")

url = 'https://books.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    print("Site carregado")
else:
    print("Erro")

soup = BeautifulSoup(response.text, "html.parser")

livros = soup.find_all("article", class_= "product_pod")

for livro in livros:
    titulo = livro.find("h3").find("a")["title"]
    preco = livro.find("p", class_= "price_color").text

    print(f"Titulo: {titulo}, Preço: {preco}")
