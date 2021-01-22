# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função

def notes(* schoolNotes, sit=False):
    """
    # EN-US:
    → Function to analyze notes and situations of several students.
    :param schoolNotes: One or more grades from students (accepts several).
    :param sit: Optional value, indicating whether or not to add the situation.
    :return: Dictionary with various information about the class situation.

    # PT-BR:
    → Função para analisar notas e situações de vários alunos.
    :param schoolNotes: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """

    notesDict = {}
    notesDict['total'] = len(schoolNotes)
    notesDict['bigger'] = max(schoolNotes)
    notesDict['smaller'] = min(schoolNotes)
    notesDict['average'] = sum(schoolNotes) / len(schoolNotes)
    if sit:
        if notesDict['average'] >= 7:
            notesDict['situation'] = 'BOA'
        elif notesDict['average'] >= 5:
            notesDict['situation'] = 'RAZOÁVEL'
        else:
            notesDict['situation'] = 'RUIM'

    return notesDict


help(notes)
print()

n = notes(9, 10, 5.5, 2.5, 8.5)
print(n)
print()

n = notes(9, 10, 5.5, 2.5, 8.5, sit=True)
print(n)
