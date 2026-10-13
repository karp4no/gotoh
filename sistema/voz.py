import pyttsx3
import threading

class VoiceEngine:
    def __init__(self):
        self.enabled = False

    def falar(self, texto: str):
        if not self.enabled or not texto:
            return

        def _executar_voz():
            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', 160)
                engine.setProperty('volume', 0.9)
                
                # Seleciona voz PT se disponível
                for voice in engine.getProperty('voices'):
                    if "pt" in voice.id.lower() or "brazil" in voice.id.lower():
                        engine.setProperty('voice', voice.id)
                        break

                import re
                texto_limpo = re.sub(r'https?://\S+', '', texto)
                texto_limpo = re.sub(r'[*_#~`•🔗]', '', texto_limpo).strip()

                if texto_limpo:
                    engine.say(texto_limpo)
                    engine.runAndWait()
            except Exception:
                pass

        # Roda a voz totalmente isolada
        t = threading.Thread(target=_executar_voz, daemon=True)
        t.start()

voz = VoiceEngine()
