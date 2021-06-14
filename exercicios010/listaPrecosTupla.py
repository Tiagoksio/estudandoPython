# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular;
produtos = ('Celular', 980.99, 'TV', 1200.99, 'Máscara', 1.99, 'Livros', 34.90)
print(f'{"=" * 50}\n{"="}{" TABELA DE PRODUTOS ":^48}{"="}\n{"=" * 50}')
for item in produtos:
    if produtos.index(item) % 2 == 0:
        print(f'= {item:.<35} R${produtos[produtos.index(item) + 1]:>8} =')
print(f'{"=" * 50}\n{"="}{" FIM DA TABELA ":^48}{"="}\n{"=" * 50}')