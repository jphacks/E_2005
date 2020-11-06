def wakati(text):
    import MeCab
    import io

    mecab_api = MeCab.Tagger('-Owakati')
    wakati_words = mecab_api.parse(text).split()
    return wakati_words

def remove_blank_of_files(dir_path, file_num):
    import io

    for num in range(1, file_num+1):
        with io.open(dir_path + str(num) + '.txt', 'r') as f:
            content = f.read().replace(' ', '')
            #print(content)
            #print("-----------------\n")

        with io.open(dir_path + str(num) + '.txt', 'w') as f:
            f.write(content)
            f.close()

def count_words(dir_path, file_num):
    import io

    words = {}

    for num in range(1, file_num+1):
        with io.open(dir_path + str(num) + '.txt', 'r') as f:
            wakati_words = wakati(f.name)
            for word in wakati_words:
                if word in words.keys():
                    words[word] += 1
                else:
                    words[word] = 1

            f.close()

    return words

def print_result(words):
    score_sorted = sorted(words.items(), key=lambda x:x[1], reverse=True)
    tmp_score = 0
    for word, score in score_sorted:
        if score != tmp_score:
            print('\n\n' + str(score) + ':\n' + word, end='')
            tmp_score = score
        else:
            print(', ' + word, end='')

    print('\n')

if __name__ == '__main__':
    print('This is text to wakati style process')

