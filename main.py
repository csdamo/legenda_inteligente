import openai
import os
import streamlit as st
from streamlit_chat import message as msg


openai.api_key = os.getenv('OPENAI_API_KEY')

imagem = 'assets/vanGogh.jpeg'

st.title("Conheça as principais obras de Vicent Van Gogh")
st.image(imagem)
st.write("***")


#############################################################################################################################################################

texto_1 = """
Embora A Noite Estrelada tenha sido pintada durante o dia no estúdio do térreo, seria impreciso classificá-la como pintura de memória. 
A vista, identificada como sendo a de uma janela virada para o leste na cela de Van Gogh, foi por ele explorada em não menos que vinte e uma oportunidades, seja na produção de estudos ou pinturas derivadas,[carece de fontes] incluindo em A Noite Estrelada. 
"Através da janela com barras de ferro", escreveu para o irmão c. 23 de maio de 1889, "Eu posso ver um campo cercado de trigo (...) acima do qual, durante a manhã, eu vejo o sol nascer com toda a sua glória."
Van Gogh pintou a vista da janela em diferentes períodos do dia, sob várias condições, como na alvorada, anoitecer, dias ensolarados, nublados, ventosos e num dia chuvoso. 
A equipe de funcionários do asilo não o deixava pintar na cela, mas Vincent, ainda nos aposentos, conseguia rascunhar com tinta ou carvão no papel e então usava os desenhos como a base para a criação de variações de trabalhos anteriores. O elemento pictórico em comum a todas essas pinturas e desenhos é a linha diagonal que representa as baixas colinas dos Alpilles. Van Gogh aproximou o campo de enquadramento em seis dessas obras, mais notavelmente em Campo de Trigo Com Ciprestes (F717) e em A Noite Estrelada, trazendo as árvores para mais perto na composição.[carece de fontes]
Uma das primeiras pinturas dessa vista foi Paisagem Montanhosa Atrás de Saint-Rémy (F611).
Van Gogh produziu vários rascunhos para essa tela, dentre os quais destaca-se O Campo de Trigo Cercado Depois da Tempestade (F1547) como um típico exemplo. 
Não se sabe essa pintura foi feita no estúdio ou in loco. Numa carta de 9 de junho, onde o artista fala sobre esse trabalho, há a menção de ter pintado ao ar livre por uns dias.
Numa carta para a irmã Wil de 16 de junho de 1889, o pintor descreve a segunda das duas paisagens que estivera produzindo,[19][Carta 4] Campo Verde (F719), a primeira que definitivamente fora pintada en plein air durante a estadia no hospital psiquiátrico.
Campo de Trigo, Saint-Rémy de Provence (F1548) é um dos estudos produzidos para essa pintura. Dois dias depois, Vincent escreveu para Theo contando-lhe que havia pintado "um céu estrelado".[21][Carta 1]
A Noite Estrelada é a única noturna da série de obras da vista do quarto do hospício. Em carta do começo de junho para o irmão, Vincent escreveu: "Eu observei nesta manhã o campo da minha janela por um bom tempo antes da alvorada, com nada [no céu] além da Estrela d'Alva, que parecia enorme".[Carta 5] 
Pesquisadores determinaram que Vênus estivera mesmo visível ao amanhecer de Provence na primavera de 1889 e que naquele período seu brilho era quase máximo. Dessa forma, concluiu-se que a "estrela" mais brilhante da pintura, logo à direita do cipreste, é o segundo planeta do Sistema Solar.
A lua foi uma estilização, pois registros astronômicos indicam que o astro estivera minguante giboso quando Van Gogh produziu a tela.
Mesmo que a Lua então estivesse minguante, a representação de Van Gogh não estaria astronomicamente adequada. O único elemento pictórico definitivamente fora do alcance daquela vista de Van Gogh é o vilarejo, que teve por base o rascunho F1541v, feito a partir de uma encosta montanhosa acima do nível de Saint-Rémy.
Pickvance considerou que o desenho F1541v teria sido feito depois e que o campanário parecia mais neerlandês que provençal, fruto de uma mistura de vários trabalhos do artista no período de Nuenen, levantando então a possibilidade de a pintura ser a primeira das "reminiscências do Norte" que desenvolveria no início do ano seguinte.[1] Hulsker alegou que uma paisagem revertida, catalogada como F1541r, teria sido também um estudo para essa A Noite Estrelada
"""

if 'texto_imagem_1' not in st.session_state:
    st.session_state.texto_imagem_1 = [
                {
            "role": "assistant", 
            "content": texto_1
        },
    ]
st.subheader('A Noite Estrelada')    

imagem_1 = 'assets/vangogh_noiteestrela.webp'
st.image(imagem_1)

question = st.text_input("O que você quer saber a obra 'A Noite Estrelada' ")
btn_send = st.button("Quero saber mais sobre A Noite Estrelada")

if btn_send:
    contexto = st.session_state.texto_imagem_1.append({"role": "user", "content": question})
    return_openai=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=contexto,
        max_tokens= 500,
        n=1
    )
    st.session_state.texto_imagem_1.append(
        {
            "role": "assistant", 
            "content": return_openai['choices'][0]['message']['content']
        }
    )
    
    len_list = len(st.session_state.texto_imagem_1)
    
    st.write(st.session_state.texto_imagem_1[-1]['content'])

#############################################################################################################################################################

texto_2 = """
Quarto em Arles é uma obra do pintor impressionista Vincent van Gogh. Há três exemplares originais, pintados entre outubro de 1888 e setembro de 1889. 
A obra é uma das mais conhecidas do artista.
O famoso quadro retrata o quarto que Vincent van Gogh alugou numa pensão, na cidade de Arles, na França, país onde trabalhou durante quase toda a sua vida.
Essa tela atualmente encontra-se no Museu de Orsay, em Paris, na França.
Van Gogh, a pedido de seu irmão Theo, fez uma segunda versão de Quarto em Arles em 1889. 
A "cópia", entretanto, não é exata; nota-se o uso de tons mais escuros que o original, redução da ênfase das fendas no assoalho, bem como diferenças em dois porta-retratos nas paredes.
Embora buscasse a impressão de tranquilidade em seu quadro, este reflete a tensão, a solidão e desarraigamento de Van Gogh na ocasião da pintura. 
Os objetos do quarto não tem relação entre si, o piso aparenta cair para frente, a janela está entreaberta, os quadros pendem em direção à cama, os móveis em diagonal, tudo parece refletir o caos em que Van Gogh mergulhara.
Os pigmentos das tintas utilizadas na pintura foram avaliadas em 2012, concluindo-se que as paredes eram originalmente roxas, com o passar do tempo o pigmento vermelho perdeu sua cor e deixou as paredes azuladas.
"""

if 'texto_imagem_2' not in st.session_state:
    st.session_state.texto_imagem_2 = [
                {
            "role": "assistant", 
            "content": texto_2
        },
    ]
st.subheader('Quarto em Arles')     

imagem_2 = 'assets/quarto-arles-getty.webp'
st.image(imagem_2)

question = st.text_input("O que você quer saber a obra 'Quarto em Arles' ")
btn_send = st.button("Quero saber mais sobre Quarto em Arles")

if btn_send:
    st.session_state.texto_imagem_2.append(
        {"role": "user", "content": question}
    )
    return_openai=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.texto_imagem_2,
        max_tokens= 500,
        n=1
    )
    st.session_state.texto_imagem_2.append(
        {
            "role": "assistant", 
            "content": return_openai['choices'][0]['message']['content']
        }
    )
    
    len_list = len(st.session_state.texto_imagem_2)
    
    st.write(st.session_state.texto_imagem_2[-1]['content'])