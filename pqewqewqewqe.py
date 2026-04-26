import requests
from bs4 import BeautifulSoup


class SimpleParagraphParser:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        self.timeout = 10

    def get_paragraphs(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            p_tags = soup.find_all('p')

            paragraphs = []
            for p in p_tags:
                text = p.get_text(strip=True)
                if text:
                    paragraphs.append(text)

            return paragraphs

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к {url}: {e}")
            return []


if __name__ == "__main__":
    parser = SimpleParagraphParser()
    url = "https://spb.top-academy.ru"
    paragraphs = parser.get_paragraphs(url)

    if paragraphs:
        print("Первые 5 параграфов:")
        for i, p in enumerate(paragraphs[:5], 1):
            print(f"{i}. {p[:100]}..." if len(p) > 100 else f"{i}. {p}")
    else:
        print("Не удалось получить параграфы со страницы")
