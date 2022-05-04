def bienvenido(lang):
    def bienvenido_spanish():
        return "Bienvenido"

    def bienvenido_english():
        return "Welcome"


    lang_func = {"spanish": bienvenido_spanish,
                 "english": bienvenido_english}
				 
    return lang_func[lang]

spanish = bienvenido("spanish")
print(spanish())

english = bienvenido("english")
print(english())