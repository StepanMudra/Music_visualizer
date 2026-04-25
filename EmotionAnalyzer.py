import torch
from transformers import pipeline
import librosa

class EmotionAnalyzer:

    def analyze_emotion(self, text, model):
        # Vytvoření pipeline pro analýzu emocí
        emotion_classifier = pipeline("text-classification", model=model, top_k=None)
        # Analýza emocí
        emotions = emotion_classifier(text)
        return emotions

    def analyze_music(self, filename):
        y, sr = librosa.load(filename)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        harmonic, percussive = librosa.effects.hpss(y)
        chromagram = librosa.feature.chroma_cqt(y=harmonic, sr=sr)

        pitch_classes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        chroma_mean = chromagram.mean(axis=1)
        dominant_key = pitch_classes[chroma_mean.argmax()]

        major_profile = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
        minor_profile = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

        import numpy as np
        major_corr = np.corrcoef(chroma_mean, major_profile)[0, 1]
        minor_corr = np.corrcoef(chroma_mean, minor_profile)[0, 1]
        mode = "major" if major_corr > minor_corr else "minor"

        energy = float(np.mean(librosa.feature.rms(y=y)))
        energy_label = "high" if energy > 0.1 else "medium" if energy > 0.03 else "low"

        return (
            f"Tempo: {float(tempo[0]):.1f} BPM, "
            f"Key: {dominant_key} {mode}, "
            f"Energy: {energy_label} ({energy:.3f})"
        )