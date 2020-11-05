def wakati():
    import MeCab
    import io

    mecab_api = MeCab.Tagger('-Owakati')
    with io.open('proken.txt', 'r') as f:
        content = f.read()
        wakati_words = mecab_api.parse(content).split()

        print(wakati_words)
        return wakati_words

if __name__ == '__main__':
    wakati()

