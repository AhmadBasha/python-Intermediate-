from bs4 import BeautifulSoup
import requests
#import lxml

with open("website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
# print(soup.prettify())
# it will show us the first one of <a> tag
print(soup.a)
print("-----------------------")
all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)
print("-----------------------")
# here for the text in anchor tags
for tag in all_anchor_tags:
    print(tag.getText())
print("-----------------------")
# here the link in the anchor tags
for tage in all_anchor_tags:
    print(tag.get("href"))
print("-----------------------")
# find h1 with (id) on the page.
heading = soup.find(name="h1", id="name")
print(heading)
print(heading.string)
print("-----------------------")
# find it with (class) element
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.get("class"))
print(section_heading.getText())
print(section_heading.string)
print("-----------------------")
# here select an element by the order of the tags
# here choose anchor tag that inside p tag
company_url = soup.select_one(selector="p a")
print(company_url)
# here to select an id you can put # hashtag before the id
print("-----------------------")
name = soup.select_one(selector="#name")
print(name.string)
print("-----------------------")
# by class select all element that have heading element as class
heading_class = soup.select(selector=".heading")
print(heading_class)

print("-----------------------")
print("**********************")
###### this section for live website

response = requests.get("https://news.ycombinator.com")
# this is to take all the html elements.
# print(response.text)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(selector="tr td .title .storylink")
print(articles)
print("-----------------------")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

articles_upvote = [score.getText() for score in soup.select(selector=".subtext .score")]

print(article_texts)
print(article_links)
print(articles_upvote)
# here to get the numbers of the upvote in the articles we need to split each one of them
upvotes = [int(score.split()[0]) for score in articles_upvote]
print(upvotes)

# here to save the top five articles
top_5 = []
for _ in range(0,5):
    # here to save the largest number for upvotes
    largest_number = max(upvotes)
    # here find the index of the largest number
    the_index =upvotes.index(largest_number)
    # insert them in the list
    top_5.append([article_texts[the_index],
                  article_links[the_index],
                  upvotes[the_index]])
    # delete the large voted article to get the next one
    article_texts.pop(the_index)
    article_links.pop(the_index)
    upvotes.pop(the_index)

print("-----------------------")
print(top_5[0])
print(top_5[1])
print(top_5[2])
print(top_5[3])
print(top_5[4])






