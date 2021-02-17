from bs4 import BeautifulSoup

with open("notion.html", "r", encoding="UTF-8") as nf:
    soup = BeautifulSoup(nf, "html.parser")
    s = soup.select("article")
    f = open("tistory.html", "w", encoding="UTF-8")
    f.write(str(s[0])[:16] + "Notion_P " + str(s[0])[16:])