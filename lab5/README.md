# Aby wykonać laboratorium stworzyłem nową aplikację. Dodałem do niej 3 widoki:
- Widok **home** jako stronę główną a na niej wykonane przykłady z wykładu,
- Widok **scraping** a w nim formularz, w którym możemy podać stronę i szukany element do scrapowania
- Widok **xpath** a do tego widoku dodane zostały elementy z innych stron za pomocą xPath i lxmlx

## Przed rozpoczęciem dodawania elementów należało pobrać pakiet **Beautifulsoup4** za pomocą polecenia ``pip install beautifulsoup4`` oraz pakiet **lxml** za pomocą polecenia ``pip install lxml``.

## Tak przedstawia się widok home:
![](1)

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
## W przykładzie nr 3 zmodyfikowałem kod w taki sposób aby dzięki wyrażeniom regualrnym otrzymać wszystkie linki zaczynające się od "https" a następnie w szablonie dodałem je do tagu **a** do atrubutu **href**
## Tak przedstawia się div z przykładu nr 3 w szablonie home:


```python
<div class="twoRemPaddig">
    <h1>Przykład 3</h1>
    {% for links in all_links %}
        <a href = "{{links.href}}" >{{links.text}}</a>   
    {% endfor %}
</div>
```

