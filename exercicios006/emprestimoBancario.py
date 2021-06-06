# Escreva um programa para aprovar o empréstimo bancários de uma casa. O programa vai perguntar o **valor da casa**, o **salário** do comprador e em **quantos anos** ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder **30%** do salário ou então o emprestimo será negado;
valCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o valor do salário, utilizando "." no lugar de ",": '))
prazo = int(input('Informe em quantos anos pretende concluir o pagamento: '))
mensalidade = valCasa / (prazo * 12)
print('O pagamento será em {}x de R${}'.format(prazo * 12, mensalidade) if mensalidade <= salario * 0.3 else 'O emprestimo não foi aprovado.')