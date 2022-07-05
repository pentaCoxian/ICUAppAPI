# ICUSyllabusScrape

ICUのシラバスとコースオファリングスのスクレイピングを行ってmariaDBに突っ込む感じのサムシング

## 必要パッケージ
- selenium
- webdriver-manager
- beautifulsoup4
- lxml
- mariadb (will need mariadb conector c? [Install CS package](https://mariadb.com/docs/connect/programming-languages/c/install/))
- tqdm (進捗確認用、必要なければ`scrape.py`のl:84`for i in tqdm(range(len(regno))):`からtqdmを外す)
かな？エラー出たら適時インストールしてください…

## Maria DB

For mariaDB, this repo uses mariadb along with mroonga for Japanese full text search. Setup as follows.

Install mariadb and run `mysql_secure_installation` script.
Before installing mroonga engine, make shure that the os is a version supported by mroonga. Supported OS versions can be seen [here](). The setup in hte next section is for Ubuntu 20.04.

Mroonga should be bundled with maradb but I've never seen it so,
To install, first enableing universe and security repo in ubuntu 
```
sudo apt-get install -y -V software-properties-common lsb-release
sudo add-apt-repository -y universe
sudo add-apt-repository "deb http://security.ubuntu.com/ubuntu $(lsb_release --short --codename)-security main restricted"
```
Then, add PPA to repo
```
sudo add-apt-repository -y ppa:groonga/ppa
sudo apt-get update
```
Finally install mroonga for mariadb aswell as MeCab for Japanese Tokenize
```
sudo apt-get install -y -V mariadb-server-mroonga
sudo apt-get install -y -V groonga-tokenizer-mecab
```


