# from matplotlib.style import context
# from playwright.sync_api import sync_playwright

# def run(playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=50)
#     # chromium = playwright
#     # browser = chromium.launch()
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlJDZ0FQAQ?hl=en-ID&gl=ID&ceid=ID%3Aen')
#     page.screenshot(path='tes.png')
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)
    # html_articles = []
   
   
    # for i in range(3):
    #     articles = url.locator('ul[class="novel-list grid col col2"] a')
    #     html_articles.append(articles.inner_html())
    #     url.locator('ul[class="pagination"] a').nth(0)
    # with open('all_articles.html', 'w+') as f:
    #     full_html_articles = ''.join(html_articles)
    #     f.write(full_html_articles)
    #     browser.close()

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
import time

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.apple.com/br/shop/product/MV7N2BE/A/airpods-com-estojo-de-recarga")
    html = page.content()
    soup = BeautifulSoup(html,'html.parser')
    valorAppleStore = soup.select("span.as-price-installments")[-2].get_text().replace(" à vista (10% de desconto)", '')
    print(valorAppleStore)
    browser.close()