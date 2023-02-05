# Akinator_Clone

## 概要
アキネーター<https://jp.akinator.com>のクローンサイトを作る。

下記URLの内容を画面に質問を表示し答えも表示できるようにしました。
https://qiita.com/Hanull/items/e7a3e4e675dfb3b44a7d

README編集中。  

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
### win10 win11 
- pythonの公式サイトから最新版をダウンロード<https://pythonlinks.python.jp/ja/index.html>
  （環境パス設定するようにチェックを入れる）
- 任意のdir作成
- git clone <レポジトリのURL>
- source venv/bin/activate
- ```pip install flask```
- ```pip install numpy```
- ```pip install pandas```

### Linux環境（Mac等）
- 編集中

## 使い方
  - ```source venv/bin/activate``` 仮想環境にはいる
  - ```deactivate```　仮想環境から抜ける
  - appの場所を知らせてあげる  ```export FLASK_APP=flaskr```
  - app立ち上げ ```flask --debug run```
  - http://127.0.0.1:5000/ にアクセス
  - urlに/recommend/ を追加してアクセス
  - 質問が表示される。

## お役立ち情報
- FraskとかpythonとかNumpyの参考になるURLを載せる
- Fraskチュートリアル(https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/tutorial/index.html)
- 元ネタ（https://qiita.com/Hanull/items/e7a3e4e675dfb3b44a7d）
- 随時更新する。

## Memo
- 

## Auther

## Licence

