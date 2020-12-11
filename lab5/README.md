# Aby wykonać laboratorium stworzyłem nową aplikację. Dodałem do niej 3 widoki:
- Widok **home** jako stronę główną a na niej wykonane przykłady z wykładu,
- Widok **scraping** a w nim formularz, w którym możemy podać stronę i szukany element do scrapowania
- Widok **xpath** a do tego widoku dodane zostały elementy z innych stron za pomocą xPath i lxmlx

## Przed rozpoczęciem dodawania elementów należało pobrać pakiet **Beautifulsoup4** za pomocą polecenia ``pip install beautifulsoup4`` oraz pakiet **lxml** za pomocą polecenia ``pip install lxml``.

## Tak przedstawia się widok home:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab5/zrzuty/1.PNG)

### Do wyświetlenia przykładów z repozytorium wystarczyło przekazać do funkcji return funkcje **render** ze słownikiem, z szablonem do którego będziemy przekazywać dane oraz słownikiem z utowrzonymi danymi z web scrapingu.
Tak wygląda kod z przykładami z repozytorium:

```python
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, "html.parser")
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
    
    # Zmodyfikowałem przykład 3 za pomocą wyrażenia regularnego
    # Create top_items as empty list
    all_links = []

    # Extract and store in top_items according to instructions on the left
    # znajdź wszystkie tagi a którch atrubut href zaczyna się od "https"
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
```
## W przykładzie nr 3 zmodyfikowałem kod w taki sposób aby dzięki wyrażeniom regualarnym otrzymać wszystkie linki zaczynające się od "https" a następnie w szablonie dodałem je do tagu ```a``` do atrubutu ```href```
## Tak przedstawia się div z przykładu nr 3 w szablonie home:


```python
<div class="twoRemPaddig">
    <h1>Przykład 3</h1>
    {% for links in all_links %}
        <a href = "{{links.href}}" >{{links.text}}</a>   
    {% endfor %}
</div>
```

## Do stworzenia formularza wykorzystałem gotowy formularz z bootstrapa https://getbootstrap.com/docs/4.0/components/forms/ . Dostosowałem go do potrzeb laboratoriów. Tak prezentuje się widok "scraping" z formularzem przed wyszukaniem wskazanego elementu:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab5/zrzuty/2.PNG)

## Jako przykład do wyświetlenia szukanego elementu posłużyłem się stroną https://zacniewski.gitlab.io/ .

## Tak przedstawiają się dane które podałem w formularzu:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab5/zrzuty/3.PNG)

## Po wykonaniu przeszukiwania tak przedstawia się widok dla tagu ```p```:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab5/zrzuty/4.PNG)


## Tak przedstawia się funkcja w widokach służąca do pobierania danych:
```python
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
```

## Gdy wyślemy formularz do fuknckji trafia adres url oraz inorfmacja jakiego elementu funkcja ma szukać pod danym adresem url. Działa to w taki sposób, że po pobraniu wskazanego elementu poszukiwane są w nim tagi takie jak:

- span
- article

## Oraz atrybuty :
- id
- class
- href

## Dodatkowo za pomocą funckji .text zwracany jest tekst z danego tagu a w przypadku gdy jest to np. div to jako tekst wyświetlone zostanie również wyświetlone wszystko co jest wewnątrz diva (tzn. np **span** który posiada jakiś tekst i jest wewnątrz tego diva i wszystkie inne elementy posiadające tekst wchodzące w skład tego diva) a następnie za pomocą metody strip() pozbywamy się zbędnych spacji. Jeśli jednak któryś z tagów bądź atrybutów był pusty czyli po prostu wewnątrz elementu takowy nie występuje to zostanie do niego wpisany string "no matches" .

## Tak przedstawia się przykład dla elemntu "Div":
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab5/zrzuty/5.PNG)

## Jak można zauważyć na rysnku powyżej zostało znalezione aż 28 elementów **div** a wewnątrz nich wyświetlone inne zdefiniowane wcześniej w funkcji elementy.

## Kodu z szablonu "scraping"(Jeśli link istnieje to zostajey on dodany do tagu ``a`` wraz z jego atrybutem ``href``):

```python
{% extends 'scrapping/base.html' %}
{% block content %}
    <form method="POST" class="w40">
        {% csrf_token %}
        <div class="form-group">
            <label>Podaj url</label>
            <input type="text" name="web_link" class="form-control" required placeholder="Url">
        </div>
        <div class="form-group">
            <label for="exampleInputPassword1">Podaj szukany element</label>
            <input type="text" class="form-control" name="element" required placeholder="element">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    <ul style="font-family: 'Roboto', sans-serif;font-size:130%;font-weight:800;">
        <li>Przeszukana strona to : <a href = "{{websiteLink}}">{{websiteLink}}</a></li>
        <li>Poszukiwany element to : <span class="text-success">{{element}}</span></li>
        <li>Liczba znalezionych elemntów : {{amount}}</li>
    </ul>
    <hr></hr>

    {% for elements in allElements %}
        <ul style="padding:2rem">
            <li>klasa--------->{{elements.findClass}}</li>
            <li>id--------->{{elements.findId}}</li>
            <li>span--------->{{elements.findSpan}}</li>
            <li>text--------->{{elements.getText}}</li>
            {% if elements.findHref == 'no matches' %}
                <li>link--------->{{elements.findHref}}<li>
            {% else %}
                <li><a href="{{elements.findHref}}">link--------->{{elements.findHref}}</a></li>
            {% endif %}
        </ul>
    {% endfor %}
{% endblock %}
```

## Na koniec do zastosowania XPath i xmlx stworzyłem strone z widokiem o nazwie "xpath" w którym zastosowałem obie metody. Przykład z pobraniem elementu za pomocą klasy(przykład nr2) i przykład z pobraniem scieżki xpath(przykład nr 1) znajdują się na stronie xPath obok siebie zostaną pokazane po krótkim omówieniu jak je znaleźć.

## Przykład nr 2 to pobranie adresu ``url`` a następnie po zbadaniu elementu pobranie scieżki xPath

## Proces przedstawia się następująco. Najpierw ze strony https://www.octoparse.com/blog/top-30-free-web-scraping-software pobieram jej adres url. Następnie klikam zbadaj i skopiuj xPath:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab5/zrzuty/6.png)

## Następnie do kodu wrzucam scieżkę i kod prezentuje się następująco:
```python
def xml(request):
    # Szukanie elementu poprzez xPath
    url = 'https://www.octoparse.com/blog/top-30-free-web-scraping-software'    #<------------- Tutaj wrzucam adres url
    path = '/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/ul' #<----------------------------Tutaj wrzucam scieżke xPath
    response = requests.get(url)
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxmlPrzyklad2 = tree[0].text_content()
```

## Przykład nr 1 to również pobranie adresu ```url``` a następnie tym razem skopiwanie nazwy klasy.
## Proces przedstawia się następująco. Najpierw ze strony http://zacniewski.gitlab.io/ pobieram jej adres url. Następnie przechodzę do zbadania elementu i kopiuje nazwę klasy:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab5/zrzuty/7.png)

## Teraz pozostaje wrzucić ```url``` i nazwę klasy do naszego kodu:
```python
  # Szukanie elemntu przez nazwę klasy   
    url = 'http://zacniewski.gitlab.io/'  #<---------------- Tutaj wrzucam adres url
    path = '//*[@class="well"]' #<---------------- Tutaj wrzucam nazwę klasy
    response = requests.get(url)    
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxmlPrzyklad1 = tree[0].text_content()
```

## Finalnie funkcja w widokach wygląda następująco:
```python
def xml(request):
    
     # Szukanie elementu poprzez xPath
    url = 'https://www.octoparse.com/blog/top-30-free-web-scraping-software'    
    path = '/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/ul'
    response = requests.get(url)
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxmlPrzyklad2 = tree[0].text_content()
    
    # Szukanie elemntu przez nazwę klasy   
    url = 'http://zacniewski.gitlab.io/'  
    path = '//*[@class="well"]'
    response = requests.get(url)    
    source = html.fromstring(response.content)    
    tree = source.xpath(path)
    lxmlPrzyklad1 = tree[0].text_content()

    return render(request, 'scrapping/xpath.html', {'lxml1': lxmlPrzyklad1,'lxml2': lxmlPrzyklad2 })
```
## Tak wygląda strona z pobranymi elementami:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab5/zrzuty/8.PNG)

