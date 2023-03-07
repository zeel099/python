import random
hyy=["hello","hii","how are you"]
bye=["see you later","nothing much"]
while True:
        a=input()
        if a.lower() in hyy:
            answer=["helo sir","how can i help you","hyy"]
            print(random.choice(answer))
        elif a.lower() in bye:
            answer=["goodbye sir","have a good day","thank you"]
            print(random.choice(answer))
        else:
            print("sorry in can't understand")