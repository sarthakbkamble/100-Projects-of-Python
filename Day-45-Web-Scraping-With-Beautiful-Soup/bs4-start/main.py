from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")


articles_span = soup.find_all(name="span",class_="titleline")
articles = [article.find("a") for article in articles_span]
article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]


# print(article_texts)
# print(article_links)
print(article_upvotes)

index_of_highest_upvote = article_upvotes.index(max(article_upvotes))
print(article_texts[index_of_highest_upvote],"\n",article_links[index_of_highest_upvote],"\n",article_upvotes[index_of_highest_upvote])


# article_span = soup.find_all(name="span", class_="titleline")
# article_tag = article_span.find(name="a")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")

# article_upvote = soup.find(name="span", class_="score")
# article_upvote_text = article_upvote.getText()






# print(soup.title)

# title_data = soup.select(".titleline a")
# for title in title_data:
#     print(title.getText())
#     print("\n")

# import lxml
# with open("Day-45-Web-Scraping-With-Beautiful-Soup/bs4-start/website.html", "r") as file:
#     file_data = file.read()

# soup = BeautifulSoup(file_data,"html.parser")
# print(soup.prettify())
