# menu_launcher.py - Menu interativo para escolher execução
import subprocess
import sys
import os

def show_menu():
    """Mostra menu de opções para executar"""
    print("\n" + "="*60)
    print("🚀 ASSISTENTE JURÍDICO AI - MENU DE DESENVOLVIMENTO")
    print("="*60)
    print()
    print("Escolha uma opção:")
    print()
    print("1. 🐍 Executar main.py (Teste do ambiente)")
    print("2. 🌐 Executar Streamlit (Interface web)")
    print("3. 🧪 Executar testes")
    print("4. 📋 Mostrar status do projeto")
    print("5. ❌ Sair")
    print()
    print("-"*60)

def run_main():
    """Executa main.py"""
    print("🐍 Executando main.py...")
    subprocess.run([sys.executable, "main.py"])

def run_streamlit():
    """Executa Streamlit"""
    print("🌐 Iniciando Streamlit...")
    print("Interface será aberta no navegador em http://localhost:8501")
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

def run_tests():
    """Executa testes (quando existirem)"""
    print("🧪 Executando testes...")
    if os.path.exists("tests"):
        subprocess.run([sys.executable, "-m", "pytest", "tests/"])
    else:
        print("⚠️  Pasta de testes ainda não existe.")
        print("💡 Será criada na próxima fase do desenvolvimento.")

def show_status():
    """Mostra status do projeto"""
    print("📋 STATUS DO PROJETO:")
    print("-" * 30)
    
    # Verificar arquivos essenciais
    files_to_check = [
        ("main.py", "Teste do ambiente"),
        ("app.py", "Interface Streamlit"),
        (".env", "Configurações"),
        ("requirements.txt", "Dependências"),
    ]
    
    for file, desc in files_to_check:
        exists = "✅" if os.path.exists(file) else "❌"
        print(f"{exists} {file:<20} - {desc}")
    
    print()
    print("📦 DEPENDÊNCIAS PRINCIPAIS:")
    
    try:
        import crewai
        print(f"✅ CrewAI: {crewai.__version__}")
    except ImportError:
        print("❌ CrewAI não encontrado")
    
    try:
        import streamlit
        print(f"✅ Streamlit: {streamlit.__version__}")
    except ImportError:
        print("❌ Streamlit não encontrado")
    
    # Verificar APIs
    print()
    print("🔑 CONFIGURAÇÃO DE APIS:")
    from dotenv import load_dotenv
    load_dotenv()
    
    groq_key = os.getenv('GROQ_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    
    print(f"{'✅' if groq_key and groq_key != 'your_groq_api_key_here' else '❌'} Groq API")
    print(f"{'✅' if openai_key and openai_key != 'your_openai_api_key_here' else '❌'} OpenAI API")

def main():
    """Menu principal"""
    while True:
        show_menu()
        
        try:
            choice = input("Digite sua escolha (1-5): ").strip()
            
            if choice == '1':
                run_main()
            elif choice == '2':
                run_streamlit()
            elif choice == '3':
                run_tests()
            elif choice == '4':
                show_status()
            elif choice == '5':
                print("👋 Até logo!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")
            
            input("\n📱 Pressione Enter para voltar ao menu...")
            
        except KeyboardInterrupt:
            print("\n👋 Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()