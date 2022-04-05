#Scrapy Demo

install dependencies
```
sudo apt-get install python3 python3-dev
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
pip install --user pipenv
pipenv install --ignore-pipfile
```

Run spider
```
pipenv run scrapy crawl coles -a urls=<url1>,<url2>
```
Example
```
pipenv run scrapy crawl coles -a urls=https://www.coles.com.au/ 
```
