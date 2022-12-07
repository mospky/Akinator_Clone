# Akinator_Clone

## 概要
アキネーターのクローンサイトを作ってみたくなりました。

## プロジェクトの状態
下記URLの内容を画面に質問を表示し答えも表示できるようにしました。
https://qiita.com/Hanull/items/e7a3e4e675dfb3b44a7d

現状試す場合は、pythonの環境だけ整えて頂いて、recommend_org.pyを実行すればCLIレベルで確認できます。（もしくはflaskの環境を整えればGUIレベルで確認できるのですが...環境構築のReadMeを完成させるまでお待ちください。）

また、READMEは編集中です。  

## ToDo(全体)
- README作成
  - 環境作成について(win編/Mac編)
  - 実施方法
  - gitignore作成

## ToDo(実装)
  - モック作成
  - 答えの数が奇数の時
  - データの定義の仕方を確認(DBからjson形式で取得->pandas用に変換？)
  - DB接続（ここまでやって完成とする？）
  - 答えがなかった時の処理(一連の解答内容を一時的に保存する？答えを入力させてDBに保存)
  - ベイズの定理（解答者が間違う可能性を考慮したもの）

## 環境構築
  - 編集中
  - pythonを導入して、仮想環境作成して、pipでjinjaをinstallして...etc

## 仮想環境に入る/抜ける
  - ```source venv/bin/activate```
  - ```deactivate```

## app実施方法
  - appの場所を知らせてあげる  ```export FLASK_APP=flaskr```
  - app立ち上げ ```flask --debug run```
  - http://127.0.0.1:5000/recommend/ にアクセス
  - 質問が表示される。
  - 質問を増やす場合、/flaskr/recommend.py のdata定義に質問とかを追加するだけ。

## お役立ち情報
- FraskとかpythonとかNumpyの参考になるURLを載せる
- Fraskチュートリアル(https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/tutorial/index.html)
- 元ネタ（https://qiita.com/Hanull/items/e7a3e4e675dfb3b44a7d）
- ...随時更新します。

## Memo
- 
