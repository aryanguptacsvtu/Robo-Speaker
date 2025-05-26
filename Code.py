import pyttsx3

if __name__ == "__main__":

    print("Welcome to RoboSpeaker🤖🤖\n---Created by Aryan")
    engine = pyttsx3.init()

    # 🔊 Set the voice (0 for male, 1 for female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Change Speaking Speed
    engine.setProperty('rate', 170) 

    while True:
        text = input("Enter what you want me to speak(or 'q' to quit): ")

        if text.lower() == "q":
            engine.say("Bye Bye friend")
            engine.runAndWait()
            break

        engine.say(text)
        engine.runAndWait()