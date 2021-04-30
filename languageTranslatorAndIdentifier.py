from translate import Translator
from langdetect import detect
from iso639 import languages
language = input("Enter the language which you want to search ")
l = detect(language)
print(l)
if l == "en":
        print("Language is in default form : English")
q = input("Do you want to translate : ")
if q == "y" and "Y" :
        p = input("Enter the language code you want to translate in : ")
        print("Translating input language into desired language :")
        translator= Translator(from_lang=l,to_lang=p)
        translation = translator.translate(language)
        print (translation)
else :
         print("Language Remained Un-changed")
