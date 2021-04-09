from plugin import plugin
import random


@plugin("give me advice")
def advice(jarvis, s):
    """
    Takes in a string, checks if its a question and returns a random response to the question.
    """ 
    answers = [
        "No",
        "Yes",
        "You Can Do It!",
        "I Cant Help You",
        "Sorry To hear That, But You Must Forget :(",
        "Keep It Up!",
        "Nice",
        "Dont Do It Ever Again",
        "I Like It, Good Job",
        "I Am Not Certain",
        "Too Bad For You, Try To Find Something Else To Do And Enjoy",
        "Time Will Pass And You Will Forget",
        "Dont Do It",
        "Do It",
        "Never Ask Me About That Again",
        "I Cant Give Advice Now I Am Sleepy",
        "Sorry I Cant Hear This Language",
        "Sorry But Your Question Does Not Make Sense"]

    greetings = "#################################################\n" \
                "#                   HELLO THERE!                #\n" \
                "#   Ask Me Question And I Will Give You Advice  #\n" \
                "# I Am Limited So Pick First Which Fits Context #\n" \
                "#################################################\n"

    jarvis.say(greetings)

    # validate question
    while True:
        question = input("Ask Me A Question: ").strip()
        if len(question) > 0 and question[-1] == '?':
            break

    # continue giving different answers until one makes sense.
    in_context = False
    while not in_context:
        # this line can generate an out of bound index
        randPos = random.randint(0, len(answers) - 1)
        jarvis.say(answers[randPos])
        while True:
            desire = input("Was This In Context? (Y/N) : ")
            if desire.strip().lower() == 'n':
                jarvis.say("Its A Pitty :( I'll Try Again!")
                break
            elif desire.strip().lower() == 'y':
                in_context = True
                jarvis.say("Good To hear! Happy To Advise You!")
                jarvis.say("Good Bye!")
                break