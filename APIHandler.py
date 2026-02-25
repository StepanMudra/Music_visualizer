from openai import OpenAI

class APIHandler:
    def __init__(self, key):
        self.__client = self.create_client(key)

    def create_client(self, key):
        return OpenAI(api_key=key)

    @property
    def get_client(self):
        return self.__client