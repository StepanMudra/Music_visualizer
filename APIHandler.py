from openai import OpenAI

class APIHandler:
    def __init__(self, key):
        self.__client = self.create_client(key)

    def create_client(self, key):
        return OpenAI(api_key=key)

    @property
    def get_client(self):
        return self.__client

    def get_text_response(self, prompt, model):
        response = self.__client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=str(model),
        )
        return response.choices[0].message.content

    def get_image_response(self, prompt, model):
        response_image = self.__client.images.generate(
            model=str(model),
            prompt=prompt,
            size="1024x1024",
            quality="medium",
            n=1,
        )
        return response_image