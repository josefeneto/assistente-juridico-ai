# app.py - Interface Streamlit para Assistente Jurídico
import streamlit as st
import os
from dotenv import load_dotenv

# Configuração da página
st.set_page_config(
    page_title="Assistente Jurídico IA",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar variáveis de ambiente
load_dotenv()

# CSS customizado
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f4e79;
        padding: 1rem 0;
        border-bottom: 3px solid #d4af37;
        margin-bottom: 2rem;
    }
    .warning-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .info-box {
        background-color: #d1ecf1;
        border-left: 5px solid #17a2b8;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header principal
    st.markdown('<h1 class="main-header">🏛️ Assistente Jurídico IA - Portugal</h1>', 
                unsafe_allow_html=True)
    
    # Aviso legal obrigatório
    st.markdown("""
    <div class="warning-box">
        <h4>⚖️ AVISO LEGAL OBRIGATÓRIO</h4>
        <p>A informação fornecida é de natureza geral e meramente informativa, não constituindo 
        aconselhamento jurídico específico. Esta informação não substitui a consulta presencial 
        a um advogado devidamente inscrito na Ordem dos Advogados. A aplicação da lei depende 
        sempre das circunstâncias concretas e específicas de cada situação.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar com informações
    with st.sidebar:
        st.header("📋 Configuração")
        
        # Status das APIs
        groq_configured = bool(os.getenv('GROQ_API_KEY'))
        openai_configured = bool(os.getenv('OPENAI_API_KEY'))
        
        st.subheader("🔑 Status das APIs:")
        st.write(f"{'✅' if groq_configured else '❌'} Groq API")
        st.write(f"{'✅' if openai_configured else '❌'} OpenAI API")
        
        if not groq_configured and not openai_configured:
            st.error("⚠️ Nenhuma API configurada!")
            st.info("Configure pelo menos uma API no arquivo .env")
        
        st.subheader("📚 Especialidades Disponíveis:")
        specialties = [
            "📋 Direito Civil",
            "⚖️ Direito Penal", 
            "💼 Direito Comercial",
            "👥 Direito do Trabalho",
            "🏢 Direito Administrativo",
            "📑 Análise de Documentos"
        ]
        for specialty in specialties:
            st.write(specialty)
    
    # Interface principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("💬 Faça sua Consulta Jurídica")
        
        # Campo para a pergunta
        user_question = st.text_area(
            "Descreva sua dúvida jurídica:",
            height=150,
            placeholder="Exemplo: Quais são os requisitos para um contrato de compra e venda ser válido segundo o Código Civil português?"
        )
        
        # Selectbox para especialidade
        specialty = st.selectbox(
            "Escolha a área do direito:",
            ["Automático", "Direito Civil", "Direito Penal", "Direito Comercial", 
             "Direito do Trabalho", "Direito Administrativo"]
        )
        
        # Botão para processar
        if st.button("🔍 Consultar Agentes IA", type="primary", use_container_width=True):
            if not user_question.strip():
                st.error("Por favor, digite sua pergunta.")
            elif not groq_configured and not openai_configured:
                st.error("Configure pelo menos uma API key no arquivo .env")
            else:
                # Placeholder para processamento
                with st.spinner("🤖 Consultando especialistas..."):
                    # Simular processamento (por enquanto)
                    import time
                    time.sleep(2)
                    
                    # Resposta placeholder
                    st.success("✅ Consulta processada!")
                    
                    st.markdown("### 📋 Resposta dos Agentes:")
                    st.markdown(f"""
                    <div class="info-box">
                    <h4>🎯 Pergunta analisada:</h4>
                    <p><em>"{user_question}"</em></p>
                    
                    <h4>⚖️ Especialidade: {specialty}</h4>
                    
                    <h4>🤖 Status do Sistema:</h4>
                    <p>✅ Sistema configurado e funcional</p>
                    <p>🔄 Agentes IA em desenvolvimento</p>
                    <p>📚 Base de conhecimento: Códigos portugueses</p>
                    
                    <h4>📋 Próxima Fase:</h4>
                    <p>Implementação do sistema multi-agente CrewAI para fornecer respostas jurídicas especializadas.</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🛠️ Status do Sistema")
        
        # Status dos componentes
        st.metric("Streamlit", "🟢 Ativo")
        st.metric("CrewAI", "🟡 Configurado")
        st.metric("APIs", "🟡 Parcial" if groq_configured or openai_configured else "🔴 Não Config.")
        
        st.subheader("📊 Informações Técnicas")
        st.write(f"Python: {st.__version__}")
        st.write("Framework: Streamlit + CrewAI")
        st.write("Estado: Desenvolvimento")
        
        st.subheader("🔧 Próximos Passos")
        steps = [
            "✅ Interface funcional",
            "🔄 Configurar APIs",
            "🔄 Criar agentes IA", 
            "🔄 Base conhecimento",
            "🔄 Deploy Railway"
        ]
        for step in steps:
            st.write(step)

if __name__ == "__main__":
    main()
