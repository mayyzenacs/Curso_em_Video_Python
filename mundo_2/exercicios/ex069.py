#
cont = 0
fem = 0
masc = 0
ida = 0
while True:
    SEXO_MASCULINO = ('homem', 'm', 'masculino', 'h')
    SEXO_FEMININO = ('mulher', 'feminino', 'f')
    idade = int(input('Digite sua idade '))
    sexo = ' '
    while sexo not in SEXO_FEMININO and SEXO_MASCULINO:
        sexo = input('Digite seu sexo ').lower().strip()

    cont += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = input('Voce quer continuar S/N? ').upper()
    if sexo in SEXO_MASCULINO:
        masc += 1
    elif idade >= 18:
        ida += 1
    elif sexo in SEXO_FEMININO and idade<20:
        fem += 1
    else:
        print('resposta invalida')
    if pergunta == 'N':
        print('Programa encerrado.')
        print(f'Voce digitou {cont} pessoas. {masc} sao homens, {ida} tem 18 anos e {fem} mulheres tem menos de 20 anos')
        break