import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from objetos import teste_estado, lista_estados

st.title('Sistema de Auxilio ao Candidato')
st.markdown('Esse sistema tem como objetivo tornar mais claro as informações contidas na base de dados pública do governo brasileiro a respeito da tejetória do ensino superior no Brasil.')

resume_sac = st.expander('💠 Mais informações')
with resume_sac:
  st.markdown('**Através dele será possível:**')
  col1, col2 = st.columns(2)
  with col1:
    st.markdown('• Visualizar informações a respeito da oferta de cursos de ensino superior por Estado;')
    st.markdown('• Identificar os cursos ofertados pelas instituições de ensino;')
  with col2:
    st.markdown('• Conferir os principais indicadores de trajetória de ensino superior;')
    st.markdown('• Análises.')
  st.markdown('[Clique aqui para acessar a base de dados pública.](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-de-fluxo-da-educacao-superior)')

st.markdown('___')

#
#SEÇÃO 1 - Informações Gerais
options_estados= ['Escolha uma opção', 'Estado 1', 'Estado 2', 'Estado 3', 'Estado 4']

st.header('Oferta e Classificação das Instituições por Estado')
st.write('Abaixo você poderá selecionar um estado para iniciar a navegação em nosso aplicativo. A partir do estado selecionado, será apresentado algumas informações a respeito das instituições e ofertas de cursos.')

user_estado = st.selectbox('Selecione o estado', options_estados)


# SERÁ NECESSÁRIO ESTRUTURAR OS DADOS DE ACORDO COM A SEÇÃO
# PENSAR NA ESTRUTURAÇÃO DA SEÇÃO 01
 
options_1 = ['-','UFES', 'Multivix', 'Unip', 'FAESA', 'UCL']
options_2 = ['-','Unicamp', 'USP', 'PUC-SP', 'ITA']
options_3 = ['-','UFRJ', 'PUC-RJ', 'IME']
options_4 = ['-','Harvard', 'MIT', 'Princetown University', 'Einstein University']

dict_options = {'Estado 1': options_1,
                'Estado 2': options_2,
                'Estado 3': options_3,
                'Estado 4': options_4}


#for estado in lista_estados:
#  if user_estado == estado.nome:
#    st.bar_chart(x=)

if user_estado in dict_options: 
  options = dict_options[user_estado]
  user_unviersidade = st.selectbox(f'Escolha uma universidade existente em {user_estado}',options)
else:
  st.error('Selecione uma opção valida.')



    
    
    
