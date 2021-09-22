from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

print("Hello, I'm Mr. Robot and I'm a simple bot.")
print("You can talk to me by writing into console, then pressing enter.")
print("If you wish to end the conversation, simply type 'bye' and press enter.\n")

print("So, this is start of our conversation. How are you?")

conll = ConllExtractor()

while (user_in := input(">")) != "bye":
    user_in_blob = TextBlob(user_in, np_extractor=conll)

    if user_in_blob.polarity <= -0.5:
        response = "Oh dear, that sounds bad."
    elif user_in_blob.polarity <= 0:
        response = "Hmm, that's not great."
    elif user_in_blob.polarity <= 0.5:
        response = "Well, that sounds positive."
    elif user_in_blob.polarity <= 1:
        response = "Wow, that sounds great."

    if user_in_blob.find("why") >= 0:
        response = f"Becasue universe works like that."

    np = user_in_blob.noun_phrases

    if np:
        response = f"{response} Can you tell me more about {np[0].pluralize()}?"

    print(response)

print("It was nice talking to you, bye.")