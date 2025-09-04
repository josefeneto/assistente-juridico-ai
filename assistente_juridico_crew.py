# -*- coding: utf-8 -*-
"""
Assistente Jurídico IA - Portugal
Sistema multi-agente especializado em Direito Português
Versão com Tasks organizadas 
"""

import sys
import os
from dotenv import load_dotenv
from crewai import Crew

# Importar agentes
from agents.coordenador import create_coordenador_agent
from agents.especialista_civil import create_especialista_civil
from agents.especialista_penal import create_especialista_penal
from agents.especialista_comercial import create_especialista_comercial

# Importar tasks
from tasks.coordenacao_task import create_coordenacao_task
from tasks.civil_task import create_civil_task
from tasks.penal_task import create_penal_task
from tasks.comercial_task import create_comercial_task
from tasks.validacao_task import create_validacao_task

def inicializar_sistema():
    """
    Inicializa todos os agentes do sistema
    """
    try:
        # Criar agentes
        coordenador = create_coordenador_agent()
        especialista_civil = create_especialista_civil()
        especialista_penal = create_especialista_penal()
        especialista_comercial = create_especialista_comercial()
        
        return {
            'coordenador': coordenador,
            'civil': especialista_civil,
            'penal': especialista_penal,
            'comercial': especialista_comercial
        }
    except Exception as e:
        print(f"❌ Erro ao inicializar sistema: {e}")
        return None

def identificar_especialista(resultado_coordenacao):
    """
    Identifica qual especialista deve ser usado baseado na análise do coordenador
    """
    resultado_lower = resultado_coordenacao.lower()
    
    if any(termo in resultado_lower for termo in ['penal', 'crime', 'criminal', 'código penal', 'contraordenação']):
        return 'penal'
    elif any(termo in resultado_lower for termo in ['comercial', 'empresa', 'sociedade', 'societário', 'csc']):
        return 'comercial'
    else:
        return 'civil'  # Default para civil

def processar_consulta_juridica(consulta_usuario):
    """
    Processa uma consulta jurídica completa através do sistema multi-agente
    """
    try:
        print(f"🤖 Processando consulta: {consulta_usuario}...")
        
        # Inicializar agentes
        agentes = inicializar_sistema()
        if not agentes:
            return "❌ Erro na inicialização do sistema."

        # FASE 1: COORDENAÇÃO - Análise da consulta
        print("📋 Fase 1: Análise e coordenação...")
        coordenacao_task = create_coordenacao_task(agentes['coordenador'], consulta_usuario)
        
        crew_coordenacao = Crew(
            agents=[agentes['coordenador']],
            tasks=[coordenacao_task],
            verbose=True
        )
        
        resultado_coordenacao = crew_coordenacao.kickoff()
        print("✅ Fase de coordenação concluída")
        
        # Identificar especialista
        tipo_especialista = identificar_especialista(str(resultado_coordenacao))
        print(f"🎯 Área identificada: {tipo_especialista.title()}")
        print(f"👨‍⚖️ Especialista selecionado: Especialista em Direito {tipo_especialista.title()} Português")

        # FASE 2: ESPECIALIZAÇÃO - Resposta especializada
        print("📚 Fase 2: Análise especializada...")
        
        if tipo_especialista == 'penal':
            especialista_task = create_penal_task(agentes['penal'], consulta_usuario, "Direito Penal")
            agente_especialista = agentes['penal']
            area_nome = "Direito Penal"
        elif tipo_especialista == 'comercial':
            especialista_task = create_comercial_task(agentes['comercial'], consulta_usuario, "Direito Comercial")
            agente_especialista = agentes['comercial']
            area_nome = "Direito Comercial"
        else:
            especialista_task = create_civil_task(agentes['civil'], consulta_usuario, "Direito Civil")
            agente_especialista = agentes['civil']
            area_nome = "Direito Civil"
        
        crew_especialista = Crew(
            agents=[agente_especialista],
            tasks=[especialista_task],
            verbose=True
        )
        
        resposta_especialista = crew_especialista.kickoff()
        print("✅ Fase de interpretação concluída")

        # FASE 3: VALIDAÇÃO - Revisão da resposta
        print("🔍 Fase 3: Validação e revisão...")
        validacao_task = create_validacao_task(
            agentes['coordenador'], 
            str(resposta_especialista), 
            consulta_usuario
        )
        
        crew_validacao = Crew(
            agents=[agentes['coordenador']],
            tasks=[validacao_task],
            verbose=True
        )
        
        resultado_validacao = crew_validacao.kickoff()
        print("✅ Processo completo!")

        # Formatação da resposta final
        resposta_final = f"""## 🏛️ Assistente Jurídico IA - Portugal

### 🎯 Área do Direito: {area_nome}

### 📋 Resposta Jurídica:
{resposta_especialista}

---

### ⚖️ AVISO LEGAL OBRIGATÓRIO
**A informação fornecida é de natureza geral e meramente informativa, não constituindo aconselhamento jurídico específico. Esta informação não substitui a consulta presencial a um advogado devidamente inscrito na Ordem dos Advogados. A aplicação da lei depende sempre das circunstâncias concretas e específicas de cada situação.**

---
*Sistema: Assistente Jurídico IA v1.0 | Especialização: Direito Português*"""

        return resposta_final

    except Exception as e:
        erro_msg = f"""## ❌ Erro no Processamento

**Pergunta:** {consulta_usuario}

**Erro:** {str(e)}

### 🔧 Possíveis Soluções:
1. Verifique se as APIs estão configuradas no arquivo .env
2. Certifique-se de que tem conexão à internet
3. Tente reformular a pergunta de forma mais específica

### ⚖️ AVISO LEGAL OBRIGATÓRIO
A informação fornecida é de natureza geral e meramente informativa, não constituindo aconselhamento jurídico específico. Esta informação não substitui a consulta presencial a um advogado devidamente inscrito na Ordem dos Advogados.

Para assistência jurídica profissional, consulte sempre um advogado qualificado."""
        
        return erro_msg

def modo_interativo():
    """
    Modo interativo para testar o sistema
    """
    print("🏛️ Assistente Jurídico IA - Portugal")
    print("=" * 50)
    print("💡 Digite 'sair' para terminar")
    print("💡 Digite 'exemplos' para ver perguntas exemplo")
    print("=" * 50)
    
    exemplos = [
        "Qual é o enquadramento do Crime de ameaça por mensagem?",
        "Como se faz a Constituição de sociedade por quotas?",
        "Descreve os diversos Elementos do crime de furto?",
        "Explicar os Direitos do inquilino particular?"
"""
        "Quais são os requisitos para um contrato de compra e venda ser válido?",
        "Se alguém me ameaçar de morte por mensagem, que crime é esse?",
        "Quais são as obrigações de uma sociedade por quotas?",
        "Como posso constituir uma empresa unipessoal por quotas?",
        "O que constitui o crime de furto em Portugal?"
"""
    ]
    
    while True:
        pergunta = input("\n📝 Sua pergunta jurídica: ").strip()
        
        if pergunta.lower() in ['sair', 'quit', 'exit']:
            print("👋 Obrigado por usar o Assistente Jurídico IA!")
            break
        elif pergunta.lower() == 'exemplos':
            print("\n📚 Exemplos de perguntas:")
            for i, exemplo in enumerate(exemplos, 1):
                print(f"{i}. {exemplo}")
            continue
        elif not pergunta:
            print("⚠️  Por favor, digite uma pergunta.")
            continue
        
        print("-" * 60)
        resultado = processar_consulta_juridica(pergunta)
        print("\n💬 Resposta do sistema:")
        print(resultado)
        print("=" * 60)

def main():
    """
    Função principal
    """
    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Verificar argumentos de linha de comando
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'interativo':
        modo_interativo()
        return
    
    # Teste padrão
    print("🚀 Testando Sistema Multi-Agente Completo...")
    print("=" * 60)
    
    # Inicializar e testar sistema
    agentes = inicializar_sistema()
    if agentes:
        print("✅ Sistema multi-agente inicializado com sucesso!")
        
        # Pergunta de teste (pode alterar aqui para testar diferentes áreas)
        pergunta_teste = "Quais são os requisitos para um contrato de compra e venda ser válido em Portugal?"
        
        print(f"\n📝 Pergunta de teste:")
        print(f"'{pergunta_teste}'")
        print("-" * 60)
        
        resultado = processar_consulta_juridica(pergunta_teste)
        print("\n💬 Resposta do sistema:")
        print(resultado)
    else:
        print("❌ Falha na inicialização do sistema.")

if __name__ == "__main__":
    main()