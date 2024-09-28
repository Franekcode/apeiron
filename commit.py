from langflow import LangFlow
import requests

# Function to fetch HTML content from a given URL
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch URL: {url}")

# Function to extract product information using LangFlow
def extract_product_info(html_content):
    # Set up a LangFlow model that can analyze HTML
    flow = LangFlow(
        # Define your LangFlow steps here
        steps=[
            {
                "type": "html-parser",
                "input": html_content,
                "selector": "div",  # Use a broad selector initially
                "output": "parsed_content"
            },
            {
                "type": "llm-analyzer",  # Use LLM to analyze the content
                "input": "parsed_content",
                "output": "product_info",
                "model": "gpt-3.5-turbo",  # Use a suitable LLM
                "prompt": "Extract product names and prices from the given HTML content."
            }
        ]
    )

    # Run the flow
    result = flow.run()
    return result['product_info']

# URL of the page to scrape
url = 'https://www.decathlon.pl/mezczyzna/koszulki-meskie'

# Main execution
try:
    html_content = fetch_html(url)
    product_info = extract_product_info(html_content)
    print(product_info)  # Output the extracted product information
except Exception as e:
    print(e)
 