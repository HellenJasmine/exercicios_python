perguntas = [
    {
        'pergunta':'Quanto é 2 + 2? ',
        'opções' : ['1','3','4','5'],
        'resposta' : '4',

    },
    {
        'pergunta':'Quanto é 5 * 5? ',
        'opções' : ['25','55','10','51'],
        'resposta' : '25',
    },
    {
        'pergunta':'Quanto é 10/2? ',
        'opções' : ['4','5', '2', '1'],
        'resposta' : '5',
    }

]


acertos = erros = 0
for i in perguntas:
    print("Pergunta: ",i['pergunta'])
    for index, opc in enumerate(i['opções']):
        print(f"{index}) {opc}")
    resposta = int(input("Digite sua resposta: "))
    if i['opções'][resposta] == i['resposta']:
        acertos += 1
        print("voce acertou")
    else:
        erros += 1
        print("Resposta errada!")
    # if resposta == int(i['resposta']):

print("Parabéns acertou todas" if erros == 0 else f"Você acertou {acertos} e errou {erros}")