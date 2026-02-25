analyze = analyzator.analyze_emotion(text)

prompt = f"""
Generate a detailed description based on sentiment {analyze} where emotions are represented by colours 
and probability of emotions represents amount of colour of the emotion,
after it use tempo and chromagram for the atmosphere of the picture{analyze}.
"""









p = f"""#Identity:
            You are an expert for reading emotion from music defined by chromagram and tempo. Also you are master for expresing emotions from music. Also you can put colours emotions You describing it for a painter who will paint an art based on your description.
        #Task
            Make description for a painter based on These emotions {analyze} and these music {analyzator.analyze_music()} and text {text}"""


# Generování textového popisu
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": p,
        }
    ],
    model="gpt-4o",
)

print(response.choices[0].message.content)


history = response.choices[0].message.content
# Vytvoření promptu pro generování popisu
prompt_image = f"""
Generate an image based on description {response.choices[0].message.content}.
"""

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
k = 0
while(k < 3):
    pro = f"""#Identity:
                    You are my critics and you should provide me guidance to better describing emotion for painting.
              #Task:
                    Look at these: {history}"""
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pro,
            }
        ],
        model="gpt-4o",
    )
    print(response.choices[0].message.content)
    history = history + "Describtion of emotions: " +response.choices[0].message.content
    if k == 4:
        pro = f"""#Identity:
                    You are an expert for expresing and describing emotions and you should listen to critic and learn form past and critic points.
                   #Task:
                    {history} max length is 4000 characters."""
    else:
        pro = f"""#Identity:
                    You are an expert for expresing and describing emotions and you should listen to critic and learn form past and critic points.
                   #Task:
                    {history}"""
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pro,
            }
        ],
        model="gpt-4o",
    )
    print(response.choices[0].message.content)
    history = history + "Critics: " +response.choices[0].message.content
    k += 1

# Vytvoření promptu pro generování popisu
prompt_image = f"""
Generate an image based on description {response.choices[0].message.content}.
"""