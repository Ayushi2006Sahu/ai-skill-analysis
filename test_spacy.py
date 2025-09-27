import spacy

# English small model load karna
nlp = spacy.load("en_core_web_sm")

# Test sentence
doc = nlp("Ayushi is testing her resume analyzer.")

# Tokens print karna
print([token.text for token in doc])
