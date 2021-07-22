from django.shortcuts import render
from bs4 import BeautifulSoup
from flask import Flask, render_template
import urllib
import urllib.parse
import urllib.request as req
import csv
import random
import requests
import json
from django.shortcuts import render
import json
from collections import OrderedDict
import pprint


def index(request):
  

    list_url = []
    for i in range(1,4):

        if i == 1:
            rand = 500 + random.randrange(31, 49)
            rand = str(rand)
            url = 'https://recipe.rakuten.co.jp/category/41-' + rand + '/'
        if i == 2:
            rand = 550 + random.randrange(0, 18)
            rand = str(rand)
            url = 'https://recipe.rakuten.co.jp/category/42-' + rand + '/'
        if i == 3:
            rand = 500 + random.randrange(69, 82)
            rand = str(rand)
            url = "https://recipe.rakuten.co.jp/category/43-" + rand + "/"
            
        #HTMLの要素を持ってくる
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        #<a>タグだけをとってきたかったが、いらないやつがたくさんついてくるので、その上階層の<li>を取得
        #<li>タグはたくさんあるのでfind_allを使う。仕様でfind_allで見つけたものはリストに格納される
        li = soup.find_all('li',class_ = 'recipe_ranking__item')

        a_tag = []

        for li_tag in li:
            #<li>タグの中にある<a>は一つだけなのでfindでよい。.get('href')でhref要素を取得
            link = "https://recipe.rakuten.co.jp" + li_tag.find('a').get('href')
            a_tag.append(link)

        j = random.randrange(0,len(a_tag))

        list_url.append(a_tag[j])



    return render(request, 'menu/index.html', {
        'url1': list_url[0],
        'url2': list_url[1],
        'url3': list_url[2],
    })