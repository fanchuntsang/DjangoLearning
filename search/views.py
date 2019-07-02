from django.http import HttpResponse
from django.shortcuts import render
from django.utils.http import urlquote
from urllib import request
from bs4 import BeautifulSoup

# Create your views here.
def search(localRequest):
    result ={}
    context={"result":result}
    keyWord = localRequest.GET['keyWord']
    url = "https://www.biqukan.com/s.php?ie=gbk&s=2758772450457967865&q="
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    if  localRequest.GET['keyWord']!=None:
        keyWord = urlquote(localRequest.GET['keyWord'])
        url +=keyWord;
        target_req = request.Request(url = url, headers = head)
        target_response = request.urlopen(target_req)
        target_html = target_response.read().decode('gbk','ignore')
        #创建BeautifulSoup对象
        listmain_soup = BeautifulSoup(target_html,'lxml')
        novels = listmain_soup.find_all('h4',class_ = 'bookname')
        for novel in novels:
            for novelDetail in novel.find_all('a'):
                print(novelDetail.string)
                print("https://www.biqukan.com/"+novelDetail.get("href"))
                result[novelDetail.string] = "https://www.biqukan.com/"+novelDetail.get("href")
        print(result)
        return render(localRequest,"searchResult.html",context)
    else :
        return HttpResponse("请输入关键词")

def search_qidian(localRequest):
    result ={}
    context={"result":result}
    keyWord = localRequest.GET['keyWord']
    url = "https://www.23txt.com/search.php?keyword="
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    if  localRequest.GET['keyWord']!=None:
        keyWord = urlquote(localRequest.GET['keyWord'])
        url +=keyWord;
        target_req = request.Request(url = url, headers = head)
        target_response = request.urlopen(target_req)
        target_html = target_response.read().decode('utf-8','ignore')
        #创建BeautifulSoup对象
        listmain_soup = BeautifulSoup(target_html,'lxml')
        novels = listmain_soup.find_all('h3',class_ = 'result-item-title result-game-item-title')
        for novel in novels:
            for novelDetail in novel.find_all('a'):
                print(novelDetail.find('span').string)
                # print(novelDetail.get("href"))
                result[novelDetail.find('span').string] = novelDetail.get("href")
        print(result)
        return render(localRequest,"searchResult_qidian.html",context)
    else :
        return HttpResponse("请输入关键词")

