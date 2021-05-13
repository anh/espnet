import re

# Regular expression matching whitespace:
_whitespace_re = re.compile(r'\s+')

def collapse_whitespace(text):
      return re.sub(_whitespace_re, ' ', text)


def replace_uws(text):
    return text.replace(u'\xa0', u" ")


def lowercase(text):
    return text.lower()


def basic_cleaners(text):
    '''Basic pipeline'''
    text = lowercase(text)
    text = text.replace("-", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = replace_uws(text)
    text = collapse_whitespace(text)
    return text
