import configparser

class Config_loader:

    def __init__(self):
        self.__config = self.load_config()
        self.__text = self.__config['Song']['Text_of_song']
        self.__path = self.__config['Song']['Path_to_song']

    def load_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config

    @property
    def get_text(self):
        return self.__text

    @property
    def get_path(self):
        return self.__path

Config_loader().load_config()