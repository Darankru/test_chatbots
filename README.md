Chatbot with python. Following this tutorial:

https://medium.com/@AlexanderObregon/how-to-build-a-simple-chatbot-with-python-4ce0742546a1


Steps:

- Install spcy and nltk
- ```nltk.download('popular')``` to download the most popular datasets and models
- ```python -m spacy download en_core_web_sm``` to download a small model
- The test should now ouput: [('Hello', 'INTJ'), ('world', 'NOUN'), (',', 'PUNCT'), ('this', 'PRON'), ('is', 'AUX'), ('a', 'DET'), ('test', 'NOUN'), ('.', 'PUNCT')]
- For the NLTK preprocessing, the following packages seem to be missing:
  - ```nltk.download('punkt_tab')```
  - ```nltk.download('averaged_perceptron_tagger_eng')```

https://www.digitalocean.com/community/tutorials/how-to-create-an-intelligent-chatbot-in-python-using-the-spacy-nlp-library