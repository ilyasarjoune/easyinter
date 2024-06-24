import requests
from bs4 import BeautifulSoup
import json

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    url = f'https://www.linkedin.com/jobs/search?keywords=Stage&location=Morocco&geoId=102787409&trk=public_jobs_jobs-search-bar_search-submit&position=2&pageNum={page}&currentJobId=3954128721'
    r = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_list = []
    divs = soup.find_all('div', class_='base-card')
    for item in divs:
        title_tag = item.find('a')
        title = title_tag.text.strip() if title_tag else 'No title available'
        href = title_tag['href'].strip() if title_tag else 'No link available'
        company_tag = item.find('h4', class_='base-search-card__subtitle')
        company = company_tag.text.strip() if company_tag else 'No company available'
        location_tag = item.find('span', class_='job-search-card__location')
        location = location_tag.text.strip() if location_tag else 'No location available'
        date_tag = item.find('time', class_='job-search-card__listdate')
        datef = date_tag.text.strip() if date_tag else 'No date available'

        job = {
            'title': title,
            'company': company,
            'location': location,
            'date': datef,
            'link': href
        }
        job_list.append(job)

    return job_list

# Extract data
c = extract(0)
job_data = transform(c)

# Print the job data to inspect it
# print(json.dumps(job_data, indent=2))

# Send data to Laravel API
api_url = 'http://127.0.0.1:8000/api/internships'
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(api_url, json=job_data, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    print('Data sent successfully to Laravel API!')
except requests.exceptions.RequestException as e:
    print(f'Error sending data to Laravel API: {e}')
