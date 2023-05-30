def calculate(person):
    calculate_imc(person)
    describe_imc(person)

def calculate_imc(person):
    person.imc = person.weight / person.height ** 2

def describe_imc(person):
    person.description = 'Obesidade'

    if person.imc < 18.5: person.description = 'Magreza'
    elif person.imc < 24.9: person.description = 'Normal'
    elif person.imc < 30: person.description = 'Sobrepeso'