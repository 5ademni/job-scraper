import requests
from bs4 import BeautifulSoup

def get_tunisia_job_offers():
    # URL of the job listings website
    url = "https://www.bayt.com/en/tunisia/jobs/"

    # Send an HTTP request to fetch the page content
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all job listings
    job_listings = soup.find_all("div", class_="card")

    # Extract relevant information (e.g., job title, company, type, etc.)
    for job in job_listings:
        title = job.find("h2").text.strip()
        company = job.find("span", class_="company-name").text.strip()
        job_type = job.find("span", class_="job-type").text.strip()
        location = job.find("span", class_="location").text.strip()

        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Job Type: {job_type}")
        print(f"Location: {location}")
        print("-" * 40)

if __name__ == "__main__":
    get_tunisia_job_offers()
