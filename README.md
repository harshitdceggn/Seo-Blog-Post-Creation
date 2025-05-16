# 📝 AI-based SEO Blog Post Creation Tool

## 🚀 Overview
This project is an end-to-end automation pipeline that:
1. Scrapes best-selling products from an e-commerce source
2. Performs SEO keyword research
3. Generates a blog post using AI-friendly templates
4. Publishes it directly to your WordPress.org blog using the Jetpack-supported XML-RPC or REST API

---

## 🔧 Features
- 🔍 Scrapes best-selling products (currently using dummy data for testing)
- 📈 Generates SEO-optimized keywords automatically
- 🧠 Creates a 150–200 word product blog post using placeholders (AI integration ready)
- 📤 Auto-posts the blog on WordPress (Jetpack-connected sites)
- 🗃️ Supports both Medium and WordPress integrations (Medium requires token-based setup)

---

## 📁 Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Runs the complete pipeline |
| `scraper.py` | Simulates product scraping (can be extended to real sources) |
| `keyword_research.py` | Generates SEO keyword phrases based on the product name |
| `script_generator.py` | Generates blog post content using keywords |
| `post_publisher.py` | Publishes blog post to WordPress or Medium |

---

## ⚙️ Setup Instructions

### 1. Install Dependencies
```bash
pip install requests beautifulsoup4 python-wordpress-xmlrpc
