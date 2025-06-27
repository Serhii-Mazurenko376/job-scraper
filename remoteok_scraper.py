import requests
from bs4 import BeautifulSoup
import csv

URL = "https://remoteok.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Send GET request
response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    print("✅ Successfully fetched the page!")
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.title)

    # Proceed to scrape
    job_posts = soup.find_all("tr", class_="job")
    print(f"Found {len(job_posts)} job posts")

    jobs_data = []  # List to collect job dictionaries

    for job in job_posts:
        try:
            title = job.find("h2", itemprop="title").get_text(strip=True)
            company = job.find("h3", itemprop="name").get_text(strip=True)
            location = job.find("div", class_="location")
            location_text = location.get_text(strip=True) if location else "Remote"
            link = "https://remoteok.com" + job.get("data-href")

            jobs_data.append({
                "Title": title,
                "Company": company,
                "Location": location_text,
                "Link": link
            })

            print("\nJob Title:", title)
            print("Company:", company)
            print("Location:", location_text)
            print("Link:", link)

        except Exception as e:
            print("Error parsing job:", e)

    # Save to CSV
    with open("jobs.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Title", "Company", "Location", "Link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(jobs_data)

    print("\n✅ Saved jobs to jobs.csv")

else:
    print(f"❌ Failed to fetch page: {response.status_code}")
