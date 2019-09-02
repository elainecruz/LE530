import pandas as pd
# Dataset from - https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

# Using the panda method read_table to read the SMSSpamCollection file uploaded and then renaming the columns to label and sms_message
df = pd.read_table('SMSSpamCollection', sep = '\t', names = ['label', 'sms_message'])

# Output printing out first 5 rows
print(df.head())


#Here I'm converting the values in the 'label' column to 0 or 1 (ham becoming 0 and spam becoming 1)
df['label'] = df.label.map({'ham':0, 'spam':1})

#Printing out number of rows and columns using 'shape'.
print(df.shape)


#Small sample array to understand the preprocessing techniques available to us when dealing with textual data.
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_case_documents = []

#Here there's a for that iterate through all the strings in documents and turns it all to lower case strings and then it adds to the previous array created(lower_case_documents)
for i in documents:
    lower_case_documents.append(i.lower())

print(lower_case_documents)



sans_punctuation_documents = []
import string


for i in lower_case_documents:
 
  #Auxiliar string that will have the string of lower_case_documents the for is on
  aux = ''

  # A for that iterates through the whole string so it checks if it's a punctuation charatcer and if it's not it adds in the auxiliar string
  for j in i:
    if(j.isalnum() or j==' '):
      aux+=j

  sans_punctuation_documents.append(aux)
    
print(sans_punctuation_documents)


preprocessed_documents = []


for i in sans_punctuation_documents:
   #Here the string i the for is at is tokenized and then the array of words is added to the preprocessed_documents array
   preprocessed_documents.append(i.split(' '))

print(preprocessed_documents)


frequency_list = []
import pprint
from collections import Counter

#A for that iterate through the elements in the preprocessed_documents array and counts the frequency of each word in this element and then adds the dictionary created to the list
for i in preprocessed_documents:
  frequency_list.append(Counter(i))
  
pprint.pprint(frequency_list)




