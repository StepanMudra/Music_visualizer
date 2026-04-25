from Configuration_loader import Configuration_loader
from DescriptionMaker import DescriptionMaker
from EmotionAnalyzer import EmotionAnalyzer
from APIHandler import APIHandler
class Engine:

    def run(self):
        config_loader = Configuration_loader()
        emotion_analyzer = EmotionAnalyzer()
        description_maker = DescriptionMaker()

        text = config_loader.get_text
        path = config_loader.get_path
        key = config_loader.get_api_key
        number_of_iterations = config_loader.get_number_of_iterations
        emotion_analysis_model = config_loader.get_emotion_analysis_model
        text_model = config_loader.get_text_model
        image_model = config_loader.get_image_model

        describer_first_template = config_loader.get_describer_first
        describer_template = config_loader.get_describer
        critic_template = config_loader.get_critic

        text_analysis = emotion_analyzer.analyze_emotion(text, emotion_analysis_model)
        music_analysis= emotion_analyzer.analyze_music(path)

        api_handler = APIHandler(key)

        print("Text analysis")
        print(text_analysis)
        print("Music analysis")
        print(music_analysis)
        print("Text")
        print(text)
        describer_first_prompt = description_maker.make_first_describer_prompt(describer_first_template, text_analysis, music_analysis, text)
        i = 1
        response_describer = api_handler.get_text_response(describer_first_prompt, text_model)
        print("First describer response")
        print(response_describer)
        while i < int(number_of_iterations):
            critic_prompt = description_maker.make_critic_prompt(critic_template, response_describer)
            response_critic = api_handler.get_text_response(critic_prompt, text_model)
            print("Response critic")
            print(response_critic)
            describer_prompt = description_maker.make_describer_prompt(describer_template, response_describer, response_critic, text_analysis, music_analysis, text)
            response_describer = api_handler.get_text_response(describer_prompt, text_model)
            print("Response describer")
            print(response_describer)
            i += 1

        image_url = api_handler.get_image_response(response_describer, image_model)
        print(image_url)

Engine().run()

