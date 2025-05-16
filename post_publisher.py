from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

def post_to_wordpress(title, content, site_url, username, app_password):
    """
    Publish a post to WordPress using XML-RPC (works for free blogs).

    Args:
        title (str): Title of the blog post.
        content (str): Content of the blog post (HTML or text).
        site_url (str): WordPress XML-RPC endpoint, usually 'https://<your-site>.wordpress.com/xmlrpc.php'
        username (str): WordPress username.
        app_password (str): Your WordPress password (not app password in this case).
    
    Returns:
        bool: True if posted successfully, False otherwise.
    """

    # Make sure your site_url ends with /xmlrpc.php
    if not site_url.endswith('/xmlrpc.php'):
        site_url = site_url.rstrip('/') + '/xmlrpc.php'

    try:
        client = Client(site_url, username, app_password)

        post = WordPressPost()
        post.title = title
        post.content = content
        post.post_status = 'publish'

        post_id = client.call(NewPost(post))
        print(f"✅ Blog post published successfully! Post ID: {post_id}")
        return True

    except Exception as e:
        print(f"❌ Failed to publish blog post via XML-RPC: {e}")
        return False

# Dummy placeholder for Medium
def post_to_medium(*args, **kwargs):
    pass
