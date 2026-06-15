# DjangoTrainsApp
Djangoの基礎的な文法を学習をするためのアプリです。
対象：①Djangoを初めて学習する方
      ②Djangoの学習が上手く進まなく、練習をしてみたいと思っている方

-是非テウ君にラインまたはSlackでフィードバックを伝えてください！

# 手順
1. 新しいディレクトリを作って、githubからファイルをダウンロード：git clone https://github.com/tw999634/DjangoTrainsApp.git
2. 仮想環境構築：python -m venv .venv
3. 仮想環境実行：.venv\Scripts\activate
4. ディレクトリ移動：cd DjangoTrainsApp
5. ライブラリをインストール：pip install -r requirements.txt (またはdjango, pymysqlがインストールされていることを確認)
6. mysqlにアカウント生成：IDはroot, PASSWORDはrootmysql (またはconfig/settings.pyファイルを直接修正)
7. mysqlでdjangotrainデータベース生成：CREATE DATABASE djangotrain;
8. データベーステーブル生成：python manage.py migrate
9. データ生成：python manage.py seed_practice_contents
10. サーバー実行：python manage.py runserver
11. ブラウザでWebページ接続：https://127.0.0.1:8000/practice または https://localhost:8000/practice
