# -*- coding: utf-8 -*-
"""
Task de Validação - Assistente Jurídico IA
Responsável por revisar e validar as respostas dos especialistas
"""

from crewai import Task

def create_validacao_task(agent_coordenador, resposta_especialista, consulta_original):
    """
    Cria task de validação para revisar resposta do especialista
    """
    
    task = Task(
        description=f'''Revisa e valida a resposta jurídica fornecida pelo especialista,
        garantindo que:

        VALIDAÇÃO DE CONTEÚDO:
        1. As citações legais estão corretas e precisas
        2. Os conceitos jurídicos estão bem explicados
        3. A informação está atualizada conforme legislação portuguesa
        4. A resposta é completa e responde à pergunta

        VALIDAÇÃO DE FORMA:
        1. Linguagem é clara e acessível
        2. Estrutura é lógica e bem organizada
        3. Inclui o aviso legal obrigatório
        4. Não contém conselhos jurídicos específicos

        MELHORIAS:
        1. Adiciona informações relevantes em falta
        2. Clarifica pontos confusos
        3. Melhora a estrutura se necessário
        4. Garante compliance com limitações éticas

        Se encontrares problemas significativos, indica as correções necessárias.
        Se a resposta estiver adequada, confirma e apresenta a versão final.

        CONSULTA ORIGINAL: "{consulta_original}"
        RESPOSTA A VALIDAR: "{resposta_especialista}"''',
        
        agent=agent_coordenador,
        expected_output='''Validação estruturada contendo:
        1. Análise da correção das citações legais
        2. Avaliação da clareza dos conceitos explicados
        3. Verificação da completude da resposta
        4. Confirmação da presença do aviso legal
        5. Lista de melhorias aplicadas (se houver)
        6. Resposta final validada e aprovada
        7. Confirmação de compliance ético''',
        
        output_file=None
    )
    
    return task

def test_validacao_task():
    """Teste da task de validação"""
    try:
        from agents.coordenador import create_coordenador_agent
        coordenador = create_coordenador_agent()
        task = create_validacao_task(
            coordenador, 
            "Resposta de teste",
            "Consulta de teste"
        )
        print("✅ Task de Validação criada com sucesso!")
        print(f"Descrição: {task.description[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar Task de Validação: {e}")
        return False

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    print("🔍 Testando Task de Validação...")
    print("-" * 40)
    
    success = test_validacao_task()
    
    if success:
        print("\n✅ Task de Validação está pronta!")
        print("🎯 Função: Revisão e validação das respostas jurídicas")