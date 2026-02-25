from Configuration_loader import Configuration_loader
from EmotionAnalyzer import EmotionAnalyzer
from APIHandler import APIHandler
class Engine:

    def run(self):
        config_loader = Configuration_loader()
        emotion_analyzer = EmotionAnalyzer()
        text = config_loader.get_text
        path = config_loader.get_path
        key = config_loader.get_api_key
        emotion_analysis_model = config_loader.get_emotion_analysis_model
        text_analysis = emotion_analyzer.analyze_emotion(text, emotion_analysis_model)
        music_analysis= emotion_analyzer.analyze_music(path)
        api_handler = APIHandler(key)
Engine().run()


# Text k analýze
text = """
text
"""


analyzator = EmotionAnalyzer()


# Generování textového popisu
response_image = client.images.generate(
    model="dall-e-3",
    prompt=prompt_image,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response_image.data[0].url
print(image_url)