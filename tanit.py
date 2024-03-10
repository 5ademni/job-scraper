import requests
from bs4 import BeautifulSoup
import json


def scrape_jobs(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    '''DEBUG: with open('sample_response.html', 'w', encoding='utf-8') as f:
        f.write(response.text)'''
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []

    # Find the job postings on the page
    for job_post in soup.find_all('article'):
        job_title = job_post.find(
            'div', class_='media-heading listing-item__title').text.strip()
        company_name = job_post.find(
            'span', class_='listing-item__info--item listing-item__info--item-company').text.strip()
        location = job_post.find(
            'span', class_='listing-item__info--item listing-item__info--item-location').text.strip()
        voir_plus_link = job_post.find(
            'a', class_='link')['href']

        job = {
            'title': job_title,
            'company': company_name,
            'location': location,
            'link': voir_plus_link
        }

        jobs.append(job)

    return jobs


def scrape_all_pages(base_url, num_pages):
    all_jobs = []
    for i in range(1, num_pages + 1):
        url = f"{base_url}&page={i}"
        jobs = scrape_jobs(url)
        all_jobs.extend(jobs)
    return all_jobs


if __name__ == "__main__":
    base_url = "https://www.tanitjobs.com/jobs/"
    num_pages = 5  # replace with the number of pages you want to scrape
    jobs = scrape_all_pages(base_url, num_pages)

    with open('jobs.json', 'w') as f:
        json.dump(jobs, f)
