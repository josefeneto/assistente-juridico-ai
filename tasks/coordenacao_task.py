# -*- coding: utf-8 -*-
"""
Task de Coordenação - Assistente Jurídico IA
Responsável por analisar a consulta e direcionar para o especialista adequado
"""

from crewai import Task

def create_coordenacao_task(agent_coordenador, consulta_usuario):
    """
    Cria a task de coordenação para análise inicial da consulta
    """
    
    task = Task(
        description=f'''Analisa a seguinte consulta jurídica de um utilizador português:

        CONSULTA: "{consulta_usuario}"

        A tua função é:
        1. Analisar a consulta e identificar a(s) área(s) do direito envolvida(s)
        2. Determinar qual especialista deve responder (Civil, Penal, Comercial)
        3. Fornecer contexto sobre por que essa especialização foi escolhida
        4. Identificar os principais conceitos jurídicos envolvidos
        5. Preparar instruções específicas para o especialista

        IMPORTANTE:
        - Se a consulta envolver múltiplas áreas, indica todas
        - Se não for clara, pede esclarecimentos
        - Inclui sempre que é uma consulta sobre direito português

        RESULTADO ESPERADO:
        Análise clara da consulta com direcionamento para o especialista adequado,
        incluindo contexto e conceitos-chave a abordar.''',
        
        agent=agent_coordenador,
        expected_output='''Análise estruturada contendo:
        1. Identificação da(s) área(s) jurídica(s)
        2. Especialista recomendado
        3. Justificação da escolha
        4. Conceitos-chave a abordar
        5. Instruções específicas para o especialista''',
        
        output_file=None  # Não salva em arquivo, apenas mantém em memória
    )
    
    return task

def test_coordenacao_task():
    """Teste da task de coordenação"""
    try:
        from agents.coordenador import create_coordenador_agent
        coordenador = create_coordenador_agent()
        task = create_coordenacao_task(coordenador, "Teste de consulta")
        print("✅ Task de Coordenação criada com sucesso!")
        print(f"Descrição: {task.description[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar Task de Coordenação: {e}")
        return False

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    print("📋 Testando Task de Coordenação...")
    print("-" * 40)
    
    success = test_coordenacao_task()
    
    if success:
        print("\n🎉 Task de Coordenação está pronta!")
        print("🎯 Função: Análise e direcionamento de consultas")