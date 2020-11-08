# 詐欺チェッカー

[![IMAGE ALT TEXT HERE](https://lh3.googleusercontent.com/ECora-SQQqrSwWJ_nzx-gRYtwUHxxURkoRBf2Zm-ujNO7nzhsvb0uUgGQiBTDc0ZQb_W-m6Kn6Oy0QgLEhagJMzkyRaBibFgxM-BHhlPusILFwH7x8f4XZ4du638b5q1UK1LQKYmoQW7SfSyn2A7gYFx66NMEzVQ3oE77z1KU6rZAdFOkUdkjxm24Z8qU7_5yxNwWv1EcLMDJfP_VlLPCpvF-70iVt-qb5TJKCDoKS2WKjpgGsc5NvG3aktxQ4awf_JBsx2fvUSe3KfUUplZ3DpBd5HyIWcykylzUEtbJSR6jHM3CPjoR9AbG9JGShy3sjp8Tq9PKmhwOoW23fdisgVKwa-eSXPPIFDWxv3v3A946MgSaJhGIlDN-G_yPQsTYIGu8cGjbrYQRUNxthV5hoeXWlBxvnH1_C3jYRlV4Wx6MPNTsi9PmoTaQNNwNaCCKP3BYJyx0uiyjZP-IkXS0updDAts-lW2qKaWC9vTZB-vdVEavm6wh6I0egK8U10cw-icboi6PSApPCfox8-KJhoiKhfyt_bh_wRtCnZRk9qyN8obLYP8cmJxRCm-3DiPBAuEJs0p9B2pwjQ4Dr2NgtjJo_dlb6sWz_LKDtdh4992qDZFevKS09BZ5V7ufR5dO5creN_rQo2l6beNAcRCTGXBV9-kgULr_oWXzQZpUy1qY-MaSa5htdONlllYJg=w960-h540-no?authuser=0)](https://youtu.be/7Tp2uuxSwVc)



# 詐欺×Tech
## 製品概要
### 背景
近年、オレオレ詐欺をはじめとした**特殊詐欺**の発生件数が増加している。日本全国での特殊詐欺の被害額は1年で**300億円**(2019年)を超えており(※1)、また、年々手口も多様化している。<br>
しかし主な対策方法は大きく変化しておらず、認知はされているものの確実な方法であるとは言い難い。7割以上の人は誰にも相談せずに行動してしまうというデータ(※2)もあり、多くの家庭で核家族化が進行している現代では、今後も特殊詐欺による被害は大きくなることが予想される。<br>
本アプリは電話内容を直接解析し、離れている家族と共有することで特殊詐欺に対して抜本的な解決方法をアプローチする。<br>

(※1)
令和元年における特殊詐欺認知・検挙状況等について（確定値版）<br>
https://www.npa.go.jp/bureau/criminal/souni/tokusyusagi/hurikomesagi_toukei2019.pdf

(※2)
「オレオレ詐欺」の9割は「固定電話」への着信から始まる<br>
https://seniorguide.jp/article/1171332.html<br><br>
 (2020/11/07現在)
### 製品説明
本アプリは電話内容を音声認識によって解析し、危険度を測定する。その測定結果をLINEを通して予め登録されたユーザーに送信し、電話内容とその危険性を家族全体で共有することが可能となる。
##### １．チェッカーIDとLINEbotの追加
チェッカーIDは通話録音デバイスにあり、通話をチェックされる人ごとに用意されています。  
家族など身の回りの人はLINEbotを追加しチェッカーIDを登録します。  
チェッカーIDはデバイスごとにデータを保存したりLINEbotで通知するユーザを決定したりするのに用います。
##### 2. 通話の録音・テキスト変換
電話がかかるとユーザーはデバイスで録音を開始します。録音した音声はCloud Speech-to-Textでテキストに変換されサーバーに送信されます
##### 3. 形態素解析・危険度の測定
送信されたテキストに対し、形態素解析を行い後ほど説明する _危険ワード_ の数で危険度を測定します。
##### 4. LINEbotで通知
測定結果とフィードバックリンクをLINEbotで家族に通知します。これによって家族は危険な通話に気づくことができます。
##### 5. 通話内容の確認・フィードバック
フィードバックリンクにアクセスすると、通話から「検出された危険ワード」と「その他のワード」が表示されます。
それらの結果からユーザは「危険ワード」を新たにフィードバックデータとして追加することができます。
フィードバックデータはその家族間専用のデータとして以降の測定に即座に反映されます。

##### 危険ワードについて
危険ワードは
1. アプリ上の全体データ
2. 個人のフィードバックデータ
の2種類があります。   
今回、1の全体データには警察が公開している50近くの通話データを分析し、[頻繁に登場するもの](https://github.com/jphacks/E_2005/wiki/%E5%8D%B1%E9%99%BA%E3%81%AA%E3%83%AF%E3%83%BC%E3%83%89%EF%BC%88%E9%A0%85%E7%9B%AE%E5%88%A5%EF%BC%89)を設定しました。

### DEMO
下記リンクを参照(youtube)<br>
https://youtu.be/7Tp2uuxSwVc


### 特長
#### 特長1　危険度測定では警察が公開している50近くのサンプルデータから抽出した結果により判定を行っている。また、ユーザーのフィードバックにより個別に危険なワードを設定できるため。より精度の高い判定を可能にしている。
#### 特長2　似たような手法としてかかってきた電話番号で詐欺を検知する方法もあるが、この場合新規の詐欺電話に対応できない。本アプリは電話内容から直接解析を行うため、抜本的な解決を行うことができる。
#### 特長3　LINEを用いて電話内容を共有することでユーザーがより手軽に利用できる。
#### 特長4　被害者のほとんどが「自分が詐欺電話に引っかかっていると気付かなかった」というケースが多く問題となっている(※3)が、本アプリは危険度判定と家族による電話内容の吟味により、詐欺の見落としを防げる。
#### 特長5　親族同士で予め合言葉を決めておくといった従来の解決策では手間がかかり、実践しづらいものであった。本アプリは自動で電話内容が共有されるためユーザーの手を煩わせることがない。

(※3)
昨年の特殊詐欺被害者アンケート結果　県警<br>
http://www.nagano-np.co.jp/articles/62622<br><br>

### 解決出来ること
通話内容を録音・解析して危険度を測定、家族にLINEで通知することで、オレオレ詐欺等の特殊詐欺の被害を防止できる。
### 今後の展望
技術的な展望は以下の通り。

* 現在外部のマイクから音を拾っているが、受話器から直接音声データを拾得する。
* 危険度測定の精度を向上させる。
* 信頼度が一定の水準に達したら警察に直接通報できる機能を搭載する。
* フィードバックシステムの向上

また、応用例として

* 録音できるあらゆる犯罪の防止。
* インターホン等に設置し悪質な勧誘、訪問販売の検知、対応。

### 注力したこと（こだわり等）
* 警察が公開している50以上のサンプルデータを抽出、反映。
* ユーザーが行うべき作業を極力減らすことにより、利便性を向上させた。
* LINEを用いて危険度を共有するため、メールに比べ、見逃しにくくなった。
* フィードバックシステムによって、ユーザーに応じた危険度を測定できる。

## 開発技術
### 活用した技術
* python 
* 音声テキスト変換
* 形態素解析
* データベース
* LINEbot

#### API・データ
* Google Cloud Speech-to-Text
* [実際の詐欺の通話記録](https://www.police.pref.chiba.jp/seisoka/safe-life_fraud-audio.html)

#### フレームワーク・ライブラリ・モジュール
* Flask
* mecab-python3
* unidic-lite
* line-bot-sdk
* sqlalchemy
* psycog2

#### デバイス
* USBマイク

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 音声検出によるデータの危険度測定機能
* フィードバックシステム


