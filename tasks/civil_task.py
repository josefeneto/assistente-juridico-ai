# -*- coding: utf-8 -*-
"""
Task de Direito Civil - Assistente Jurídico IA
Especializada em questões de Direito Civil português
"""

from crewai import Task

def create_civil_task(agent_civil, consulta_usuario, area_identificada="Direito Civil"):
    """
    Cria task especializada em Direito Civil português
    """
    
    task = Task(
        description=f'''Como especialista em Direito Civil português, analisa e responde
        à seguinte consulta jurídica:

        CONSULTA: "{consulta_usuario}"
        ÁREA: {area_identificada}

        A tua resposta deve incluir:
        1. ENQUADRAMENTO LEGAL: Artigos específicos aplicáveis
        2. CONCEITOS JURÍDICOS: Definição clara dos termos técnicos
        3. EXPLICAÇÃO: Interpretação acessível da legislação
        4. JURISPRUDÊNCIA: Orientações dos tribunais superiores (se relevante)
        5. CONSIDERAÇÕES PRÁTICAS: Aspectos importantes a considerar
        6. AVISO LEGAL: Disclaimer obrigatório sobre natureza informativa

        METODOLOGIA:
        - Cita sempre os artigos específicos (ex: "art. 405º do Código Civil")
        - Explica conceitos técnicos de forma clara
        - Distingue diferentes situações quando aplicável
        - Refere legislação complementar relevante
        - Inclui jurisprudência consolidada

        LIMITAÇÕES:
        - NÃO dês conselhos sobre ações específicas a tomar
        - NÃO substitui consulta com advogado
        - Foca na informação jurídica geral e educativa''',
        
        agent=agent_civil,
        expected_output='''Resposta jurídica estruturada contendo:
        1. Base legal (artigos do Código Civil e legislação complementar)
        2. Definições dos conceitos jurídicos relevantes
        3. Explicação clara e acessível
        4. Referências jurisprudenciais (quando aplicável)
        5. Considerações práticas importantes
        6. Aviso legal obrigatório completo''',
        
        output_file=None
    )
    
    return task

def test_civil_task():
    """Teste da task civil"""
    try:
        from agents.especialista_civil import create_especialista_civil
        especialista = create_especialista_civil()
        task = create_civil_task(especialista, "Teste de consulta civil")
        print("✅ Task Civil criada com sucesso!")
        print(f"Descrição: {task.description[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar Task Civil: {e}")
        return False

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    print("📋 Testando Task de Direito Civil...")
    print("-" * 40)
    
    success = test_civil_task()
    
    if success:
        print("\n✅ Task Civil está pronta!")
        print("📚 Especialização: Contratos, Propriedade, Obrigações, Família")