# -*- coding: utf-8 -*-
from crewai import Agent
from langchain_groq import ChatGroq
import os

def create_especialista_civil():
    # Configurar LLM
    llm = None
    groq_key = os.getenv('GROQ_API_KEY')
    groq_model = os.getenv('GROQ_MODEL')

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
    
    especialista = Agent(
        role='Especialista em Direito Civil Português',
        goal='Fornecer informação jurídica sobre Direito Civil português incluindo contratos, propriedade e família',
        backstory='És um jurista especializado em Direito Civil português com conhecimento do Código Civil e jurisprudência portuguesa.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
    
    return especialista

def test_especialista_civil():
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        agent = create_especialista_civil()
        print("✅ Especialista Civil criado!")
        print(f"Role: {agent.role}")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("⚖️ Testando Especialista Civil...")
    test_especialista_civil()
