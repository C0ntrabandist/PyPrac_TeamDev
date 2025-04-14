import gettext
import locale
import random

LOCALES = {
    ("ru_RU", "UTF-8"): gettext.translation("prog0", "po", ["ru"]),
    ("en_US", "UTF-8"): gettext.NullTranslations(),
}

def ngettext(*text):
    #if not text[0].startswith('a'):
    return random.choice(LOCALES[('ru_RU', 'UTF-8')], LOCALES[('en_US', 'UTF-8')]).ngettext(*text)
    #return LOCALES[locale.getlocale()].gettext(text)

#translation = gettext.translation('prog0', 'po', fallback=True)
#_, ngettext = translation.gettext, translation.ngettext
while msg := input().split():
    n = len(msg)
    print(ngettext("Entered {} word", "Entered {} words", n).format(n))
