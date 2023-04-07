import pandas as pd

# criar um dataframe com alguns dados
data = {'Nome': ['João', 'Maria', 'José'],
        'Idade': [30, 25, 40],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']}
df = pd.DataFrame(data)

# converter o dataframe em HTML
html_table = df.to_html()

# criar o arquivo HTML e salvar o código
with open('D:/vscode/Projeto Web/tabela.html', 'w') as f:
    f.write(html_table)

# imprimir o código HTML
print(html_table)
