# ICUAppAPI

ICUのシラバスとコースオファリングスのスクレイピングを行ってmariaDBに突っ込む感じのサムシング。ついでに日本語全文検索のためにMroongaもインストールするよ。

## 必要パッケージ
- selenium
- webdriver-manager
- beautifulsoup4
- lxml
- mariadb (will need mariadb conector c? [Install CS package](https://mariadb.com/docs/connect/programming-languages/c/install/))
- tqdm (進捗確認用、必要なければ`scrape.py`のl:84`for i in tqdm(range(len(regno))):`からtqdmを外す)
- Flask
- falcon
かな？エラー出たら適時インストールしてください…
`pip3 install selenium webdriver-manager beautifulsoup4 lxml mariadb tqdm Flask falcon`

## Maria DB

For mariaDB, this repo uses mariadb along with mroonga for Japanese full text search. Setup as follows. **IF USING UBUNTU, CHECK THAT UBUNTU IS 20.04. MROONGA DOES NOT SUPPORT 22.04**

Install mariadb and run `mysql_secure_installation` script.
```
sudo apt install mariadb-server
sudo mysql_secure_installation
```

Then, setup users and default database.`sudo mariadb`
```
CREATE USER username@'%' IDENTIFIED BY 'passwordForUser';
CREATE DATABASE databaseName;
GRANT ALL ON databaseName.* TO username@'%';
FLUSH PRIVILEGES;
QUIT;
```

This will create a user that can access databaseName from anywhere, but mariadb will still refuse connections from outside local host. Therefore, go to mariadb config file. In my case it was `/etc/mysql/mariadb.conf.d/50-server.cnf`. Open it with sudo nano(or Vim if you want to look cool or something). Under `[mysqld]` find `bind-address=127.0.0.1`. comment it out. 

Next, this isn't nessesary for mariadb installation, as we're in the config file, we can add config for mroonga. Under `[mysqld]`, add this to the end.
```
    innodb_ft_min_token_size=1
    ft_min_word_len=1

    innodb_buffer_pool_size=1024M
    innodb_log_file_size=1G

    server-id=100
    max_connect_errors=10000
    max-connections=500

    character-set-server=utf8mb4
```

## Installing mroonga

Again, before installing mroonga engine, make shure that the os is a version supported by mroonga. Supported OS versions can be seen [here](https://mroonga.org/docs/install.html). The setup in hte next section is for Ubuntu 20.04.

Mroonga should be bundled with maradb but I've never seen it. So, to install, first enable universe and security repo in ubuntu.
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
That's all! congrats you now should have mroonga installed on mariadb.
```
sudo mariadb
MariaDB [(none)]> SHOW ENGINES;
+--------+---------+----------------------------------------+
| Engine | Support | Comment                                | 
+--------+---------+----------------------------------------+
| Mroonga| YES     | CJK-ready fulltext search, column store|
| InnoDB | DEFAULT | Supports transactions, row-level loc...|
+--------+---------+----------------------------------------+
9 rows in set (0.000 sec)
```

To enable access from local servers, 
```
sudo ufw allow to 192.168.0.0/16 port 3306 proto tcp     
```
where `192.168.0.0/16` selects private network range and `port 3306` is mariadb port with `proto tcp` being the protocol used. This should limit the firewall so that only local devices can access the server.

```
sudo systemctl restart mariadb
sudo systemctl restrt ufw
```
for the changes to take place



## MeCab config

mecabrc will be missing. this folder likely will be in `/etc/mecabrc` for some reason. Thus, copy the folder to what mecab wants `sudo cp /etc/mecabrc /usr/local/etc`.


noteable: https://engineering.linecorp.com/ja/blog/mecab-ipadic-neologd-new-words-and-expressions/
https://qiita.com/katsuyuki/items/65f79d44f5e9a0397d31
https://32imuf.com/sqlalchemy/note/  -> add full text index to TEXT is possible?

install dict using `sudo apt install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file`
for better dictionaries, install ipadic-neologd 
```
git clone https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
sudo bin/install-mecab-ipadic-neologd
```
to find dict location, `sudo find / | grep mecab-ipadic-neologd`
## SQLAlchemy

Setup example
```
engine = sa.create_engine("mariadb+mariadbconnector://python:pythonAccess56@172.31.54.136:3306/syllabusdb?charset=utf8mb4",echo=True)
Base = declarative_base()

class Course(Base):
    __tablename__ ="testtable"
    __table_args__ = {
        'mariadb_ENGINE': 'mroonga',
        'mariadb_DEFAULT_CHARSET': 'utf8mb4'
    }
    regno = sa.Column(sa.Integer, primary_key=True)
    title_j = sa.Column(sa.String(length=15900))
    title_e = sa.Column(sa.String(length=400))
```


# Code

To access the database in a VPC using python and mariadb, the connection setup should be something like this:
```
conn = mariadb.connect(
        user = "username",
        password = "passwordForUser",
        host = "local-ip-address",
        port = 3306,
        database = "databaseName"
    )
```
where the username and password is from the setup done in the mariadb setup section. The host woll point to localhost or another server. In this case we are using AWS EC2 so we will use the local ip, which shouldn't change even after reboot.


## File structure

mariadbTemp folder includes files for scraping data from icu and pushing it to a different ec2 instance.
Should be 
- Scrape.py : source of scraping
- helper.py : helper function to pharse the results from scrape.py currently used for course info
- sqlAlch.py : use MeCab to turn scraped content to tags and put them in remote mariadb