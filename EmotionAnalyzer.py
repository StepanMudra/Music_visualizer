from transformers import pipeline
import librosa

class EmotionAnalyzer:

    def analyze_emotion(self, text):
        # Vytvoření pipeline pro analýzu emocí
        emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base",
                                      return_all_scores=True)
        # Analýza emocí
        emotions = emotion_classifier(text)
        return emotions

    def analyze_music(self):
        filename = 'filename'
        y, sr = librosa.load(filename)

        # Extrakce základních hudebních rysů
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        harmonic, percussive = librosa.effects.hpss(y)
        chromagram = librosa.feature.chroma_cqt(y=harmonic, sr=sr)

        # Výpis základních rysů
        return tempo, chromagram