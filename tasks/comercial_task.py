# -*- coding: utf-8 -*-
"""
Task de Direito Comercial - Assistente Jurídico IA
Especializada em questões de Direito Comercial português
"""

from crewai import Task

def create_comercial_task(agent_comercial, consulta_usuario, area_identificada="Direito Comercial"):
    """
    Cria task especializada em Direito Comercial português
    """
    
    task = Task(
        description=f'''Como especialista em Direito Comercial português, analisa e responde
        à seguinte consulta jurídica:

        CONSULTA: "{consulta_usuario}"
        ÁREA: {area_identificada}

        A tua resposta deve incluir:
        1. ENQUADRAMENTO LEGAL: Código das Sociedades Comerciais e legislação aplicável
        2. CONCEITOS EMPRESARIAIS: Definições técnicas de direito societário
        3. OBRIGAÇÕES LEGAIS: Deveres e responsabilidades empresariais
        4. PROCEDIMENTOS: Formalidades legais e registos obrigatórios
        5. CONSEQUÊNCIAS: Implicações do incumprimento
        6. CONSIDERAÇÕES PRÁTICAS: Aspectos operacionais relevantes
        7. AVISO LEGAL: Disclaimer obrigatório

        FONTES A CITAR:
        - Código das Sociedades Comerciais (CSC)
        - Código do Registo Comercial (CRC)
        - Código de Insolvência e Recuperação de Empresas (CIRE)
        - Código do IRC e outros diplomas fiscais
        - Regulamentos da CMVM
        - Jurisprudência comercial relevante

        METODOLOGIA:
        - Distingue tipos de sociedades e suas especificidades
        - Indica prazos e formalidades obrigatórias
        - Explica responsabilidades dos sócios/administradores
        - Refere obrigações contabilísticas e fiscais
        - Menciona sanções por incumprimento

        LIMITAÇÕES:
        - NÃO dá conselhos sobre estratégias empresariais específicas
        - NÃO substitui consulta com advogado comercialista
        - Para operações complexas, recomenda sempre assessoria jurídica''',
        
        agent=agent_comercial,
        expected_output='''Resposta jurídica estruturada contendo:
        1. Base legal (CSC e legislação comercial aplicável)
        2. Definições dos conceitos empresariais relevantes
        3. Obrigações e responsabilidades legais
        4. Procedimentos e formalidades obrigatórias
        5. Consequências do incumprimento
        6. Considerações práticas importantes
        7. Recomendações sobre assessoria jurídica
        8. Aviso legal obrigatório completo''',
        
        output_file=None
    )
    
    return task

def test_comercial_task():
    """Teste da task comercial"""
    try:
        from agents.especialista_comercial import create_especialista_comercial
        especialista = create_especialista_comercial()
        task = create_comercial_task(especialista, "Teste de consulta comercial")
        print("✅ Task Comercial criada com sucesso!")
        print(f"Descrição: {task.description[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar Task Comercial: {e}")
        return False

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    print("💼 Testando Task de Direito Comercial...")
    print("-" * 40)
    
    success = test_comercial_task()
    
    if success:
        print("\n✅ Task Comercial está pronta!")
        print("📚 Especialização: Sociedades, Contratos Comerciais, Direito Empresarial")