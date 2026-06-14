# DjangoTrainsApp
Djangoの学習をするためのアプリです。是非テウ君にフィードバックを伝えてください。

# 手順
1. 新しいディレクトリを作って、githubからファイルをダウンロード：git clone https://github.com/tw999634/DjangoTrainsApp.git
2. 仮想環境構築：python -m venv .venv
3. 仮想環境実行：.venv\Scripts\activate
4. ライブラリをインストール：pip install -r requirements.txt (またはdjango, pymysqlがインストールされていることを確認)
5. mysqlにアカウント生成：IDはroot, PASSWORDはrootmysql (またはconfig/settings.pyファイルを直接修正)
6. mysqlでdjangotrainデータベース生成：CREATE DATABASE djangotrain;
7. データベーステーブル生成：python manage.py migrate
8. データ生成：python manage.py seed_practice_contents
9. サーバー実行：python manage.py runserver
10. ブラウザでWebページ接続：https://127.0.0.1:8000/practice または https://localhost:8000/practice
