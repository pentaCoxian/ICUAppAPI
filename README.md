# ICUSyllabusScrape

ICUのシラバスとコースオファリングスのスクレイピングを行ってmongodb atlasに挿入するスクリプトです。

## 必要パッケージ
- selenium
- webdriver-manager
- beautifulsoup4
- lxml
- pymongo
- dnspython
- certifi
- tqdm (進捗確認用、必要なければ`scrape.py`のl:84`for i in tqdm(range(len(regno))):`からtqdmを外す)
かな？エラー出たら適時インストールしてください…

## Useage

`mongoAccess.py`のCONNECTION_STRINGを作成したmongodb atlasの設定に従って作成してください。その後`login_config_example.py`を`login_config.py`に名称変更して内容をicu portalのログイン情報に変更したら実行できるはずです。