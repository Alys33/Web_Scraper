#
import requests
from bs4 import BeautifulSoup
import string
import os
# # Stage 1/5; Wanna Talk to the Internet


# user = input()
# url = requests.get(user)
# if url.status_code == 200:
#     try:
#         r = url.json()['content']
#         print(r)
#     except:
#         print('Invalid quote resource!')
#
# else:
#     print("Invalid quote resource!")

# Stage 2/5: The Beautiful Soup Ingredients

# user_url = input("enter the site: ")
# if 'imdb' not in user_url or 'title' not in user_url:
#     print('Invalid movie page!')
# else:
#     response = requests.get(user_url, headers={'Accept_Language':'en-US,en;q=0.5'})
#     soup = BeautifulSoup(response.content, 'html.parser')
#     title = soup.find('h1')
#     description = soup.find('span', {'data-testid': 'plot-l'})
#     if description is None:
#         print('Invalid movie page!')
#     else:
#         dict = {"title": title.text, "description":description.text}
#         print(dict)



# Stage 3 / 5 : What the File?

# user_url = input("enter the site: ")
# response = requests.get(user_url)
# if response.status_code != 200:
#     print(f"The URL returned {response.status_code}")
# else:
#     page_content = response.content
#     with open("source.html", "wb") as f:
#         f.write(page_content)
#         f.close()
#     print("Content saved")


# Stage 4/ 5: The Soup is Real
# new_list = []
# url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
#
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# # all articles type
# ls_art = soup.find_all("article")
# #
# # # all news type
#
# for art in ls_art:
#     x = art.find('span', {"data-test":'article.type'})
#     if "News" == x.contents[1].text:
#         new_list.append(art)
#
# # # getting the links to the article's contents
# links = []
# for art in new_list:
#     link = art.find("a", {'data-track-action':"view article"})
#     links.append(link['href'])
#
# # # scraping each article
# #
# list_articles =[]
# for el in links:
#     url = 'https://www.nature.com'+el
#     response = requests.get(url,headers={'Accept-Language': 'en-US,en;q=0.5'})
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     body = soup.find_all("div", {"class":"c-article-body main-content"})[0].text
#     body = body.encode("utf-8")
#
#     title = soup.find("title").text
#     title = title.strip()
#     for el in string.punctuation:
#         if el in title:
#             title = title.replace(el,"")
#     title = title.replace(" ","_")
#     with open(f'{title}.txt', 'wb') as f:
#         f.write(body)
#         f.close()
#     list_articles.append(f'{title}.txt')
# print(f"Saved article: {list_articles}")


# Stage 5/5: Soup, Sweet Soup


nb_page = int(input())
type_article = input()



for page in range(1,nb_page + 1):
    url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    os.mkdir(f"Page_{page}")
    os.chdir(f"Page_{page}")


# all type articles
    ls_art = soup.find_all("article")
    new_list = []
    for art in ls_art:
        x = art.find('span', {"data-test": 'article.type'})
        if type_article == x.contents[1].text:
            new_list.append(art)

    links = []
    for art in new_list:
        link = art.find("a", {'data-track-action': "view article"})
        links.append(link['href'])

    list_articles = []
    for el in links:
        url = 'https://www.nature.com' + el
        response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(response.content, 'html.parser')

        body = soup.find_all("div", {"class": "c-article-body main-content"})[0].text
        body = body.encode("utf-8")

        title = soup.find("title").text
        title = title.strip()
        for el in string.punctuation:
            if el in title:
                title = title.replace(el, "")
        title = title.replace(" ", "_")
        with open(f'{title}.txt', 'wb') as f:
            f.write(body)
            f.close()
        list_articles.append(f'{title}.txt')
    os.chdir(os.path.dirname(os.getcwd()))
print("Saved all articles.")










