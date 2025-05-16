from scraper import get_best_selling_products
from keyword_research import get_seo_keywords
from script_generator import generate_blog_post
from post_publisher import post_to_wordpress, post_to_medium

def seo_blog_post_creation_pipeline():
    print("Starting AI-based SEO Blog Post Creation Tool...\n")

    products = get_best_selling_products()
    if not products:
        print("No best-selling products found. Exiting.")
        return

    top_product = products[0]
    product_name = top_product['name']
    print(f"Processing product: {product_name}\n")

    keywords = get_seo_keywords(product_name)
    print(f"SEO keywords: {keywords}\n")

    blog_post = generate_blog_post(product_name, keywords)
    print(f"Blog post:\n{blog_post}\n")

    wordpress_url = 'oksje.wordpress.com'
    wordpress_user = 'harshitdceggn'
    wordpress_password = 'greenJAP@123'

    post_response = post_to_wordpress(
        product_name,
        blog_post,
        wordpress_url,
        wordpress_user,
        wordpress_password
    )

    if post_response:
        print("Blog post published successfully on WordPress.")
    else:
        print(" Failed to publish blog post.")

if __name__ == "__main__":
    seo_blog_post_creation_pipeline()
