# アイリスの種類を判別する

sckit-learnのirisデータセットをニューラルネットワークで学習したモデルでアイリスの花の判別アプリを作成した。

## 目的
・ニューラルネットワークのコーディングの概要をつかむ。
・作成した機械学習モデルをアプリ化する。

## モジュール
### learning.ipynb
・pandas
・numpy
・matplotlib
・sklearn
・joblib （機械学習モデルの保存）

### app.py
・tkinter（GUI作成）
・joblib（機械学習モデルの読み込み）
・numpy


## 使用方法
`python app.py`で実行し、任意のアイリスの花のsepal length,sepal width,petal length,petar widthをそれぞれ入力し、Judgeボタンを押下。

（sepalはがく、petalは花弁）


機械学習モデルによって予測されたアイリスの種類がメッセージボックスで表示される。

![image](https://user-images.githubusercontent.com/82374688/155661894-47217af6-d0a4-43fb-9807-bb6b902cf98d.png)

![image](https://user-images.githubusercontent.com/82374688/155661916-013eb409-9d4c-43c5-bb3b-d1e1d774cfd9.png)

このアイリスはvirginicaらしい。

## 一言
ニューラルネットワークはブラックボックスと言われいてるだけに、他の機械学習の手法と違って

割とシンプルなコーディングになった。重回帰を使った時は正誤率が92％付近だったため、精度はいいことがわかる。

