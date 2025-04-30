import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import os
from openai import OpenAI
import Musiclibrary  # Assuming your Music library is a separate module with song links
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize components
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Get Spotify API credentials from environment variables
client_id = os.getenv('SPOTIFY_CLIENT_ID')  # Set your Spotify client ID in the environment variable
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')  # Set your Spotify client secret in the environment variable
redirect_uri = "http://localhost:8888/callback"

# Spotify API Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-library-read user-read-playback-state user-modify-playback-state user-read-currently-playing"
))

# Get OpenAI API key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')  # Set your OpenAI API key in the environment variable
client = OpenAI(api_key=openai_api_key)

# News API Key (set in environment variable)
newsapi = os.getenv('NEWS_API_KEY')  # Set your News API key in the environment variable

def speak(text):
    """Speaks the provided text."""
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    """Processes commands using OpenAI API."""
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": command},
            ],
        )
        return completion.choices[0].message.content
    except Exception:
        return "I encountered an error connecting to AI."

def Processcommand(c):
    """Handles user commands."""
    c = c.lower()

    if "stop" in c:
        speak("Shutting down Jarvis.")
        exit(0)

    websites = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "facebook": "https://facebook.com",
        "spotify": "https://spotify.com",
        "twitter": "https://twitter.com",
        "instagram": "https://instagram.com",
        "linkedin": "https://linkedin.com",
        "reddit": "https://reddit.com",
        "github": "https://github.com",
        "netflix": "https://netflix.com",
        "amazon": "https://amazon.com",
        "yahoo": "https://yahoo.com",
        "bing": "https://bing.com",
        "wikipedia": "https://wikipedia.org",
        "stackoverflow": "https://stackoverflow.com",
        "whatsapp": "https://web.whatsapp.com",
        "discord": "https://discord.com",
        "telegram": "https://web.telegram.org",
    }

    # Handle website opening
    for key, url in websites.items():
        if f"open {key}" in c:
            speak(f"Opening {key}")
            webbrowser.open(url)
            return

    # Play music from the Music library
    if "play" in c:
        song = c.split("play", 1)[-1].strip()
        if song in Musiclibrary.music:
            link = Musiclibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        return

    # Play Music on Spotify
    if "play" in c and "spotify" in c:
        song_name = c.split("play")[-1].strip()
        
        if not song_name:
            speak("Please tell me the song name you want to play on Spotify.")
            return  # Wait for the song name in the next interaction

        # Search for the song on Spotify
        results = sp.search(q=song_name, limit=1, type='track')
        
        if results['tracks']['items']:
            song = results['tracks']['items'][0]
            track_url = song['external_urls']['spotify']
            speak(f"Playing {song_name} on Spotify")

            # Ensure there is an active device to play the song
            devices = sp.devices()
            if devices['devices']:
                # If a device is available, start playing the song
                try:
                    sp.start_playback(uris=[song['uri']])
                    webbrowser.open(track_url)
                    speak(f"Song is now playing: {song_name}")
                except Exception as e:
                    speak(f"Sorry, there was an error starting playback: {e}")
            else:
                speak("No active device found for playback. Please make sure a device is available.")
        else:
            speak(f"Sorry, I couldn't find {song_name} on Spotify.")
        return

    # Get news
    if "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])[:5]
                for article in articles:
                    speak(article["title"])
                return
        except Exception:
            speak("Sorry, I couldn't fetch the news at this moment.")
            return

    # Default OpenAI processing
    output = aiProcess(c)
    speak(output)

def listen_for_command():
    """Listens for commands and processes them."""
    recognizer = sr.Recognizer()

    print("Listening for 'Jarvis'...")

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=6)  # Timeout after 6 seconds
            word = recognizer.recognize_google(audio).lower()

            print(f"Heard: {word}")

            if "jarvis" in word:
                speak("Yes, how can I help?")
                return True
            else:
                print("Quietly listening...")
                return False

    except sr.UnknownValueError:
        # No speech detected, keep listening silently
        return False
    except sr.RequestError:
        # Problem with speech recognition service
        speak("Sorry, there was an error with the speech recognition service.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        if listen_for_command():  # Check if 'Jarvis' was recognized
            while True:
                # Listen for the first command after activation
                with sr.Microphone() as source:
                    print("Jarvis Active... Listening for command...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=6)
                    try:
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")  # Print the heard command

                        Processcommand(command)  # Process the command
                    except sr.UnknownValueError:
                        continue  # If nothing is heard, continue listening
                    except Exception as e:
                        print(f"Error: {e}")
