import re

class MyFunctions:
    def clean_string(str):
        str = re.sub(r"@\S+", "", str)
        str = str.replace('#', '')
        my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@'
        str = re.sub('[' + my_punctuation + ']+', ' ', str)  # strip
        str = re.sub(r"http\S+", "", str)
        str = str.replace('covid', '')
        str = str.replace('covid19', '')
        str = str.replace('covid-19', '')
        str = str.replace('coronavirus', '')
        str = ''.join(i for i in str if not i.isdigit())
        return str
