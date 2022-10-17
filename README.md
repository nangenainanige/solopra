# 概要
そろばん初心者のために開発した、レベル別の問題作成webアプリケーションです。  
「見取り算」「かけ算」「わり算」をそれぞれのレベルに応じて問題作成ができます。  
また塾の先生向けにページを印刷することも念頭に置いて作成しています。  
# 各ファイルの機能
## djangoproj
### settings.py
アプリケーションの管理やメールサーバー設定などを行うファイルです。
### urls.py
webページのurlを記述したファイルです。
## sorobanapp
### mitori2.py
見取り算の問題作成実行ファイルです。
### kake.py  
かけ算の問題作成実行ファイルです。
### wari.py  
わり算の問題作成実行ファイルです。
### views.py
各計算実行ファイルとtemplates配下にあるHtmlファイルとの連携を行います。

### templates/soroban
#### base.html
「見取り算」「かけ算」「わり算」のページのひな型です。
#### mitori.html
見取り算のページです。
#### kake.html
かけ算のページです。
#### wari.html
わり算のページです。
#### top.html
トップページです。
#### contact.html
お問い合わせのページです。

### static
以下css、javascriptを記載しています。
#### css/wholecss/mobilewhole.css
スマホの画面サイズに合わせたcssファイルです。
#### css/wholecss/pcwhole.css
PCの画面サイズに合わせたcssファイルです。
