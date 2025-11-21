"""
COBOL-Tutor - Interaktiver KI-gestützter COBOL-Kurs
Powered by Google Gemini (KOSTENLOS!)
"""
import streamlit as st
from ai_tutor import CobolTutor
from cobol_executor import CobolExecutor, install_cobol
from lessons import get_lesson, get_all_lesson_ids, get_lesson_titles
import os

# Seitenkonfiguration
st.set_page_config(
    page_title="COBOL-Tutor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session State initialisieren
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'current_lesson_id' not in st.session_state:
    st.session_state.current_lesson_id = '1_basics'
if 'user_code' not in st.session_state:
    st.session_state.user_code = ""
if 'cobol_installed' not in st.session_state:
    st.session_state.cobol_installed = False

# CSS für besseres Styling
st.markdown("""
<style>
    .stCodeBlock {
        background-color: #f0f2f6;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
</style>
""", unsafe_allow_html=True)

def initialize_cobol():
    """Initialisiert COBOL-Umgebung"""
    if not st.session_state.cobol_installed:
        with st.spinner("Prüfe COBOL-Installation..."):
            executor = CobolExecutor()
            if not executor.check_cobol_installed():
                st.warning("GnuCOBOL wird installiert, bitte warten...")
                if install_cobol():
                    st.success("✅ GnuCOBOL erfolgreich installiert!")
                    st.session_state.cobol_installed = True
                else:
                    st.error("❌ Installation fehlgeschlagen")
                    return False
            else:
                st.session_state.cobol_installed = True
    return True

def main():
    st.title("💻 COBOL-Tutor")
    st.markdown("*Lerne COBOL interaktiv mit KI-Unterstützung* 🆓")
    
    with st.sidebar:
        st.header("📚 Lektionen")
        
        lesson_titles = get_lesson_titles()
        selected_lesson = st.selectbox(
            "Wähle eine Lektion:",
            options=list(lesson_titles.keys()),
            format_func=lambda x: lesson_titles[x],
            key='lesson_selector'
        )
        
        if selected_lesson != st.session_state.current_lesson_id:
            st.session_state.current_lesson_id = selected_lesson
            st.session_state.user_code = ""
        
        st.divider()
        
        st.subheader("⚙️ Einstellungen")
        
        # Info Box für kostenlosen API-Key
        st.info("🆓 **100% Kostenlos!** Hole dir deinen Gemini API-Key:")
        st.markdown("[→ AI Studio](https://aistudio.google.com/app/apikey)")
        
        api_key = st.text_input(
            "Google Gemini API-Key:",
            type="password",
            value=os.getenv('GEMINI_API_KEY', ''),
            help="Kostenloser API-Key von https://aistudio.google.com/app/apikey"
        )
        
        if api_key:
            os.environ['GEMINI_API_KEY'] = api_key
        
        st.divider()
        st.markdown("### 💡 Tipps")
        st.markdown("""
        - Stelle Fragen an den KI-Tutor
        - Probiere den Code aus
        - Fehler sind Lernchancen!
        - Nutze die Hinweis-Funktion
        """)
        
        st.divider()
        st.caption("🤖 Powered by Google Gemini")
    
    lesson = get_lesson(st.session_state.current_lesson_id)
    
    if lesson:
        st.header(lesson['title'])
        
        tab1, tab2, tab3, tab4 = st.tabs(["📖 Theorie", "💻 Code-Editor", "🎯 Übung", "💬 KI-Tutor"])
        
        with tab1:
            st.markdown(lesson['description'])
            st.subheader("Beispiel:")
            st.code(lesson['example'], language='cobol')
            
            if st.button("🤖 Beispiel erklären lassen", key='explain_example'):
                tutor = CobolTutor()
                with st.spinner("Tutor denkt nach..."):
                    explanation = tutor.analyze_code(lesson['example'])
                    st.info(explanation)
        
        with tab2:
            st.subheader("Probiere es selbst:")
            
            st.info("💡 **Tipp:** Einrückungen sind im Free-Format egal! Du kannst den Code einfach kopieren und ohne Anpassung ausführen.")
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                user_code = st.text_area(
                    "Dein COBOL-Code:",
                    value=st.session_state.user_code,
                    height=300,
                    key='code_editor'
                )
                st.session_state.user_code = user_code
            
            with col2:
                st.markdown("**Aktionen:**")
                
                if st.button("▶️ Code ausführen", type="primary"):
                    if user_code.strip():
                        if initialize_cobol():
                            executor = CobolExecutor()
                            with st.spinner("Kompiliere und führe aus..."):
                                result = executor.execute_cobol(user_code)
                                
                                if result['success']:
                                    st.markdown('<div class="success-box">✅ Erfolgreich ausgeführt!</div>', 
                                              unsafe_allow_html=True)
                                    st.code(result['output'], language='text')
                                else:
                                    st.markdown(f'<div class="error-box">❌ Fehler bei {result["stage"]}</div>', 
                                              unsafe_allow_html=True)
                                    st.code(result['error'], language='text')
                    else:
                        st.warning("Bitte gib Code ein!")
                
                if st.button("🔍 Code analysieren"):
                    if user_code.strip():
                        tutor = CobolTutor()
                        with st.spinner("Analysiere..."):
                            feedback = tutor.analyze_code(user_code)
                            st.info(feedback)
                    else:
                        st.warning("Bitte gib Code ein!")
                
                if st.button("🗑️ Zurücksetzen"):
                    st.session_state.user_code = ""
                    st.rerun()
                
                if st.button("📋 Beispiel laden"):
                    st.session_state.user_code = lesson['example']
                    st.rerun()
        
        with tab3:
            if 'exercise' in lesson:
                exercise = lesson['exercise']
                
                st.subheader("🎯 Aufgabe:")
                st.info(exercise['task'])
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("💡 Hinweis anzeigen"):
                        tutor = CobolTutor()
                        with st.spinner("Generiere Hinweis..."):
                            hint = tutor.get_hint(exercise, st.session_state.user_code)
                            st.success(hint)
                
                with col2:
                    if st.button("👀 Lösung anzeigen"):
                        st.warning("Versuche es erst selbst! 😊")
                        with st.expander("Lösung (klicke um anzuzeigen)"):
                            st.code(exercise['solution'], language='cobol')
                
                st.subheader("Deine Lösung:")
                exercise_code = st.text_area(
                    "Schreibe deinen Code hier:",
                    value=st.session_state.user_code,
                    height=250,
                    key='exercise_code'
                )
                
                if st.button("✅ Lösung prüfen", type="primary"):
                    if exercise_code.strip():
                        if initialize_cobol():
                            executor = CobolExecutor()
                            with st.spinner("Prüfe deine Lösung..."):
                                result = executor.execute_cobol(exercise_code)
                                
                                tutor = CobolTutor()
                                feedback = tutor.get_response(
                                    f"Der Schüler hat folgende Lösung für die Aufgabe '{exercise['task']}' eingereicht. Gib konstruktives Feedback!",
                                    code_result=result
                                )
                                
                                if result['success']:
                                    st.success("🎉 Dein Code läuft!")
                                    st.code(result['output'], language='text')
                                else:
                                    st.error("Es gibt noch Fehler:")
                                    st.code(result['error'], language='text')
                                
                                st.subheader("Feedback vom Tutor:")
                                st.info(feedback)
                    else:
                        st.warning("Bitte schreibe erst Code!")
        
        with tab4:
            st.subheader("💬 Frag den KI-Tutor")
            
            for msg in st.session_state.conversation_history:
                if msg['role'] == 'user':
                    with st.chat_message("user"):
                        st.write(msg['content'])
                else:
                    with st.chat_message("assistant"):
                        st.write(msg['content'])
            
            user_question = st.chat_input("Stelle eine Frage zu COBOL...")
            
            if user_question:
                with st.chat_message("user"):
                    st.write(user_question)
                
                st.session_state.conversation_history.append({
                    'role': 'user',
                    'content': user_question
                })
                
                tutor = CobolTutor()
                with st.spinner("Tutor denkt nach..."):
                    response = tutor.get_response(
                        user_question,
                        conversation_history=st.session_state.conversation_history[:-1],
                        current_lesson=lesson
                    )
                
                with st.chat_message("assistant"):
                    st.write(response)
                
                st.session_state.conversation_history.append({
                    'role': 'assistant',
                    'content': response
                })
                
                st.rerun()
            
            if st.button("🗑️ Chat leeren"):
                st.session_state.conversation_history = []
                st.rerun()
    
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <small>COBOL-Tutor | Powered by Google Gemini AI 🆓</small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
