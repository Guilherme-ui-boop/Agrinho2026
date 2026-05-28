import streamlit as st
import random
import time

# Configuração da página com novo visual (tema escuro/moderno por padrão)
st.set_page_config(page_title="BioVisão Agro", page_icon="🛸", layout="wide")

# Cabeçalho totalmente diferente
st.title("🛸 BioVisão Agro")
st.subheader("Monitoramento Geoespacial e Inteligência Artificial para Defesa Ecológica")
st.write("---")

# Nova proposta de valor para o concurso
st.sidebar.markdown("""
## 🌾 O Conceito
O **BioVisão Agro** afasta-se do monitoramento convencional de planta por planta. Utilizando simulação de imagens aéreas (Drones/Satélites), a IA escaneia talhões inteiros para identificar manchas de infestação antes que elas se espalhem, garantindo o equilíbrio perfeito entre superprodução e preservação ambiental.
""")

st.markdown("""
### 📊 Painel de Controle de Visão Aérea
Suba o arquivo de mapeamento ou a foto aérea da sua propriedade (capturada por drone ou satélite) para iniciar a varredura automatizada com Inteligência Artificial.
""")

# Área de Upload alterada
arquivo_mapa = st.file_uploader("📂 Arraste aqui a imagem aérea da lavoura (Formato: JPG, PNG ou TIF)", type=["jpg", "jpeg", "png", "tif"])

if arquivo_mapa is not None:
    # Divisão da tela em colunas para um visual mais profissional
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 🌐 Imagem Original")
        st.image(arquivo_mapa, caption="Mapa aéreo carregado no sistema", use_container_width=True)
        
    with col2:
        st.write("### 🤖 Processamento da IA")
        progresso = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progresso.progress(i + 1)
            
        with st.spinner("Calculando Índice de Vegetação (NDVI) e focos de calor..."):
            time.sleep(1.5)
            
        # Nova simulação de diagnóstico (Diferente do projeto do seu amigo)
        cenarios = [
            {
                "diagnostico": "Anomalia Detectada no Talhão Norte (Possível Infestação de Percevejo-marrom)",
                "severidade": "Moderada",
                "area": "4.2 Hectares afetados",
                "solucao": "Ativar aplicação cirúrgica via drone de pulverização de precisão utilizando extratos botânicos regulamentados. Preservação estimada de 92% da fauna de insetos benéficos da área periférica."
            },
            {
                "diagnostico": "Área Totalmente Estabilizada (Equilíbrio Ecológico Perfeito)",
                "severidade": "Nenhuma",
                "area": "0 Hectares afetados",
                "solucao": "Os índices de biomassa e biodiversidade estão excelentes. O manejo sustentável atual deve ser mantido sem intervenções químicas."
            },
            {
                "diagnostico": "Alerta Crítico: Vetor de Invasão Detectado nas Bordas da Mata Preservada",
                "severidade": "Alta",
                "area": "12.5 Hectares sob risco",
                "solucao": "Criar uma barreira biológica natural plantando espécies repelentes nas bordas da lavoura. Isso impede a entrada da praga sem afetar a reserva florestal vizinha."
            }
        ]
        
        resultado = random.choice(cenarios)
        
        # Exibição estilizada dos resultados
        if resultado["severidade"] == "Nenhuma":
            st.success(f"🌱 **Status:** {resultado['diagnostico']}")
        elif resultado["severidade"] == "Moderada":
            st.warning(f"⚠️ **Alerta:** {resultado['diagnostico']}")
            st.metric(label="Área Comprometida", value=resultado["area"])
        else:
            st.error(f"🚨 **CRÍTICO:** {resultado['diagnostico']}")
            st.metric(label="Área sob Risco Imediato", value=resultado["area"])
            
        st.info(f"📋 **Diretriz de Ação Sustentável:** {resultado['solucao']}")

st.write("---")
st.caption("BioVisão Agro S
