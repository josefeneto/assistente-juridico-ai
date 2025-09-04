# -*- coding: utf-8 -*-
from crewai import Agent
from langchain_groq import ChatGroq
import os

def create_coordenador_agent():
    # Configurar LLM
    llm = None
    groq_key = os.getenv('GROQ_API_KEY')
    groq_model = os.getenv('GROQ_MODEL')

    print(f"GROQ_API_KEY existe: {groq_key and groq_key != 'your_groq_api_key_here'}")

    if groq_key and groq_key != 'your_groq_api_key_here':
        from langchain_groq import ChatGroq
        llm = ChatGroq(
            temperature=0.1,
            max_tokens=5500,
            api_key=groq_key,
            model=groq_model
        )
    else:
        from langchain_openai import ChatOpenAI
        openai_model = os.getenv('OPENAI_MODEL')
        llm = ChatOpenAI(
            temperature=0.1,
            model=openai_model
        )

    print(f"OPENAI_API_KEY existe: {os.getenv('OPENAI_API_KEY') is not None}")
    print(f"GROQ_API_KEY existe: {os.getenv('GROQ_API_KEY') is not None}")
    print(f"Modelo configurado: {groq_model}")
    import requests
    headers = {"Authorization": f"Bearer {groq_key}"}
    response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
    print(response.status_code)
    
    coordenador = Agent(
        role='Coordenador Jurídico',
        goal='Analisar consultas jurídicas portuguesas e direcionar para especialista adequado',
        backstory='És um jurista português experiente que analisa consultas e identifica a área do direito envolvida para encaminhar ao especialista correto.',
        verbose=True,
        allow_delegation=True,
        llm=llm
    )
    
    return coordenador

def test_coordenador():
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        agent = create_coordenador_agent()
        print("✅ Agente Coordenador criado!")
        print(f"Role: {agent.role}")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🤖 Testando Coordenador...")
    test_coordenador()
