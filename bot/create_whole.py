from bot.models import db, Whole

def create_db():
    money_words = ['キャッシュ', 'カード']
    for word in money_words:
        whole_word = Whole(word=word, tag='money')
        db.session.add(whole_word)
        db.session.commit()
    
    job_words = ['警察', '暴力']
    for word in job_words:
        whole_word = Whole(word=word, tag='job')
        db.session.add(whole_word)
        db.session.commit()
    
    situation_words = ['逮捕', '職務']
    for word in situation_words:
        whole_word = Whole(word=word, tag='situation')
        db.session.add(whole_word)
        db.session.commit()
    
    promise_words = ['守秘', '義務']
    for word in promise_words:
        whole_word = Whole(word=word, tag='promise')
        db.session.add(whole_word)
        db.session.commit()
    
    person_words = ['個人', '情報']
    for word in person_words:
        whole_word = Whole(word=word, tag='person')
        db.session.add(whole_word)
        db.session.commit()


if __name__ == '__main__':
    create_db()

