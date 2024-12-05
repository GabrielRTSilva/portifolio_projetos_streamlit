#Irao existir 3 classes que representarao conjunto de dados do dataframe
#o primeiro objeto sera a estado = [cod unidade federativa, cod regiao geografica, cod instituicao]
#o segundo objeto sera o das instituicoes = [cod instituicao, nome da instituicao, cod regiao geografica, cod unid federativa, cod do curso]
# o terceiro objeto sera o dos cursos = [cod instituicao, nome da instituicao, cod do curso, nome do curso, grau academico, modalidade de ensino, nome da grande area do curso, ano de ingreso, ano de referencia, *quantidade de ingressantes, quantidade de concluintes, quantidade de desistencias]
## havera um outro objeto melhor descrito futuramente que contemplara os dados para analises (estatistica, descritivas e preditivas)

#Objetos testes
class teste_estado():
  def __init__(self, nome, universidades, cod_estado, ranking):
    self.nome = nome
    self.universidades = universidades
    self.cod_estado = cod_estado
    self.ranking = ranking

class teste_universidade():
  def __init__(self, cod_univ, nome, cod_reg, cod_cursos):
    self.cod_univ = cod_univ
    self.nome = nome
    self.cod_reg = cod_reg
    self.cod_curso = cod_cursos

class teste_cursos():
  def __init__(self, cod_curso, nome):
    self.cod_curso = cod_curso
    self.nome = nome

#Atributos testes

#Estado
estado_1 = teste_estado('Espirito Santo', ['-','UFES', 'Multivix', 'Unip', 'FAESA', 'UCL'], 15, 4)
estado_2 = teste_estado('Sao Paulo', ['-','Unicamp', 'USP', 'PUC-SP', 'ITA'], 10, 2)
estado_3 = teste_estado('Rio de Janeiro', ['-','UFRJ', 'PUC-RJ', 'IME'], 14, 3)
estado_4 = teste_estado('Washington', ['-','Harvard', 'MIT', 'Princetown University', 'Einstein University', 'Tesla Foundation', 'Carnegie Institute'], 6, 1)

lista_estados = [estado_1, estado_2, estado_3, estado_4]

map_estados = {'Espirito Santo': estado_1.cod_estado,
             'Sao Paulo': estado_2.cod_estado, 
             'Rio de Janeiro': estado_3.cod_estado,
             'Washington': estado_4.cod_estado}

#Universidades
universidade_1_1 = teste_universidade(1,'UFES', 1, [range(1,11)])
universidade_1_2 = teste_universidade(2,'Multivix', 1, [range(1,11,2)])
universidade_1_3 = teste_universidade(3,'FAESA', 1, [range(1,15,3)])

universidade_2_1 = teste_universidade(4,'Unicamp', 2, [range(1,11)])
universidade_2_2 = teste_universidade(5,'USP', 2, [range(1,11,2)])
universidade_2_3 = teste_universidade(6,'PUC-SP', 2, [range(1,15,3)])

universidade_3_1 = teste_universidade(7,'UFRJ', 1, [range(1,11)])
universidade_3_2 = teste_universidade(8,'PUC-RJ', 1, [range(1,11,2)])
universidade_3_3 = teste_universidade(9,'IME', 1, [range(1,15,3)])

universidade_4_1 = teste_universidade(10,'Harvard', 3, [range(1,11)])
universidade_4_2 = teste_universidade(11,'MIT', 3, [range(1,11,2)])
universidade_4_3 = teste_universidade(12,'Princetown', 3, [range(1,15,3)])
universidade_4_4 = teste_universidade(13,'Einstein University', 3, [range(1,11)])
universidade_4_5 = teste_universidade(14,'Tesla Foundation', 3, [range(1,11,2)])
universidade_4_6 = teste_universidade(15,'Carnegie Institute', 3, [range(1,15,3)])

lista_universidades = [universidade_1_1, universidade_1_2, universidade_1_3, universidade_2_1, universidade_2_2, universidade_2_3, universidade_3_1, universidade_3_2, universidade_3_3, universidade_4_1, universidade_4_2, universidade_4_3, universidade_4_4, universidade_4_5, universidade_4_6]

#Cursos

curso_1 = teste_cursos(1, 'Medicina')
curso_2 = teste_cursos(2, 'Engenharia Civil')
curso_3 = teste_cursos(3, 'Farmacia')
curso_4 = teste_cursos(4, 'Educacao Fisica')
curso_5 = teste_cursos(5, 'Matematica')
curso_6 = teste_cursos(6, 'Biologia')
curso_7 = teste_cursos(7, 'Historia')
curso_8 = teste_cursos(8, 'Odontologia')
curso_9 = teste_cursos(9, 'Engenharia de Pesca')
curso_10 = teste_cursos(10, 'Biomedicina')
curso_11 = teste_cursos(11, 'Filosofia')
curso_12 = teste_cursos(12, 'Sociologia')
curso_13 = teste_cursos(13, 'Estatistica')
curso_14 = teste_cursos(14, 'Sistema da Informacao')
curso_15 = teste_cursos(15, 'Ciencia de Dados')

lista_cursos = [curso_1, curso_2, curso_3, curso_4, curso_5, curso_6, curso_7, curso_8, curso_9, curso_10, curso_11, curso_12, curso_13, curso_14, curso_15]