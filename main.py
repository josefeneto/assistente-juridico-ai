# main.py - Teste inicial do ambiente
import sys
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def test_environment():
    """Testa se o ambiente está configurado corretamente"""
    print("🔍 Testando ambiente de desenvolvimento...")
    print(f"Python version: {sys.version}")
    print("-" * 50)
    
    # Testar importações principais
    try:
        import crewai
        print(f"✅ CrewAI instalado: {crewai.__version__}")
    except ImportError as e:
        print(f"❌ CrewAI: {e}")
    
    try:
        import streamlit
        print(f"✅ Streamlit instalado: {streamlit.__version__}")
    except ImportError as e:
        print(f"❌ Streamlit: {e}")
    
    try:
        import groq
        print("✅ Groq API client instalado")
    except ImportError as e:
        print(f"❌ Groq: {e}")
    
    try:
        import openai
        print(f"✅ OpenAI instalado: {openai.__version__}")
    except ImportError as e:
        print(f"❌ OpenAI: {e}")
    
    # Verificar variáveis de ambiente
    print("-" * 50)
    print("🔑 Verificando variáveis de ambiente:")
    
    groq_key = os.getenv('GROQ_API_KEY')
    if groq_key:
        print(f"✅ GROQ_API_KEY: {groq_key[:10]}...***")
    else:
        print("⚠️  GROQ_API_KEY não configurada")
    
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key:
        print(f"✅ OPENAI_API_KEY: {openai_key[:10]}...***")
    else:
        print("⚠️  OPENAI_API_KEY não configurada")
    
    print("-" * 50)
    print("🎉 Teste de ambiente concluído!")
    print("\n📋 Próximos passos:")
    print("1. Configure as API keys no arquivo .env")
    print("2. Execute: streamlit run app.py")
    print("3. Teste a interface web")

if __name__ == "__main__":
    test_environment()