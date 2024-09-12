import requests
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

FIRST_RUN = False
MIN_SIMILARITY = 0.3
api_key = "<key here>"

def setup():
    """first time running the script"""
    nltk.download('popular')  # This command downloads the most popular datasets and models
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger_eng')

    # Load the installed model
    nlp = spacy.load('en_core_web_sm')

    # Process a text
    doc = nlp("Hello world, this is a test.")
    print([(w.text, w.pos_) for w in doc])  # Prints the text and the part of speech


def preprocess(input_sentence):
    """Tokenize input and assign part-of-speech tags"""
    words = word_tokenize(input_sentence) #breaks down the sentence into individual words or tokens
    pos_tags = pos_tag(words) #assigns part-of-speech tags to each token
    return pos_tags

def recognize_intent(tokens):
    """Matching to library of intent keywords"""
    greeting_keywords = ['hello', 'hi', 'greetings', 'hey']
    weather_keywords = ['weather', 'rain', 'wind']
    tokens = [token.lower() for token, pos in tokens]
    if any(token in greeting_keywords for token in tokens):
        return "greeting"
    elif any(token in weather_keywords for token in tokens):
        return "weather"
    return "unknown"  # Default intent if no known intent is found

def generate_response(intent, request):
    if intent == "greeting":
        return "Hello! How can I assist you today?"
    elif intent == "weather":
        for ent in request.ents:
            if ent.label_ == "GPE": # GeoPolitical Entity
                city = ent.text
                break
            else:
                return "You need to tell me a city to check."
            
        city_weather = get_weather(city)
   
        if city_weather is not None:
            return "In " + city + ", the current weather is: " + city_weather
        else:
            return "Something went wrong."
    else:
       return "I am not sure how to respond to that. Can you please rephrase?"

def get_weather(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

    response = requests.get(api_url)
    response_dict = response.json()
	
    weather = response_dict["weather"][0]["description"]

    if response.status_code == 200:
        return weather
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

def main():
    """
        Three main parts of the bot:
            1 Input Processing: This involves receiving the user's input and understanding it through tokenization and parsing.
            2 Intent Recognition: Identifying the user's intent based on the processed input.
            3 Response Generation: Crafting an appropriate response based on the recognized intent.
    """


    if FIRST_RUN:
        setup()
        quit()

    nlp = spacy.load('en_core_web_sm')
    # 1
    # input_sentence = "Hello, what's up?"
    input_sentence = "What is the weather in London?"

    processed_sentence = preprocess(input_sentence)
    print(processed_sentence)
    # 2
    intent = recognize_intent(processed_sentence)
    print(intent)
    # 3
    response = generate_response(intent, nlp(input_sentence))
    print(response)  




if __name__ == "__main__":
    main()