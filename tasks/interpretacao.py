# -*- coding: utf-8 -*-
"""
Tarefas de Interpretação Jurídica - Sistema Multi-Agente
Define as tarefas que os agentes devem executar para interpretar consultas jurídicas
"""

from crewai import Task

def create_coordenacao_task(pergunta_usuario):
    """
    Tarefa para o coordenador analisar e direcionar a consulta
    """
    coordenacao_task = Task(
        description=f'''Analisa a seguinte consulta jurídica de um utilizador português:
        
        CONSULTA: "{pergunta_usuario}"
        
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
        
        expected_output='''Análise estruturada contendo:
        1. Resumo da consulta
        2. Área(s) do direito identificada(s)
        3. Especialista recomendado
        4. Conceitos jurídicos principais
        5. Instruções para o especialista
        6. Observações relevantes''',
        
        agent=None  # Será atribuído na criação da crew
    )
    
    return coordenacao_task

def create_interpretacao_juridica_task(pergunta_usuario, area_direito):
    """
    Tarefa para especialista interpretar questão jurídica específica
    """
    interpretacao_task = Task(
        description=f'''Como especialista em {area_direito} português, analisa e responde 
        à seguinte consulta jurídica:
        
        CONSULTA: "{pergunta_usuario}"
        ÁREA: {area_direito}
        
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
        
        expected_output='''Resposta jurídica estruturada contendo:
        1. Resumo da questão
        2. Base legal com artigos específicos
        3. Explicação clara dos conceitos
        4. Jurisprudência relevante (se aplicável)
        5. Considerações práticas
        6. Aviso legal obrigatório
        
        Formato: Texto claro, bem estruturado, com citações precisas
        e linguagem acessível mantendo rigor técnico.''',
        
        agent=None  # Será atribuído na criação da crew
    )
    
    return interpretacao_task

def create_validacao_resposta_task():
    """
    Tarefa para validar e melhorar a resposta final
    """
    validacao_task = Task(
        description='''Revisa e valida a resposta jurídica fornecida pelo especialista,
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
        Se a resposta estiver adequada, confirma e apresenta a versão final.''',
        
        expected_output='''Resposta jurídica validada e otimizada, contendo:
        1. Confirmação da qualidade da resposta OU lista de correções
        2. Versão final melhorada (se necessário)
        3. Verificação de compliance com avisos legais
        4. Confirmação de adequação às limitações éticas
        
        A resposta final deve ser precisa, clara, completa e eticamente adequada.''',
        
        agent=None  # Será atribuído na criação da crew
    )
    
    return validacao_task

def test_tasks():
    """Teste das tarefas"""
    try:
        # Teste com pergunta exemplo
        pergunta_teste = "Quais são os requisitos para um contrato de compra e venda ser válido?"
        
        # Criar tarefas
        coordenacao = create_coordenacao_task(pergunta_teste)
        interpretacao = create_interpretacao_juridica_task(pergunta_teste, "Direito Civil")
        validacao = create_validacao_resposta_task()
        
        print("✅ Tarefa de Coordenação criada")
        print("✅ Tarefa de Interpretação Jurídica criada")  
        print("✅ Tarefa de Validação criada")
        
        return True
    except Exception as e:
        print(f"❌ Erro ao criar tarefas: {e}")
        return False

if __name__ == "__main__":
    print("📋 Testando Sistema de Tarefas...")
    print("-" * 50)
    
    success = test_tasks()
    
    if success:
        print("\n🎉 Sistema de Tarefas está pronto!")
        print("📝 Tarefas disponíveis:")
        print("  - Coordenação e análise")
        print("  - Interpretação jurídica especializada")
        print("  - Validação e otimização")
    else:
        print("\n❌ Erro na criação das tarefas")