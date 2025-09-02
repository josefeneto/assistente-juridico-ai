# teste_integracao.py - Teste de integração simples
from dotenv import load_dotenv
import os

def teste_integracao_simples():
    """Teste simples de integração sem crew complexa"""
    print("🧪 Teste de Integração Simples...")
    print("-" * 50)
    
    load_dotenv()
    
    try:
        # Testar imports básicos
        from agents.coordenador import create_coordenador_agent
        from agents.especialista_civil import create_especialista_civil
        print("✅ Imports dos agentes: OK")
        
        # Criar agentes
        coordenador = create_coordenador_agent()
        civil = create_especialista_civil()
        print("✅ Criação dos agentes: OK")
        
        # Testar CrewAI básico
        from crewai import Task, Crew, Process
        
        # Tarefa simples
        tarefa_teste = Task(
            description="Diga apenas: 'Assistente Jurídico funcionando'",
            expected_output="Confirmação de funcionamento",
            agent=civil
        )
        
        # Crew simples
        crew_teste = Crew(
            agents=[civil],
            tasks=[tarefa_teste],
            process=Process.sequential,
            verbose=False
        )
        
        print("🚀 Executando crew de teste...")
        resultado = crew_teste.kickoff()
        print(f"✅ Resultado: {resultado}")
        
        print("\n🎉 Integração básica funcional!")
        return True
        
    except Exception as e:
        print(f"❌ Erro na integração: {e}")
        print(f"Tipo do erro: {type(e).__name__}")
        return False

if __name__ == "__main__":
    sucesso = teste_integracao_simples()
    
    if sucesso:
        print("\n📋 Sistema pronto para teste completo!")
        print("Próximo: python assistente_juridico_crew.py")
    else:
        print("\n🔧 Corrigir erros antes de prosseguir")