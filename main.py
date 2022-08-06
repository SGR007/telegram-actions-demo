import logging
import logging.handlers
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


def main():
    req = requests.get('https://news.ycombinator.com/')
    soup = BeautifulSoup(req.content, 'html.parser')
    titles = [title.text for title in soup.find_all('a', 'titlelink')]
    scores = [score.text for score in soup.find_all('span', 'score')]
    # published_at = [time.text for time in soup.find_all('span', 'age')]

    hn_data = dict(zip(titles, scores))
    print(tabulate(
        {
            "titles": titles,
            "scores": scores
        }, headers=["titles", "scores"], tablefmt="pretty"
    ))

    data = tabulate(
        {
            "titles": titles,
            "scores": scores
        }, headers=["titles", "scores"], tablefmt="pretty"
    )

    logger.info(f'\n{data}')


if __name__ == '__main__':
    main()
