import random as rnd

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

print("Hello, I'm Mr. Robot and I'm a simple bot.")
print("You can talk to me by writing into console, then pressing enter.")
print("If you wish to end the conversation, simply type 'bye' and press enter.\n")

print("So, this is start of our conversation. How are you?")
while (user_in := input(">")) != "bye":
    print(rnd.choice(random_responses))