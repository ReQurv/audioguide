from googletrans import Translator


def translateString(text, toLang, fromLang = "it"):
    translator = Translator()
    return translator.translate(text, src=fromLang, dest=toLang).text



