# 詐欺チェッカー

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2020/09/JPHACKS2020_ogp.jpg)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要
### 背景
近年、オレオレ詐欺をはじめとした**特殊詐欺**の発生件数が増加している。日本全国での特殊詐欺の被害額は1年で**300億円**(2019年)を超えており(※1)、また、年々手口も多様化している。<br>
しかし主な対策方法は大きく変化しておらず、認知はされているものの確実な方法であるとは言い難い。7割以上の人は誰にも相談せずに行動してしまうというデータ(※2)もあり、多くの家庭で核家族化が進行している現代では、今後も特殊詐欺による被害は大きくなることが予想される。<br>
本アプリは電話内容を直接解析し、離れている家族と共有することで特殊詐欺に対して抜本的な解決方法をアプローチする。<br>

(※1)
令和元年における特殊詐欺認知・検挙状況等について（確定値版）
https://www.npa.go.jp/bureau/criminal/souni/tokusyusagi/hurikomesagi_toukei2019.pdf

(※2)
「オレオレ詐欺」の9割は「固定電話」への着信から始まる
https://seniorguide.jp/article/1171332.html

  2020/11/07現在
### 製品説明
本アプリは電話内容を音声認識によって解析し、危険度を測定する。その測定結果をLINEを通して予め登録されたユーザーに送信し、電話内容とその危険性を家族全体で共有することが可能となる。
### DEMO
下記リンクを参照<br>
https://youtu.be/3bterZYzVZ8


### 特長
#### 特長1　親族に確認を取るといった従来の解決策では手間がかかり、実践しづらいものであった。本アプリは自動で電話内容が共有されるためユーザーの手を煩わせることがない。
#### 特長2　似たような手法としてかかってきた電話番号で詐欺を検知する方法もあるが、この場合新規の詐欺電話に対応できない。本アプリは電話内容から直接解析を行うため、抜本的な解決を行うことができる。
#### 特長3　LINEを用いて電話内容を共有することでユーザーがより手軽に利用できる。
#### 特長4　被害者のほとんどが「自分が詐欺電話に引っかかっていると気付かなかった」というケースが多く問題となっているが、本アプリは危険度判定と家族による電話内容の吟味により、詐欺の見落としを防げる。

### 解決出来ること
高齢者世帯でも親族と簡単に電話内容を共有することで、オレオレ詐欺等の特殊詐欺の被害を防止できる。
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
* 警視庁のサイト等から集めた50以上のサンプルデータを抽出、反映。
* ユーザーが行うべき作業を極力減らすことにより、利便性を向上させた。
* LINEを用いて危険度を共有するため、メールに比べ、見逃しにくくなった。
* フィードバックシステムによって、ユーザーに応じた危険度を測定できる。

## 開発技術
### 活用した技術
* python 

#### API・データ
* Google Cloud Speech-to-Text

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


