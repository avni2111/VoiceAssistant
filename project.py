import pyttsx3 as p
import speech_recognition as sr
from seleniumWeb import infow
from Music_Player import MusicPlayer
import randfacts
import requests
from ss import key

# Flag to track whether a video is currently playing
is_video_playing = False

def speak(text):
    engine = p.init()
    engine.say(text)
    engine.runAndWait()

def get_user_input(recognizer, source, threshold, ambient_noise_adjustment):
    recognizer.energy_threshold = threshold
    recognizer.adjust_for_ambient_noise(source, ambient_noise_adjustment)
    print("listening...")
    audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)

def get_news():
    api_address = f"https://newsapi.org/v2/everything?q=keyword&apiKey={key}"
    json_data = requests.get(api_address).json()

    if 'articles' in json_data:
        news_list = []
        for i in range(3):
            news_list.append(f"Number {i + 1}: {json_data['articles'][i]['title']}.")
        return news_list
    else:
        return ["Error in API response"]

def main():
    global is_video_playing  # Declare global variable

    speak("Hello. I am your Voice Assistant. How are you")

    with sr.Microphone() as source:
        r = sr.Recognizer()

        try:
            while True:
                text = get_user_input(r, source, 10000, 1.2)
                print("User said:", text)

                if all(word in text.lower() for word in ["what", "about", "you"]):
                    speak("I am having a good day today.")
                    speak("What can I do for you?")

                text2 = get_user_input(r, source, 10000, 1.2)
                print("User said:", text2)

                if "information" in text2:
                    speak("You need information related to which topic?")

                    infor = get_user_input(r, source, 10000, 1.2)
                    print("User said:", infor)
                    speak("Searching {} in Wikipedia".format(infor))
                    assist = infow()
                    result = assist.get_info(infor)

                    if result:
                        # Speak only the first three lines from Wikipedia
                        result_lines = result.split('\n')[:3]
                        result_text = ' '.join(result_lines)
                        speak(result_text)
                    else:
                        speak("Sorry, I couldn't retrieve information at the moment.")

                elif all(word in text2.lower() for word in ["play", "video"]):
                    speak("You want to play which video?")
                    video_query = get_user_input(r, source, 10000, 1.2)
                    print("User said:", video_query)

                    # Create an instance of the MusicPlayer class
                    assist = MusicPlayer()
                    assist.play_video(video_query)

                    # Set the flag to indicate video is playing
                    is_video_playing = True

                elif "news" in text2.lower():
                    speak("Sure, let me fetch the latest news for you.")
                    news_list = get_news()
                    speak("Here are the top 3 news headlines.")
                    for news_headline in news_list:
                        speak(news_headline)

                elif any(word in text2.lower() for word in ["facts", "fact"]):
                    fact = randfacts.get_fact()
                    print("Fact:", fact)
                    speak("Sure, here's a random fact for you.")
                    speak(fact)

                elif "exit" in text2.lower() or "close" in text2.lower():
                    if is_video_playing:
                        # If a video is playing, don't exit immediately
                        speak("You are currently playing a video. Please close the video manually when you are done.")
                    else:
                        speak("Goodbye!")
                        break

                # Reset the flag after handling the video play request
                is_video_playing = False

                speak("What can I do for you now?")

        except sr.UnknownValueError:
            print("Sorry, I did not get that. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
