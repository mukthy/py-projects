from translate import Translator

# Opens the file and translates the text in the file to a specific language.
with open('translate.txt') as my_file:
    text = my_file.read()
    print(text)
    translator = Translator(to_lang='ja')
    translation = translator.translate(text)
print(translation)

# writes the translated text to the file.
with open('translated_text.txt', mode='w') as translated:
    translated_text = translated.write(translation)
