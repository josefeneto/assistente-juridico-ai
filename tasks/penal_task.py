# -*- coding: utf-8 -*-
"""
Task de Direito Penal - Assistente Jurídico IA
Especializada em questões de Direito Penal português
"""

from crewai import Task

def create_penal_task(agent_penal, consulta_usuario, area_identificada="Direito Penal"):
    """
    Cria task especializada em Direito Penal português
    """
    
    task = Task(
        description=f'''Como especialista em Direito Penal português, analisa e responde
        à seguinte consulta jurídica:

        CONSULTA: "{consulta_usuario}"
        ÁREA: {area_identificada}

        A tua resposta deve incluir:
        1. TIPIFICAÇÃO LEGAL: Identificação do crime ou infração
        2. ELEMENTOS CONSTITUTIVOS: Elementos objetivos e subjetivos
        3. MOLDURA PENAL: Penas aplicáveis e suas variações
        4. PROCEDIMENTO: Tipo de procedimento (público, semi-público, particular)
        5. PRESCRIÇÃO: Prazos de prescrição aplicáveis
        6. JURISPRUDÊNCIA: Orientações dos tribunais superiores
        7. AVISO LEGAL: Disclaimer obrigatório

        FONTES A CITAR:
        - Código Penal (DL 400/82)
        - Código de Processo Penal (DL 78/87)
        - Regime Geral das Contraordenações (DL 433/82)
        - Legislação especial relevante
        - Acórdãos do STJ e Tribunais da Relação

        METODOLOGIA:
        - Distingue crimes de contraordenações
        - Indica sempre as molduras penais (ex: "1 a 5 anos")
        - Refere se é crime público, semi-público ou particular
        - Explica os elementos do tipo de crime
        - Menciona agravantes e atenuantes relevantes

        LIMITAÇÕES:
        - NÃO aconselha sobre estratégias de defesa
        - NÃO substitui consulta com advogado criminalista
        - Em casos graves, recomenda sempre apoio jurídico especializado''',
        
        agent=agent_penal,
        expected_output='''Resposta jurídica estruturada contendo:
        1. Identificação precisa do tipo legal de crime
        2. Análise dos elementos constitutivos
        3. Moldura penal aplicável com variações
        4. Procedimento processual aplicável
        5. Prazos de prescrição
        6. Jurisprudência relevante consolidada
        7. Recomendações sobre consulta jurídica especializada
        8. Aviso legal obrigatório completo''',
        
        output_file=None
    )
    
    return task

def test_penal_task():
    """Teste da task penal"""
    try:
        from agents.especialista_penal import create_especialista_penal
        especialista = create_especialista_penal()
        task = create_penal_task(especialista, "Teste de consulta penal")
        print("✅ Task Penal criada com sucesso!")
        print(f"Descrição: {task.description[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar Task Penal: {e}")
        return False

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    print("🔒 Testando Task de Direito Penal...")
    print("-" * 40)
    
    success = test_penal_task()
    
    if success:
        print("\n✅ Task Penal está pronta!")
        print("📚 Especialização: Crimes, Penas, Processo Penal")
