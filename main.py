import requests
from bs4 import BeautifulSoup
from datetime import datetime


def main():
    req = requests.get("https://news.ycombinator.com/")
    soup = BeautifulSoup(req.content, "html.parser")
    titles = [title.text for title in soup.find_all("a", "titlelink")]
    scores = [score.text for score in soup.find_all("span", "score")]
    links = [link["href"] for link in soup.find_all("a", "titlelink")]
    # published_at = [time.text for time in soup.find_all('span', 'age')]

    hn_data = [
        {"title": title, "score": score, "link": link}
        for title, score, link in zip(titles, scores, links)
    ]
    # print(hn_data)

    with open(
        f"data/{datetime.now().strftime('%d-%m-%Y')}.txt", mode="w", encoding="utf-8"
    ) as f:
        for i in hn_data:
            f.write(f"{'-' * 20}\n")
            f.write(f"{i['title']}\n")
            f.write(f"{i['score']}\n")
            f.write(f"{i['link']}\n")
            f.write(f"{'-' * 20}\n")


if __name__ == "__main__":
    main()
