import requests

# Defina a URL da API
url = "http://servicodados.ibge.gov.br/api/v3/noticias/"

# Parâmetros da requisição
params = {
    'tipo': 'noticia',  # Pode ser 'noticia' ou 'release'
    'qtd': 3,  # Quantidade de notícias por página
    'page': 1,  # Página desejada
    'de': '01-01-2009',  # Data mínima de publicação
    'ate': '12-30-2023',  # Data máxima de publicação
    'introsize': 255,  # Tamanho máximo do texto de introdução
    'destaque': 1,  # Se deve vir ordenado por destaque (1 = sim, 0 = não)
    'busca': '',  # Termo de busca (se necessário)
    'idproduto': 'petrobras'  # Identificador do produto ou pesquisa (se necessário)
}

# Fazendo a requisição GET
response = requests.get(url, params=params)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    # Converte a resposta para JSON
    noticias = response.json()
    
    # Exibe o resultado
    for noticia in noticias['items']:
        print(f"Título: {noticia['titulo']}")
        print(f"Introdução: {noticia['introducao']}")
        print(f"Data de publicação: {noticia['data_publicacao']}")
        print(f"Link: {noticia['link']}")
        print("-" * 50)
else:
    print(f"Erro na requisição: {response.status_code}")