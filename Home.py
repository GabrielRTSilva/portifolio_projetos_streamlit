import streamlit as st
import pandas as pd
from markdowns import profile_image


st.markdown("<h1 style='text-align: center;'>Meu Resumo Profissional</h1>", unsafe_allow_html=True)

st.header('Perfil')
st.markdown('***')

col1, col2 = st.columns(2)

with col1:  
  profile_image = st.image('./images/perfil.jpeg', width= 200)
  col3, col4 = st.columns(2)
  with col3:
    st.markdown('🌐 [Instagram](https://www.instagram.com/_grtsilva/)')
    st.markdown('🌐 [Github](https://www.google.com.br)')
  with col4:
    st.markdown('🌐 [Linkedin](https://www.linkedin.com/in/gabrielrtsilva/ )')
    st.markdown('🌐 [SIGPESQ](https://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K1566462J6&tokenCaptchar=03AFcWeA63wPaK5ZJHv2_IUx1eBN9hay6ksaiDUpQoV4p4sG4ixyDiV2R3aTHL883Gi7ObHA-sRrje-IKnGIswz4I3xmK7EFPzKHnMeGnbgvWeVmMRXIGaiQlG1D8X5F8LYdwPNiTwC2-b_w_QnN2H8QgULaW4vKzFFLumcswFWM1X-gIkIPDdqlSaiUkz-e1lotW67nPVn6QbOSFDNoW5fxM__4Wuo4M_2g22gRX353K9ki1bSmnpZ3lQNzbpOBJAr_-giyFN8DNxcl-wlNFv_kF4INruxjTayoWnmpxdgC-9-cX9xFaGIrqciG4HzzZJzX4IBd68rU-68V4pmfbUnmeQDJ3lYVMYMYPuNxvu2qnqEWQ6ROFft5ES6nFb7ETa17_ashXkjsjj6jBmq_o6lqgoX4vsZB07y3xc_EZYyF5B3KXPj5jimYxaVATaK8-591kEb_3Pq7RhZW89zKQKHSXBnZ93Otc_ntF-13Oi2UO6RwDEN8Z29QEGk4m8dqY8HIVEa0at-adIN4KaFPCeEnGflWmnZ8WK1DLZ0V4gE1whs2nW2Hma4F4QLRIPL9AOJEcZg67txS5I_hn8KvHGeifgtrpZ85ySY9G1c8mC85W3Wh8SEPinW3zkwKGYRPopFbJX6Z0iI2GQUn2i_vQ5bBvNKIho6brwAI1IoxpsGnKfLjjS7fQsZihXcciRsQ6LUcEuM6xWh_FVzZbN_w5Sm0Np_YwjxRps2vEK3WGxEyOzJb0fzcwWSM8)')
with col2:
  st.header('Sobre')
  st.markdown('Me chamo Gabriel Rosemberg e sou um Analista de Dados apaixonado por facilitar a visualização e compreensão á respeito da complexa interdependência dos fatos por meio de dados coletados e disponíveis publicamente.')

st.markdown('___')

st.header('Experiências Profissionais')
st.markdown('**• Bolsista de Iniciação Científica, IFES**')
st.markdown('Atualmente estou participando de um projeto de iniciação científica ofertado pelo IFES e tendo como orientador o Dr. Rodrigo Varejão Andreão, diretor geral da FAPES. O tema da pesquisa é métodos de aprendizado de máquina explicáveis e transparentes para o desenvolvimento de sistemas de auxílio ao diagnóstico médico de eletrocardiogramas. Nessa oportunidade, estou desenvolvendo e aprimorando meus conhecimentos na área de inteligência artificial, com foco em deep learning.')

st.markdown('**• Centro de Treinamento Avançado, Diretor**')
st.markdown('O CTA foi um projeto idealizado por eu, um educador físico e o CEO da Anuar Cosméticos à prática de esportes de praia. Atuava dirigindo a estratégia de treino, que tinha como intuito reter o aluno por um maior prazo de tempo. Como professor, ministrando e auxiliando as aulas. Como codiretor, junto ao patrocinador, orientando a metodologia utilizada para melhor experiência do cliente, retenção de alunos e organização de eventos tudo isso baseado em dados que eram captados e analisados utilizando formulários e a linguagem Python. Além disso, criei um workspace para automatizar todas as demandas relacionadas a primeiro contato e cobrança de alunos, o que me fez idealizar uma nova tecnologia para facilitar processos com visão computacional. ')

st.markdown('**• Analista de Dados, Freelancer**')
st.markdown('Realizei toda a estruturação de um fluxo no ambiente do Office365 para o objetivo final de materializar um dashboard com os KPI’s do setor de análise sensorial de uma empresa internacional da indústria alimentícia. Para atingir meu objetivo, integrei as ferramentas Microsoft Forms, Microsoft Power Automate e Microsoft Power Bi, resultando em um dashboard interativo e eficiente.')

st.markdown('**• Elementus SA, Auxiliar de Tecnologia**')
st.markdown('Realizei extração, transformação e carregamento de dados utilizando linguagem Python com dados dos projetos que alimentavam KPI’s da empresa. Automatizei extrações e análises de informações de setores como administrativo, marketing, prospecção e vendas e projetos no workspace do Office 365 para alimentar dashboards no Power BI utilizando o Power Automate, Microsfot Lists e linguagem Python. Inovei o setor de tecnologia iniciando o desenvolvimento de um aplicativo geral para demandas internas utilizando o Power Apps. Além disso, desenvoli uma aplicação que simulava um CRM utilizando ferramentas low code da Microsoft e linguagem Python para os KPIs. Atuava também de suporte N1 para a toda empresa, realizando manutenção em rede, configurações em dispositivos Windows e instalações de softwares. ')

st.markdown('**• CEO, Head Growth e UX Designer, Developing Solution**')
st.markdown('A DevSolutions foi uma empresa que transformou digitalmente a vida de pequenas e médias empresas dos mais diversos seguimentos do mercado. Como CEO direcionava a atuação da equipe para sempre possuir a clareza nos processos, através de metodologias ágeis e eficientes que melhor atendiam a individualidade de cada projeto. Como Head Growth, atuava nas estratégias de prospecção e venda e lead. Também atuei como UX Designer desenvolvendo o design das ferramentas que transformaram os negócios de nossos clientes utilizando a ferramenta Figma.')


st.header('Soft Skills')
col5, col6, col7 = st.columns(3)

with col5:
  st.markdown('• Proativo')
  st.markdown('• Raciocíonio Lógico')
  st.markdown('• Comunicação')
  st.markdown('• Disciplina')
with col6:
  st.markdown('• Criativo')
  st.markdown('• Inovador')
  st.markdown('• Escuta ativa')
  st.markdown('• Observador')
with col7:
  st.markdown('• Trabalho em equipe')
  st.markdown('• Aberto a novas ideias')
  st.markdown('• Adaptável')
  st.markdown('• Atleta')

st.header('Hard Skills')
col8, col9, col10 = st.columns(3)

with col8:
  st.markdown('• Python (Matplot, sklearn, numpy, pandas, streamlit)')
  st.markdown('• HTML/CSS/JScript')
  st.markdown('• Google Colab')
  st.markdown('• Jupyter Notebook')
with col9:
  st.markdown('• Github')
  st.markdown('• Scrum')
  st.markdown('• Trello')
  st.markdown('• Figma') 
with col10:
  st.markdown('• MS Excel')
  st.markdown('• MS Power Bi')
  st.markdown('• MS Power Automate')
  st.markdown('• MS Power Apps')  



