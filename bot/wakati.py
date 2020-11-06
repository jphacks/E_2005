def wakati(text):
    import MeCab
    import io

    mecab_api = MeCab.Tagger('-Owakati')
    wakati_words = mecab_api.parse(text).split()
    return wakati_words

if __name__ == '__main__':
    print('This is text to wakati style process')

