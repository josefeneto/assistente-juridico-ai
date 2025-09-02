# test_setup.py
import sys
print(f"Python version: {sys.version}")

try:
    import crewai
    print(f"✅ CrewAI installed: {crewai.__version__}")
except ImportError:
    print("❌ CrewAI not installed")

try:
    import streamlit
    print(f"✅ Streamlit installed: {streamlit.__version__}")
except ImportError:
    print("❌ Streamlit not installed")

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv installed")
except ImportError:
    print("❌ python-dotenv not installed")

print("\n🎉 Setup verification completed!")