import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import youtube

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    try:
        if "open" in command:
            website = command.replace("open", "").strip()
            url = f"https://{website}.com"
            speak(f"Wait sir  , I am opening {website} ")
            webbrowser.open(url)

    except Exception as e:
        speak("Sorry, the word 'open' is missing.")
        print(f"Error: {e}")

def Play_music(command):
    try:
        if "play" in command:
            name_music = command.replace("play", "").strip()
            check_music = False
            
            for i in musiclibrary.music:
                if name_music in i.lower():
                    music_url = musiclibrary.music[i]
                    speak(f"Playing {name_music} from YouTube")
                    webbrowser.open(music_url)
                    check_music = True
                    break
            
            if not check_music:
                # If not found in the library, try to add it
                added_title = youtube.add_music_to_library(name_music)
                if added_title:
                    # Play the music after adding it
                    music_url = musiclibrary.music[added_title]
                    speak(f"Playing {added_title} from YouTube")
                    webbrowser.open(music_url)
                else:
                    speak(f"No music with the name {name_music} can be found in the playlist.")
    except Exception as e:
        speak("An error occurred while trying to play the music.")
        print(f"Error: {e}")

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)  # Helps reduce noise interference
                print("Listening for activation word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

            activate_jarvis = recognizer.recognize_google(audio).lower()
            print(f"Detected: {activate_jarvis}")

            if "jarvis" in activate_jarvis:
                speak("Jarvis activated. How can I help you?")
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio).lower()
                print(f"Command: {command}")

                if "shutdown" in command:
                    speak("Shutting down in 3, 2, 1. Goodbye!")
                    break
                
                process_command(command)
                Play_music(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            speak(f"API request error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
