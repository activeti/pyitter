# 設計書

## ざっくりとした要件

* ユーザーはメールアドレスで会員登録ができること
* ユーザーは140文字以内で「つぶやき」が投稿できること
* ユーザーは他のユーザーをフォロー登録し、フォロワーのみの「つぶやき一覧」を表示できること
* ユーザーは「つぶやき」をお気に入り登録できること

memo
ユーザーの見た目を定義する: 画面構成図 & 画面遷移図
データの保存方法を定義する: ER図

## 画面構成図

## 画面遷移図

```puml


state registration
registration : 会員ティザー&登録
state session
session : ログイン
state tweet_index
tweet_index : つぶやき一覧(全つぶやき)
state user_index
user_index: ユーザ一覧
state user_setting
user_setting : 設定
state profile
profile: プロフィールページ
state follow
follow : フォロー一覧
state follower
follower : フォロワー一覧
state favorite
favorite: お気に入り一覧
state tweet_follower
tweet_follower: つぶやき一覧(フォロー一覧)

registration --> tweet_index
session --> tweet_index
tweet_index --> tweet_follower
profile --> follow
profile --> follower
profile --> favorite



```

### ER図