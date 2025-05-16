import requests

def get_seo_keywords(product_name):
    keywords = [
        f"buy {product_name}",
        f"{product_name} review",
        f"best price {product_name}",
        f"{product_name} features"
    ]
    return keywords

if __name__ == "__main__":
    sample_product = "wireless headphones"
    keywords = get_seo_keywords(sample_product)
    print(f"SEO keywords for '{sample_product}': {keywords}")
