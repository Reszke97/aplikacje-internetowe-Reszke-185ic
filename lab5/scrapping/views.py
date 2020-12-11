from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from bs4 import BeautifulSoup
from lxml import html
import requests
import re


def home(request):
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, "html.parser")



    """
    websiteLink = request.POST.get('web_link', None)
    element = request.POST.get('element', None)
    source=requests.get(websiteLink)
    
    allElements = []
    
    soup = BeautifulSoup(source.content, "html.parser")
    """

    # Przykład 1
    # Create all_h1_tags as empty list
    all_h1_tags = []

    # Set all_h1_tags to all h1 tags of the soup
    for element in soup.select("h1"):
        all_h1_tags.append(element.text)

    # Create seventh_p_text and set it to 7th p element text of the page
    seventh_p_text = soup.select("p")[6].text


    # Przykład 2
    # Create top_items as empty list
    top_items = []

    # Extract and store in top_items according to instructions on the left
    products = soup.select("div.thumbnail")
    for elem in products:
        title = elem.select("h4 > a.title")[0].text
        review_label = elem.select("div.ratings")[0].text
        # strip() usuwa zbędne spacje
        info = {"title": title.strip(), "review": review_label.strip()}
        top_items.append(info)
    

    #Przykład 3
    # Create top_items as empty list
    all_links = []

    # Extract and store in top_items according to instructions on the left
    links = soup.find_all('a', {'href':re.compile('^https')})
    for ahref in links:
        text = ahref.text
        text = text.strip() if text is not None else ""

        
        href = ahref.get("href")
        href = href.strip() if href is not None else ""
        all_links.append({"href": href, "text": text})

    # Przykład 4
    all_products = []

    # Extract and store in top_items according to instructions on the left
    products = soup.select('div.thumbnail')
    for product in products:
        name = product.select('h4 > a')[0].text.strip()
        description = product.select('p.description')[0].text.strip()
        price = product.select('h4.price')[0].text.strip()
        reviews = product.select('div.ratings')[0].text.strip()
        image = product.select('img')[0].get('src')

        all_products.append({
            "name": name,
            "description": description,
            "price": price,
            "reviews": reviews,
            "image": image
        })  
    return render(request,'scrapping/home.html',{'top_items':top_items,'all_h1_tags':all_h1_tags, 
        'seventh_p_text':seventh_p_text,'all_links':all_links,'all_products':all_products})



def scraping (request):
    if request.method == "POST":
        
        websiteLink = request.POST.get('web_link', None)
        element = request.POST.get('element', None)
        url = websiteLink
        source=requests.get(url).text

        allElements = []
        
        soup = BeautifulSoup(source, "html.parser")

        items = soup.find_all(element)
        amount = len(items)    

        for i in items:
            # Szukanie klasy
            findClass = i.get('class')
            if findClass is None:
                findClass = "no matches" 
            
            # Szukanie id
            findId = i.get('id')
            findId = findId.strip() if findId is not None else "no matches"

            # Szukanie article
            findArticle = i.get('article')
            findArticle = findArticle.strip() if findArticle is not None else "no matches"

            # Szukanie tekstu
            getText = i.text
            getText = getText.strip() if getText is not None else "no matches"

            # Szukanie spanów
            findSpan = i.get('span')
            findSpan = findSpan.strip() if findSpan is not None else "no matches"

            # Szukanie linków
            findHref = i.get('href')
            findHref = findHref.strip() if findHref is not None else "no matches"

            allElements.append({"findId": findId, "findClass": findClass, "findArticle": findArticle, "getText": getText, 'findHref':findHref, 'findSpan': findSpan})
        return render(request, 'scrapping/scraping.html', {'allElements':allElements, 'amount': amount, 'websiteLink': websiteLink, 'element':element})
    return render(request, 'scrapping/scraping.html')


def xml(request):
    
    # Szuaknie elementu przy pomocy xml
    # Szukanie elementu poprzez xPath
    url = 'https://www.octoparse.com/blog/top-30-free-web-scraping-software'    
    path = '/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/ul'
    response = requests.get(url)
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxml1 = tree[0].text_content()
    
    # Szukanie elemntu przez nazwę klasy   
    url = 'http://zacniewski.gitlab.io/'  
    path = '//*[@class="well"]'
    response = requests.get(url)    
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxml2 = tree[0].text_content()

    return render(request, 'scrapping/xpath.html', {'lxml1': lxml1,'lxml2': lxml2 })
