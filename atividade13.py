from datetime import date
pessoa = {
    'nome': 'Hellen Jasmine',
    'sobrenome':'Pessoa Ferreira',
    'idade': date.today().year - 2005,
    'endereco' : [
        {
        'rua' : 'Bom Jesus',
        'cidade' : 'Brejo',
        'bairro' : 'Palestina',

    }
    ],

}
nome = pessoa.pop('nome')
print(nome)
print(pessoa.get("nome", "Évilli"))
print(pessoa.get("Hobby", "Não existe"))
last_key = pessoa.popitem()
print(last_key)
pessoa.update({
    'hobby': "ciclismo"
})

print(pessoa)