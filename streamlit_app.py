# -*- coding: utf-8 -*-
"""
Assistente Jurídico IA - Portugal
Interface Web com Streamlit
"""

import streamlit as st
import os
from dotenv import load_dotenv
from datetime import datetime
import time



# Importar a função principal do sistema
from assistente_juridico_crew import processar_consulta_juridica, inicializar_sistema

def configurar_pagina():
    """
    Configuração inicial da página Streamlit
    """
    st.set_page_config(
        page_title="Assistente Jurídico IA - Portugal",
        page_icon="⚖️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # === DEBUG COMPLETO ===
    st.write(f"TESTE_API_KEY: {os.getenv('TESTE_API_KEY')}")
    st.write(f"Total de variáveis: {len(os.environ)}")

    # Mostrar TODAS as variáveis (primeiros chars)
    st.write("**Todas as variáveis disponíveis:**")
    for key in sorted(os.environ.keys()):
        if not key.startswith('_'):  # Filtrar variáveis internas
            st.write(f"- {key}")

    st.write("🔍 **DEBUG - Variáveis de Ambiente:**")
    st.write(f"GROQ_API_KEY existe: {os.getenv('GROQ_API_KEY') is not None}")
    st.write(f"GROQ_MODEL: {os.getenv('GROQ_MODEL')}")

    # Mostrar todas as variáveis que contém GROQ
    st.write("**Todas as variáveis GROQ:**")
    for key, value in os.environ.items():
        if 'GROQ' in key.upper():
            st.write(f"- {key}: {'***' if 'KEY' in key else value}")

    # Verificar se há alguma variável similar
    st.write("**Variáveis similares:**")
    for key, value in os.environ.items():
        if any(x in key.upper() for x in ['API', 'MODEL', 'GROC', 'GROK']):
            st.write(f"- {key}: {'***' if 'KEY' in key else value}")
# === FIM DEBUG ===
    
    # CSS personalizado
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .specialist-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2a5298;
        margin: 1rem 0;
    }
    .warning-box {
        background: #fff3cd;
        border: 1px solid #ffecb5;
        color: #856404;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .success-box {
        background: #d1e7dd;
        border: 1px solid #badbcc;
        color: #0f5132;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

def sidebar_info():
    """
    Informações na barra lateral
    """
    with st.sidebar:
        st.markdown("### ℹ️ Sobre o Sistema")
        st.markdown("""
        **Assistente Jurídico IA** é um sistema multi-agente especializado em Direito Português.
        
        **Áreas de Especialização:**
        - 📋 Direito Civil
        - 🔒 Direito Penal  
        - 💼 Direito Comercial
        """)
        
        st.markdown("### 🎯 Como Funciona")
        st.markdown("""
        1. **Análise**: O sistema analisa sua pergunta
        2. **Especialização**: Direciona para o especialista adequado
        3. **Validação**: Revisa e valida a resposta
        """)
        
        st.markdown("### 📚 Exemplos de Perguntas")
        exemplos = [
            "Qual é o enquadramento do Crime de ameaça por mensagem?",
            "Como se faz a Constituição de sociedade por quotas?",
            "Descreve os diversos Elementos do crime de furto?",
            "Explicar os Direitos do inquilino particular?"
        ]
        
        for exemplo in exemplos:
            if st.button(f"💡 {exemplo}", key=f"exemplo_{exemplo[:10]}"):
                st.session_state.exemplo_selecionado = exemplo

def verificar_sistema():
    """
    Verifica se o sistema está configurado corretamente
    """
    load_dotenv()
    
    groq_key = os.getenv('GROQ_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    
    if not groq_key and not openai_key:
        st.error("⚠️ Nenhuma API key configurada! Configure GROQ_API_KEY ou OPENAI_API_KEY no arquivo .env")
        return False
    
    if groq_key and groq_key == 'your_groq_api_key_here':
        st.warning("⚠️ API key do Groq não foi atualizada no arquivo .env")
        
    return True

def processar_pergunta_async(pergunta):
    """
    Processa a pergunta de forma assíncrona com indicadores de progresso
    """
    # Barra de progresso
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Fase 1: Inicialização
        status_text.text("🔧 Inicializando sistema...")
        progress_bar.progress(20)
        time.sleep(0.5)
        
        # Fase 2: Análise
        status_text.text("📋 Analisando consulta...")
        progress_bar.progress(40)
        time.sleep(0.5)
        
        # Fase 3: Processamento
        status_text.text("🤖 Processando com especialistas...")
        progress_bar.progress(60)
        
        # Processar a consulta
        resultado = processar_consulta_juridica(pergunta)
        
        # Fase 4: Validação
        status_text.text("✅ Validando resposta...")
        progress_bar.progress(80)
        time.sleep(0.5)
        
        # Finalização
        status_text.text("🎉 Concluído!")
        progress_bar.progress(100)
        time.sleep(0.5)
        
        # Limpar indicadores
        status_text.empty()
        progress_bar.empty()
        
        return resultado
        
    except Exception as e:
        status_text.empty()
        progress_bar.empty()
        return f"❌ Erro no processamento: {str(e)}"

def main():
    """
    Função principal da aplicação Streamlit
    """
    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Configurar página
    configurar_pagina()
    
    # Título principal
    st.markdown("""
    <div class="main-header">
        <h1>⚖️ Assistente Jurídico IA</h1>
        <h3>Especializado em Direito Português</h3>
        <p>Sistema multi-agente com especialistas em Civil, Penal e Comercial</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    sidebar_info()
    
    # Verificar configuração do sistema
    if not verificar_sistema():
        st.stop()
    
    # Área principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 💬 Faça sua Consulta Jurídica")
        
        # Verificar se há exemplo selecionado
        pergunta_inicial = ""
        if 'exemplo_selecionado' in st.session_state:
            pergunta_inicial = st.session_state.exemplo_selecionado
            del st.session_state.exemplo_selecionado

        # Campo de entrada da pergunta
        pergunta_usuario = st.text_area(
            "Digite sua pergunta sobre Direito Português:",
            value=pergunta_inicial,
            height=100,
            placeholder="Ex: Quais são os requisitos para um contrato ser válido em Portugal? Aguarde 30 segundos antes de nova pergunta, devido a licenciamento LLM. Obrigado!"
        )


        # Botões de ação
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
        
        with col_btn1:
            processar = st.button("🚀 Processar", type="primary")
        
        with col_btn2:
            limpar = st.button("🗑️ Limpar")
        
        if limpar:
            st.rerun()

        # st.write(f"DEBUG - pergunta_usuario: '{pergunta_usuario}'")
        # st.write(f"DEBUG - strip(): '{pergunta_usuario.strip()}'")
        # st.write(f"DEBUG - bool check pergunta_usuario: {bool(pergunta_usuario.strip())}")
        # st.write(f"DEBUG - bool check processar: {bool(processar)}")


        # Processar pergunta
        # if processar and pergunta_usuario.strip():
        if pergunta_usuario.strip():
            st.markdown("---")
            st.markdown("### 🤖 Processamento da Consulta")

            
            # Mostrar pergunta
            st.markdown(f"**Pergunta:** {pergunta_usuario}")
            
            time.sleep(15)  # Pausa entre consultas por restrição de licenciamento Grok

            # Processar com indicadores visuais
            resultado = processar_pergunta_async(pergunta_usuario)
            
            # Mostrar resultado
            st.markdown("### 📋 Resposta do Sistema")
            st.markdown(resultado)
            
            # Salvar no histórico (opcional)
            if 'historico' not in st.session_state:
                st.session_state.historico = []
            
            st.session_state.historico.append({
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'pergunta': pergunta_usuario,
                'resposta': resultado[:200] + "..." if len(resultado) > 200 else resultado
            })

            
        elif processar:
            st.warning("⚠️ Por favor, digite uma pergunta antes de processar.")
    
    with col2:
        st.markdown("### 🎯 Especialistas Disponíveis")
        
        # Cards dos especialistas
        especialistas = [
            {
                "titulo": "📋 Direito Civil",
                "areas": ["Contratos", "Propriedade", "Obrigações", "Família", "Sucessões"],
                "cor": "#28a745"
            },
            {
                "titulo": "🔒 Direito Penal", 
                "areas": ["Crimes", "Penas", "Processo Penal", "Contraordenações"],
                "cor": "#dc3545"
            },
            {
                "titulo": "💼 Direito Comercial",
                "areas": ["Sociedades", "Contratos Comerciais", "Direito Empresarial"],
                "cor": "#007bff"
            }
        ]
        
        for especialista in especialistas:
            st.markdown(f"""
            <div class="specialist-card">
                <h4 style="color: {especialista['cor']};">{especialista['titulo']}</h4>
                <p><strong>Áreas:</strong></p>
                <ul>
            """, unsafe_allow_html=True)
            
            for area in especialista['areas']:
                st.markdown(f"<li>{area}</li>", unsafe_allow_html=True)
            
            st.markdown("</ul></div>", unsafe_allow_html=True)
    
    # Histórico de consultas (se houver)
    if 'historico' in st.session_state and st.session_state.historico:
        st.markdown("---")
        st.markdown("### 📚 Histórico de Consultas")
        
        with st.expander("Ver histórico"):
            for i, item in enumerate(reversed(st.session_state.historico[-5:])):  # Últimas 5
                st.markdown(f"""
                **{i+1}. {item['timestamp']}**  
                **P:** {item['pergunta']}  
                **R:** {item['resposta']}
                ---
                """)
    
    # Aviso legal (sempre presente)
    st.markdown("---")
    st.markdown("""
    <div class="warning-box">
        <h4>⚖️ AVISO LEGAL OBRIGATÓRIO</h4>
        <p>A informação fornecida é de natureza geral e meramente informativa, não constituindo aconselhamento jurídico específico. 
        Esta informação não substitui a consulta presencial a um advogado devidamente inscrito na Ordem dos Advogados. 
        A aplicação da lei depende sempre das circunstâncias concretas e específicas de cada situação.</p>
        <p><strong>Para assistência jurídica profissional, consulte sempre um advogado qualificado.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Rodapé
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; font-size: 0.8em;">
        Assistente Jurídico IA v1.0 | Especialização: Direito Português<br>
        Desenvolvido com CrewAI, Groq e Streamlit
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
