"""Splitting text data into tokens."""

import re

def sent_tokenize(text):

  sentences = re.split('[^a-zA-Z0-9 ]', text)

  for i in range(len(sentences)):
    sentences[i] = sentences[i].strip()

  while "" in sentences:
    sentences.remove("")   

  return sentences


def word_tokenize(sent):
  words = re.split('[^a-zA-Z0-9]', sent)
    
  for i in range(len(words)):
    words[i] = words[i].strip()
  
  return words
    

def test_run():
    """Called on Test Run."""

    text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war? Is AI a bad thing?"
    print("--- Sample text ---", text, sep="\n")
    
    sentences = sent_tokenize(text)
    print("\n--- Sentences ---")
    print(sentences)
    
    print("\n--- Words ---")
    for sent in sentences:
        print(sent)
        print(word_tokenize(sent))
        print()  # blank line for readability


if __name__ == "__main__":
    test_run()