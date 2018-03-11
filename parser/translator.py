import json
import urllib2
from urllib import quote
import textwrap

import settings


class Translator:
    """"""

    def __init__(self, lang_from='en', lang_to='zh'):
        """"""
        self.lang_from = lang_from
        self.lang_to = lang_to

        self.url = settings.TRANSLATOR_URL
        self.headers = settings.TRANSLATOR_HEADERS
        self.text_limit = settings.TRANSLATOR_TEXT_LIMIT


    def translate(self, text):
        """"""
        if self.lang_from == self.lang_to: return text
        content = textwrap.wrap(text, self.text_limit, replace_whitespace=False)
        return ' '.join(self._translate_from_webapi(s) for s in content)


    def _translate_from_webapi(self, text):
        """"""
        text = quote(text, '')
        url = self.url % (text, self.lang_from, self.lang_to)
        request = urllib2.Request(url=url, headers=self.headers)
        content = urllib2.urlopen(request).read().decode('utf-8')
        return json.loads(content)['responseData']['translatedText']


if __name__ == '__main__':
    translator = Translator()
    word = translator.translate("This is a pen.")
    print word
