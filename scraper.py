import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape job postings
def scrape_jobs(url, keywords):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []

    for job in soup.find_all('div', class_='job'):
        title = job.find('h2').text
        description = job.find('p').text
        if any(keyword.lower() in description.lower() for keyword in keywords):
            jobs.append({'title': title, 'description': description})

    return jobs

# Main function
def main():
    url = 'https://example.com/jobs'
    keywords = ['python', 'developer']
    job_listings = scrape_jobs(url, keywords)

    # Save to CSV
    with open('job_listings.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'description'])
        writer.writeheader()
        writer.writerows(job_listings)

if __name__ == "__main__":
    main()
