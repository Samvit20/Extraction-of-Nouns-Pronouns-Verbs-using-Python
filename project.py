import spacy
import textacy
from collections import Counter
nlp = spacy.load('en_core_web_sm')
file_name = 'text.txt'
list_N_P = []
final_N_P = []


# Reading the file
file_text = open(file_name).read()
file_doc = nlp(file_text)


#NOUNS & PRONOUNS
for word in file_doc.noun_chunks:
    list_N_P.append(str(word))

final_N_P = []

for i in list_N_P:
    if i not in final_N_P:
        final_N_P.append(i)

print("Nouns are: \n"+str(final_N_P))
# Word Frequency
words = [token.text for token in file_doc if not token.is_stop and not token.is_punct]
word_freq = Counter(words)

#5 commonly occurring words with their frequencies
common_words = word_freq.most_common(5)
print("\nCommon words are:")
print(common_words)

# Unique words
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print("\nUnique words are: ")
print(unique_words)

# VERBS
# pattern = [{'POS': 'VERB', 'OP': '?'},
#           {'POS': 'ADV', 'OP': '*'},
#           {'POS': 'VERB', 'OP': '+'}]
#file_doc2 = textacy.make_spacy_doc(file_text, lang='en_core_web_sm')
#verbs = textacy.extract.matches(file_doc2, pattern)
# for list in verbs:
#    print(list.text)


print("\n")

print("Code Completed")
