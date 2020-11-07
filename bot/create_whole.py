from bot.models import db, Whole

def create_db():
    money_words = ['キャッシュ', 'カード','現金','金','預金','貯金','万','円','通帳','口座','暗証番号','名義','名簿','銀行','出金','入金','手付','給付','慰謝','料','仮想','通貨','借金','担保','融資','債務']
    for word in money_words:
        whole_word = Whole(word=word, tag='money')
        db.session.add(whole_word)
        db.session.commit()
    
    job_words = ['警察', '暴力','金融','庁','警','交番','役所','役場','商事','会社','弁護']
    for word in job_words:
        whole_word = Whole(word=word, tag='job')
        db.session.add(whole_word)
        db.session.commit()
    
    situation_words = ['逮捕', '職務','事件','詐欺','被害','不審','怪しい','不正','補償','事故','補填','保険','投資','忘れ物','落とし物','株','示談','訴訟']
    for word in situation_words:
        whole_word = Whole(word=word, tag='situation')
        db.session.add(whole_word)
        db.session.commit()
    
    promise_words = ['守秘', '義務','駅','待ち合わせ','ATM','振込','受け渡し','手口']
    for word in promise_words:
        whole_word = Whole(word=word, tag='promise')
        db.session.add(whole_word)
        db.session.commit()
    
    person_words = ['個人', '情報','住所','家族','名前','本人','確認','娘','父','母','息子','近所','俺']
    for word in person_words:
        whole_word = Whole(word=word, tag='person')
        db.session.add(whole_word)
        db.session.commit()


if __name__ == '__main__':
    create_db()

