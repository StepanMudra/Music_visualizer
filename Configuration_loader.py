import configparser
from dotenv import load_dotenv
import os

class Configuration_loader:

    def __init__(self):
        load_dotenv()

        self.__config = self.load_config()

        self.__text = self.__config['Song']['Text_of_song']
        self.__path = self.__config['Song']['Path_to_song']

        self.__emotion_analysis_model = self.__config['Models']['Emotions']
        self.__text_model = self.__config['Models']['Text']
        self.__image_model = self.__config['Models']['Image']

        self.__describer_first = self.__config['Prompts']['Describer_first']
        self.__describer = self.__config['Prompts']['Describer']
        self.__critic = self.__config['Prompts']['Critic']

        self.__api_key = os.getenv("API_key")

    def load_config(self):
        config = configparser.ConfigParser(
            comment_prefixes=';',
            inline_comment_prefixes=';'
        )
        config.read('config.ini')
        return config

    @property
    def get_text(self):
        return self.__text

    @property
    def get_path(self):
        return self.__path

    @property
    def get_emotion_analysis_model(self):
        return self.__emotion_analysis_model

    @property
    def get_api_key(self):
        return self.__api_key

    @property
    def get_text_model(self):
        return self.__text_model

    @property
    def get_image_model(self):
        return self.__image_model

    @property
    def get_describer_first(self):
        return self.__describer_first

    @property
    def get_describer(self):
        return self.__describer

    @property
    def get_critic(self):
        return self.__critic

Configuration_loader().load_config()