# Faça um programa que leia o sexo de uma pessoa, mas que só aceite 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto;
sexo = ['M', 'F']
m_ou_f = ''
while not m_ou_f in sexo:
    m_ou_f = str(input('Informe seu gênero[M/F]: ')).strip().upper()
    if not m_ou_f in sexo:
        print('Gênero inválido, tente novamente!')
print(f'Gênero "{m_ou_f}" cadastrado.')   
