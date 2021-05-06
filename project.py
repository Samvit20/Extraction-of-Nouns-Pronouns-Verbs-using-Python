import spacy
nlp = spacy.load('en_core_web_sm')
file_name = 'text.txt'
list_N_P=[]
final_N_P=[]

file_text = open(file_name).read()
file_doc = nlp(file_text)
# print ([token.text for token in file_doc])

#NOUNS & PRONOUNS
for word in file_doc.noun_chunks:
    list_N_P.append(str(word))
print(list_N_P)

final_N_P = []
for i in list_N_P:
    if i not in final_N_P:
        final_N_P.append(i)

print(str(final_N_P))

#hello

print("\n")

print("Code Completed")