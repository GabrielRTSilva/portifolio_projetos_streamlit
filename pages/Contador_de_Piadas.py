import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.i = 0

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        # Aqui você pode adicionar o código para processar a imagem
        return img

st.title('Contador de Piadas')
st.markdown('Esse programa tem como objetivo fazer o usuário rir.')

resume_sac = st.expander('💡Como funciona')
with resume_sac:
    st.markdown('___')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('1. O usuário escolhe o estilo da piada que mais interessa-o.')
        st.markdown('2. Em seguida a camera frontal do usuário abre.')
    with col2:
        st.markdown('3. Por trás da câmera está rodando um algoritmo state-of-the-art para reconhecimento de expressões faciais que irá reconhecer quando o usuário sorrir.')
        st.markdown('4. O sistema se encerra quando o usuário sorrir.')
    st.markdown('___')
    st.markdown('Algoritmo: XXX')
    st.markdown('Referência: XXX')

st.markdown('___')

categoria_piada = ['Selecione uma opção', 'Trocadilhos', 'Piadas Secas', 'Piadas de Humor Negro']
joke_selector = st.selectbox('Selecione a categoria da piada:', categoria_piada)

if joke_selector != 'Selecione uma opção':
    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer, mode = 'sendonly')
