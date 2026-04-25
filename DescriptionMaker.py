class DescriptionMaker:

    def make_first_describer_prompt(self, template, emotion_result, music_result, text):
        return template.format(emotions=emotion_result, music=music_result, text=text)

    def make_describer_prompt(self, template, description, feedback, emotion_result, music_result, text):
        return template.format(description=description, feedback=feedback, emotions=emotion_result, music=music_result, text=text)

    def make_critic_prompt(self, template, description):
        return template.format(description=description)