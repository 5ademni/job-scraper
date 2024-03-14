import requests
from bs4 import BeautifulSoup
import json


def scrape_jobs(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
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
        voir_plus_link = job_post.find('a', class_='link')['href']
        logo_element = job_post.find(
            'img', class_='media-object profile__img-company')
        company_logo = logo_element['src'] if logo_element else None

        job = {
            'title': job_title,
            'company': company_name,
            'location': location,
            'link': voir_plus_link,
            'company_logo': company_logo
        }

        jobs.append(job)

    return jobs


def scrape_jobs_across_pages(base_urls, num_pages):
    all_jobs = {}
    for base_url in base_urls:
        jobs = []
        for i in range(1, num_pages + 1):
            url = f"{base_url}&page={i}"
            jobs.extend(scrape_jobs(url))
        all_jobs[base_url] = jobs
    return all_jobs


if __name__ == "__main__":
    category_dict = {
        "ingenierie": "https://www.tanitjobs.com/categories/707/ingenierie-jobs/?searchId=1710344349.2239&action=search",
        "technologie_de_linformation": "https://www.tanitjobs.com/categories/381/technologie-de-l-information-jobs/?searchId=1710344353.1857&action=search",
        "telecommunications": "https://www.tanitjobs.com/categories/710/t%C3%A9l%C3%A9communications-jobs/?searchId=1710344354.4138&action=search",
        "design": "https://www.tanitjobs.com/categories/386/design-jobs/?searchId=1710344356.7963&action=search",
        "electronique": "https://www.tanitjobs.com/categories/969/electronique-jobs/?searchId=1710344364.8323&action=search",
        "informatique": "https://www.tanitjobs.com/categories/705/informatique-jobs/?searchId=1710344373.4958&action=search"
    }
    # replace 5 with the number of pages you want to scrape
    jobs = scrape_jobs_across_pages(
        [category_dict["informatique"]], num_pages=2)

    with open('harvest/jobs.json', 'w') as f:
        json.dump(jobs, f)
