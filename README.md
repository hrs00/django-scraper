# django-scraper

## About

Django based app to run scraping cron job twice a day to scrape data about flats in pune, delhi, bengaluru, hyderabad, kolkata, jaipur, lucknow, agra, chennai and mumbai from housing.com.

## Requisites

Python packages required to run this application are listed in requirements.txt. To install the packages
```bash
pip install -r requirements.txt
```


## Installation

### 1. Add cron jobs
```bash
py manage.py crontab add
```

### 2. Run server
```bash
py manage.py runserver
```
