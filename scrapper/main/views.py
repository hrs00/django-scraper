from django.shortcuts import render
from bs4 import BeautifulSoup
import lxml, requests, pprint
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

cluster = MongoClient("mongodb+srv://<username>:<password>@cluster0.tvr9abb.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = cluster["scraper"]
collection = db["data"]

pune = ["https://housing.com/in/buy/searches/P2kiztglzttku35yi", "https://housing.com/in/buy/searches/P3zgy19bgb2xjywqp", "https://housing.com/in/buy/searches/P59h88syphonfafev", "https://housing.com/in/buy/searches/P1pu1fhmtcb6ffmti", "https://housing.com/in/buy/searches/P6w6rzu8yq0jutxih", "https://housing.com/in/buy/searches/P204l309sc6sumyo6", "https://housing.com/in/buy/searches/Pe60k9roxrhl11mb", "https://housing.com/in/buy/searches/P2p755bijb3w8veen", "https://housing.com/in/buy/searches/P3lkfsl66z59ky8xy", "https://housing.com/in/buy/searches/P3w6np3kxz7z6u4ym"]
delhi = ["https://housing.com/in/buy/searches/Pfkgym5kvlhge7gn", "https://housing.com/in/buy/searches/P43q6pfvqpemm4jmq", "https://housing.com/in/buy/searches/P56osr047do8k06lg", "https://housing.com/in/buy/searches/P3562l9da4dcq8jbi", "https://housing.com/in/buy/searches/P6sifbosdk9jhavh7", "https://housing.com/in/buy/searches/P4nbg63shm05zq9ni", "https://housing.com/in/buy/searches/P25o05lg17kds5p86", "https://housing.com/in/buy/searches/P6kuhkoxffi3m8szn", "https://housing.com/in/buy/searches/P6ub57k0m1bhyiswm", "https://housing.com/in/buy/searches/P4x6rum8xqktap38j"]
mumbai = ["https://housing.com/in/buy/searches/P6p1rr117q8jatvjh", "https://housing.com/in/buy/searches/P6rjzh7de86crx689", "https://housing.com/in/buy/searches/Pxifqgo94rn0pdam", "https://housing.com/in/buy/searches/P2rhwpqn80uznmgms", "https://housing.com/in/buy/searches/P672edzqhbl4ygkfv", "https://housing.com/in/buy/searches/P1fpe7ny75kk46ut4", "https://housing.com/in/buy/searches/Pkjmwdthlaf7av51", "https://housing.com/in/buy/searches/P3hflj8r4h8a0d7uq", "https://housing.com/in/buy/searches/P15otmhrp0jvi31vd", "https://housing.com/in/buy/searches/P64sr3l1z3so83hcj"]
lucknow = ["https://housing.com/in/buy/searches/P1xq07tfs7349ngcd", "https://housing.com/in/buy/searches/P6of8zd8uhhaelnb2", "https://housing.com/in/buy/searches/P4pjj6fjge5tmew4i", "https://housing.com/in/buy/searches/P370becnqokuwbspu", "https://housing.com/in/buy/searches/P2b0hy1jek1lliodk", "https://housing.com/in/buy/searches/P274hganfemwf1ida", "https://housing.com/in/buy/searches/P1guu9fgkou40ixcb", "https://housing.com/in/buy/searches/P3p3xouwvkn9jjzvw", "https://housing.com/in/buy/searches/P41g5k4inhlf9hxhd", "https://housing.com/in/buy/searches/P44efxvxvf90npfcg"]
agra = ["https://housing.com/in/buy/searches/P52pi3jk7j63yoyfm"]
ahmedabad = ["https://housing.com/in/buy/searches/P5pejqal1v82c496w", "https://housing.com/in/buy/searches/P38688p4dhunsg8z2", "https://housing.com/in/buy/searches/P36l91cajqown0qwr", "https://housing.com/in/buy/searches/P4gnkn9shalnddxap", "https://housing.com/in/buy/searches/P1z3e7rss3g64swwu", "https://housing.com/in/buy/searches/Pjdhgm9bwb0qxg1g", "https://housing.com/in/buy/searches/P3u17v6qfdv03cw8", "https://housing.com/in/buy/searches/P2segrs0ve5lq248g", "https://housing.com/in/buy/searches/P4f7q9r09j301onq8", "https://housing.com/in/buy/searches/P1ufj11f3nqjg6cff"]
kolkata = ["https://housing.com/in/buy/searches/P1fge1l3jdv6wjkip", "https://housing.com/in/buy/searches/P4u7sdmafjoogal4c", "https://housing.com/in/buy/searches/P3a1gsx74lnf3hr4w", "https://housing.com/in/buy/searches/Pgusmtt455m2gdem", "https://housing.com/in/buy/searches/P4uil6cnws7es98z2", "https://housing.com/in/buy/searches/P51dba1accanbvc8c", "https://housing.com/in/buy/searches/P34jxe9qk00xqaeo2", "https://housing.com/in/buy/searches/P2kc5igz9d2sq4b88", "https://housing.com/in/buy/searches/P6cepc54m2cr8pbbu", "https://housing.com/in/buy/searches/P6mctzmp464arvt0z"]
jaipur = ["https://housing.com/in/buy/searches/P501t1qw5gkmn11kj", "https://housing.com/in/buy/searches/P3gf5crot4gtlp2hp", "https://housing.com/in/buy/searches/P5oonztoq1ib2k5gd", "https://housing.com/in/buy/searches/P4wpt2thwt6156xa7", "https://housing.com/in/buy/searches/P35g25stzkhodgj09", "https://housing.com/in/buy/searches/P5i8b2xd2opvpwybw", "https://housing.com/in/buy/searches/P4flnd6xh754o1y2f", "https://housing.com/in/buy/searches/P128qbrcjt0c7a76n", "https://housing.com/in/buy/searches/P2nhidyi8pv9bq7le", "https://housing.com/in/buy/searches/P2a4mx34p7awjomk2"]
chennai = ["https://housing.com/in/buy/searches/P6v3kmtpj0f2oyp0t", "https://housing.com/in/buy/searches/P1hv8kabu33j980rv", "https://housing.com/in/buy/searches/P3nlxhdfttdcshmss", "https://housing.com/in/buy/searches/Psilrniik54ib8zt", "https://housing.com/in/buy/searches/P2p6e16trctzp4ia4", "https://housing.com/in/buy/searches/P4euyutxte07vrjkg", "https://housing.com/in/buy/searches/P40sxuhgw6f0qbvy2", "https://housing.com/in/buy/searches/P1tokohp70esscd5a", "https://housing.com/in/buy/searches/P6ntaf083argdpfzd", "https://housing.com/in/buy/searches/P6ne1si6hotnhbq8"]
bengaluru = ["https://housing.com/in/buy/searches/P16rl894c0qkogx5", "https://housing.com/in/buy/searches/P3yqqmgmdvlqoqz0n", "https://housing.com/in/buy/searches/P4ie9y33s0tezykdb", "https://housing.com/in/buy/searches/P5ldjyvluv8dq34ho", "https://housing.com/in/buy/searches/P31sk7r4jagf5ym0c", "https://housing.com/in/buy/searches/P613h1wbcuq4zmutv", "https://housing.com/in/buy/searches/P52txmvb7k9ufmw19", "https://housing.com/in/buy/searches/P6f5e34apgiybamqa", "https://housing.com/in/buy/searches/P2zuwx3wd8ufi35hx", "https://housing.com/in/buy/searches/P5kgp2umse63qjm62"]

all = pune + delhi + mumbai + lucknow + agra + ahmedabad + jaipur + chennai + bengaluru


flag = False
total = 0

def index(request):
    return render(request, "index.html")

def trigger(request):
    global total
    for each in all:
        html = requests.get(each)
        processed = BeautifulSoup(html.text, "lxml")
        prices = processed.find_all("div", class_="css-18rodr0")
        names = processed.find_all("h2", class_="_gi182v _1u71grho _7s5wglyw")
        types = processed.find_all("h3", class_="css-197fqpq")
        streets = processed.find_all("a", class_="link last-link _18uq1994 _ot7i1994")
        links = processed.find_all("a", class_="_j31fk8 _c8uea4 _g3exct _csbfng _frwh2y _ks15vq _vv1q9c _sq1l2s")

        for (price, name, type, street, link) in zip(prices, names, types, streets, links):
            collection.insert_one({"price": price.text,
            "name": name.text,
            "type": type.text,
            "locality": ",".join(street.text.split(",")[:-1]),
            "city": street.text.split(",")[-1],
            "property links": "https://housing.com/"+link.get("href")
            })
            
            total += 1

    return render(request, "triggered.html", {"total": total})

def enable(request):
    global flag
    flag = True
    return render(request, "enable.html")

def disable(request):
    global flag
    flag = False
    return render(request, "disable.html")

def my_cron_job():
    if flag:
        for each in all:
            html = requests.get(each)
            processed = BeautifulSoup(html.text, "lxml")
            prices = processed.find_all("div", class_="css-18rodr0")
            names = processed.find_all("h2", class_="_gi182v _1u71grho _7s5wglyw")
            types = processed.find_all("h3", class_="css-197fqpq")
            streets = processed.find_all("a", class_="link last-link _18uq1994 _ot7i1994")
            links = processed.find_all("a", class_="_j31fk8 _c8uea4 _g3exct _csbfng _frwh2y _ks15vq _vv1q9c _sq1l2s")

            for (price, name, type, street, link) in zip(prices, names, types, streets, links):
                collection.insert_one({"price": price.text,
                "name": name.text,
                "type": type.text,
                "locality": ",".join(street.text.split(",")[:-1]),
                "city": street.text.split(",")[-1],
                "property links": "https://housing.com/"+link.get("href")
                })
                global total
                total += 1
