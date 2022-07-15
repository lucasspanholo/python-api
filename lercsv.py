import csv

with open('csv1.csv') as arquivo:
  cont = csv.reader(arquivo, delimiter=',')
  linhas = 0
  for line in cont:
    if linhas == 0:
      print(f'colunas: {" ".join(line)}')
      linhas += 1
    else:
      print(f'\tID: {line[0]}, CPF: {line[1]}, Matricula: {line[2]}. ')
      linhas += 1
