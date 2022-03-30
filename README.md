# 「ゼロからFlaskがよくわかる本」サンプルコード

「[ゼロからFlaskがよくわかる本](https://amzn.to/30jqAud)」のサンプルコードです。

## 目次
1. はじめに
2. ブログアプリケーションの完成イメージ
3. Flaskの歴史と設計思想
4. 主要なPython Webフレームワークとトレンド
5. FlaskとDjangoの比較
6. Pythonのインストール
7. pipのインストール
8. 1つのファイルでアプリケーションを動かしてみる
9. Pipenvのインストール
10. 起動ファイルを作成する
11. configファイルを作る
12. Flaskのフレームワークについて理解する
13. テンプレートを作る
14. Bootstrapを導入
15. ログインフォームを作る
16. ビューを作る
17. ベースとなるレイアウトテンプレートを作る
18. sessionを扱う
19. flashを追加
20. url_forを使う
21. データベースを扱う
22. モデルを作る
23. スクリプトを作る
24. CRUDについて知る
25. ブログ投稿機能を作る
26. ブログ一覧機能を作る
27. ブログ詳細機能を作る
28. ブログ編集機能を作る
29. ブログ削除機能を作る
30. staticファイルを追加
31. ログイン認証のデコレータを作る
32. Blueprintでアプリケーションを分割する
33. バージョン0.11対応： flaskコマンドラインを扱えるようにする
34. バージョン1.0対応： アプリケーションファクトリを扱えるようにする
35. テストを書く
36. テストカバレッジの計測とレポートの作成
37. 最終的なアプリケーション構成
38. 最後に

## Q&A

1. Flask-Scriptがインストールできない

現時点(2021/07/20)のFlask-Scriptの最新バージョンにて、Flask2.0との組み合わせでバグ報告が上がっております。

```
$ python manage.py init_db
Traceback (most recent call last):
  File "C:\Users\xxx\workspace\python-serverless\application\manage.py", line 1, in <module>
    from flask_script import Manager
  File "C:\Users\xxx\.virtualenvs\application-rWZzxA8f\lib\site-packages\flask_script\__init__.py", line 15, in <module>
    from flask._compat import text_type
ModuleNotFoundError: No module named 'flask._compat'
```

#### 対応方法

以下のコマンドで、下記のライブラリをバージョン指定でインストールしてください。

```
pipenv install "Flask==1.1.2"
pipenv install "Jinja2==3.0.3"
pipenv install "itsdangerous==2.0.1"
pipenv install "Werkzeug==0.15.6"
```

その後、Flask-Scriptのインストールが可能になります。

