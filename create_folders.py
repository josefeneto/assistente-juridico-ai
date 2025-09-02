# create_folders.py - Script para criar estrutura de pastas
import os

def create_project_structure():
    """Cria toda a estrutura de pastas necessária"""
    
    folders = [
        "agents",
        "tasks", 
        "tools",
        "data",
        "data/codigos",
        "data/jurisprudencia",
        "utils",
        "tests"
    ]
    
    files_to_create = [
        "agents/__init__.py",
        "agents/coordenador.py",
        "agents/especialista_civil.py",
        "agents/especialista_penal.py",
        "agents/especialista_comercial.py",
        "agents/analista_documentos.py",
        "agents/redator_minutas.py",
        "tasks/__init__.py",
        "tasks/interpretacao.py",
        "tasks/analise.py",
        "tasks/redacao.py",
        "tools/__init__.py",
        "tools/search_legal.py",
        "tools/document_parser.py",
        "utils/__init__.py",
        "utils/helpers.py",
        "tests/__init__.py",
        "tests/test_agents.py"
    ]
    
    print("🏗️ Criando estrutura do projeto...")
    print("-" * 50)
    
    # Criar pastas
    for folder in folders:
        try:
            os.makedirs(folder, exist_ok=True)
            print(f"📁 Pasta criada: {folder}")
        except Exception as e:
            print(f"❌ Erro ao criar pasta {folder}: {e}")
    
    print("\n📄 Criando arquivos iniciais...")
    print("-" * 50)
    
    # Criar arquivos iniciais vazios
    for file_path in files_to_create:
        try:
            # Criar pasta pai se não existir
            parent_dir = os.path.dirname(file_path)
            if parent_dir and not os.path.exists(parent_dir):
                os.makedirs(parent_dir, exist_ok=True)
            
            # Criar arquivo se não existir
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8') as f:
                    if file_path.endswith('__init__.py'):
                        f.write('# -*- coding: utf-8 -*-\n')
                    else:
                        f.write('# -*- coding: utf-8 -*-\n\n# TODO: Implementar\n')
                print(f"📄 Arquivo criado: {file_path}")
            else:
                print(f"✅ Arquivo já existe: {file_path}")
                
        except Exception as e:
            print(f"❌ Erro ao criar arquivo {file_path}: {e}")
    
    print("\n🎉 Estrutura do projeto criada com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Implementar agentes CrewAI")
    print("2. Criar tarefas específicas")
    print("3. Integrar com interface Streamlit")
    print("4. Testar sistema completo")

if __name__ == "__main__":
    create_project_structure()
