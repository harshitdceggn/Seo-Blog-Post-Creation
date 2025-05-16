import requests
from bs4 import BeautifulSoup

def get_trending_news():
    """
    Scrape trending news articles from Google News.
    Returns a list of trending news headlines and links.
    """
    url = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve news")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    trending_news = []

    for article in articles[:10]: 
        headline = article.find('h3')
        if headline:
            title = headline.text
            link = headline.find('a')['href']
            if link.startswith('.'):
                link = 'https://news.google.com' + link[1:]
            trending_news.append({'title': title, 'link': link})

    return trending_news

def get_best_selling_products():
    """
    Returns dummy best-selling product data for testing the pipeline.
    """
    print("Using dummy product data for testing...")
    return [
        {"name": "boAt Airdopes 141", "price": "₹1,199", "link": "https://amazon.in/sample-link1"},
        {"name": "Noise ColorFit Pro 4 Alpha", "price": "₹3,499", "link": "https://amazon.in/sample-link2"},
        {"name": "Samsung Galaxy M14", "price": "₹10,499", "link": "https://amazon.in/sample-link3"},
    ]
