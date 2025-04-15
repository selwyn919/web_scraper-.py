# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import logging
# import schedule
# import time
# from datetime import datetime

# # Logging setup
# logging.basicConfig(
#     filename='scraper.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# def scrape_jobs():
#     url = 'https://vacancymail.co.zw/jobs/'
#     headers = {'User-Agent': 'Mozilla/5.0'}

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#     except requests.RequestException as e:
#         logging.error(f"Request failed: {e}")
#         return []

#     soup = BeautifulSoup(response.content, 'html.parser')
#     jobs = soup.find_all('div', class_='job-box')[:10]  # First 10 jobs

#     data = []

#     for job in jobs:
#         try:
#             title = job.find('h2').get_text(strip=True)
#             company = job.find('div', class_='company-name').get_text(strip=True)
#             location = job.find('div', class_='location').get_text(strip=True)
#             expiry = job.find('div', class_='expiry-date').get_text(strip=True)
#             description_tag = job.find('p')
#             description = description_tag.get_text(strip=True) if description_tag else 'No description'

#             data.append({
#                 'Job Title': title,
#                 'Company': company,
#                 'Location': location,
#                 'Expiry Date': expiry,
#                 'Description': description
#             })
#         except Exception as e:
#             logging.warning(f"Error parsing a job: {e}")
#             continue

#     return data

# def save_to_csv(data):
#     try:
#         df = pd.DataFrame(data)
#         df.drop_duplicates(inplace=True)
#         df.to_csv('scraped_data.csv', index=False)
#         logging.info("Data saved to scraped_data.csv")
#     except Exception as e:
#         logging.error(f"Error saving CSV: {e}")

# def job():
#     logging.info("Scraping started")
#     jobs = scrape_jobs()
#     if jobs:
#         save_to_csv(jobs)
#     else:
#         logging.warning("No jobs scraped")

# # Schedule: daily at 09:00
# schedule.every().day.at("09:00").do(job)

# def run_scheduler():
#     logging.info("Scheduler running...")
#     while True:
#         schedule.run_pending()
#         time.sleep(60)

# if __name__ == '__main__':
#     print("Running scraper now...")
#     job()  # Run immediately
#     run_scheduler()  # Comment out if you only want it to run once

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import logging
# from datetime import datetime

# # Setup logging
# logging.basicConfig(
#     filename='scraper.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# # Target URL
# BASE_URL = "https://vacancymail.co.zw/jobs/"

# # Function to scrape job listings
# def scrape_jobs():
#     try:
#         logging.info("Starting job scrape...")

#         response = requests.get(BASE_URL)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')

#         job_cards = soup.select('.job-card')[:10]  # Get only the 10 most recent job cards
#         jobs = []

#         for card in job_cards:
#             title = card.select_one('.card-title')
#             company = card.select_one('.company')
#             location = card.select_one('.location')
#             expiry = card.select_one('.expiry')
#             link = card.find('a', href=True)

#             job_link = f"https://vacancymail.co.zw{link['href']}" if link else ""
#             job_description = fetch_job_description(job_link)

#             jobs.append({
#                 "Job Title": title.text.strip() if title else "N/A",
#                 "Company": company.text.strip() if company else "N/A",
#                 "Location": location.text.strip() if location else "N/A",
#                 "Expiry Date": expiry.text.strip() if expiry else "N/A",
#                 "Job Description": job_description
#             })

#         # Convert to DataFrame
#         df = pd.DataFrame(jobs)

#         # Save to CSV
#         df.to_csv("scraped_data.csv", index=False)
#         logging.info("Job data saved to scraped_data.csv")
#         print("Scraping complete! Check 'scraped_data.csv'.")

#     except Exception as e:
#         logging.error(f"Scraping failed: {e}")
#         print("An error occurred. Check the logs in scraper.log.")

# # Function to fetch job description from job details page
# def fetch_job_description(job_url):
#     try:
#         if not job_url:
#             return "No description available"

#         res = requests.get(job_url)
#         res.raise_for_status()
#         soup = BeautifulSoup(res.text, 'html.parser')

#         description_tag = soup.select_one('.job-description')
#         return description_tag.text.strip() if description_tag else "No description available"

#     except Exception as e:
#         logging.error(f"Failed to fetch job description: {e}")
#         return "Error fetching description"

# # Run the scraper
# if __name__ == "__main__":
#     scrape_jobs()

import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Setup logging
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# URL to scrape
BASE_URL = "https://vacancymail.co.zw/jobs/"

# Function to scrape the 10 most recent job listings
def scrape_jobs():
    try:
        logging.info("Starting job scraping...")

        # Get main jobs page
        response = requests.get(BASE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find job cards (update this selector if the site structure changes)
        job_cards = soup.select('.job-card')[:10]  # Only top 10
        jobs = []

        for card in job_cards:
            title = card.select_one('.card-title')
            company = card.select_one('.company')
            location = card.select_one('.location')
            expiry = card.select_one('.expiry')
            link = card.find('a', href=True)

            job_link = f"https://vacancymail.co.zw{link['href']}" if link else ""
            job_description = fetch_job_description(job_link)

            job_data = {
                "Job Title": title.text.strip() if title else "N/A",
                "Company": company.text.strip() if company else "N/A",
                "Location": location.text.strip() if location else "N/A",
                "Expiry Date": expiry.text.strip() if expiry else "N/A",
                "Job Description": job_description
            }

            jobs.append(job_data)

        # Convert to DataFrame
        df = pd.DataFrame(jobs)

        # Save as tab-delimited CSV
        df.to_csv("scraped_data.csv", sep='\t', index=False)
        logging.info("Scraping complete. Data saved to scraped_data.csv")
        print("✅ Scraping successful! File saved as 'scraped_data.csv'.")

    except Exception as e:
        logging.error(f"Scraping failed: {e}")
        print("❌ An error occurred during scraping. Check scraper.log for details.")

# Function to fetch job description from individual job page
def fetch_job_description(job_url):
    try:
        if not job_url:
            return "No description available"

        response = requests.get(job_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        desc_tag = soup.select_one('.job-description')
        return desc_tag.text.strip() if desc_tag else "No description found"
    except Exception as e:
        logging.error(f"Failed to fetch job description: {e}")
        return "Error fetching description"

# Main
if __name__ == "__main__":
    scrape_jobs()
import pandas as pd

# 10 most recent job posts (sample placeholder data)
jobs_data = [
    {
        "Job Title": "Software Developer",
        "Company": "TechZim",
        "Location": "Harare",
        "Expiry Date": "2025-04-20",
        "Job Description": "Develop and maintain software applications."
    },
    {
        "Job Title": "Marketing Officer",
        "Company": "ZimMarketing Inc.",
        "Location": "Bulawayo",
        "Expiry Date": "2025-04-22",
        "Job Description": "Plan and execute marketing campaigns."
    },
    {
        "Job Title": "Finance Intern",
        "Company": "FinTrust Bank",
        "Location": "Mutare",
        "Expiry Date": "2025-04-25",
        "Job Description": "Assist with financial data entry and reports."
    },
    {
        "Job Title": "Graphic Designer",
        "Company": "Creative Studios",
        "Location": "Harare",
        "Expiry Date": "2025-04-21",
        "Job Description": "Design promotional materials and branding."
    },
    {
        "Job Title": "Customer Service Agent",
        "Company": "TelOne",
        "Location": "Gweru",
        "Expiry Date": "2025-04-23",
        "Job Description": "Handle customer queries and complaints."
    },
    {
        "Job Title": "Project Manager",
        "Company": "BuildZim",
        "Location": "Chitungwiza",
        "Expiry Date": "2025-04-24",
        "Job Description": "Lead project teams and manage timelines."
    },
    {
        "Job Title": "Accountant",
        "Company": "AuditPro",
        "Location": "Masvingo",
        "Expiry Date": "2025-04-22",
        "Job Description": "Manage company accounts and audits."
    },
    {
        "Job Title": "HR Assistant",
        "Company": "PeopleFirst HR",
        "Location": "Harare",
        "Expiry Date": "2025-04-26",
        "Job Description": "Support recruitment and HR operations."
    },
    {
        "Job Title": "Data Analyst",
        "Company": "DataHub",
        "Location": "Bulawayo",
        "Expiry Date": "2025-04-25",
        "Job Description": "Analyze datasets and create reports."
    },
    {
        "Job Title": "Admin Assistant",
        "Company": "ZimAdmin",
        "Location": "Kadoma",
        "Expiry Date": "2025-04-27",
        "Job Description": "Provide administrative support and coordination."
    }
]

# Convert to DataFrame
df = pd.DataFrame(jobs_data)

# Save to CSV (tab-separated)
df.to_csv("scraped_data.csv", sep="\t", index=False)

print("✅ scraped_data.csv has been created successfully!")

import pandas as pd

# Improved job data (sample)
jobs_data = [
    {
        "Job Title": "Software Developer",
        "Company": "TechZim",
        "Location": "Harare",
        "Expiry Date": "2025-04-20",
        "Job Description": "Design, develop, and maintain software systems."
    },
    {
        "Job Title": "Marketing Officer",
        "Company": "ZimMarketing Inc.",
        "Location": "Bulawayo",
        "Expiry Date": "2025-04-22",
        "Job Description": "Develop marketing strategies and campaigns."
    },
    {
        "Job Title": "Finance Intern",
        "Company": "FinTrust Bank",
        "Location": "Mutare",
        "Expiry Date": "2025-04-25",
        "Job Description": "Assist the finance department in reporting tasks."
    },
    {
        "Job Title": "Graphic Designer",
        "Company": "Creative Studios",
        "Location": "Harare",
        "Expiry Date": "2025-04-21",
        "Job Description": "Create visual content for digital and print media."
    },
    {
        "Job Title": "Customer Service Agent",
        "Company": "TelOne",
        "Location": "Gweru",
        "Expiry Date": "2025-04-23",
        "Job Description": "Provide assistance to customers and resolve issues."
    },
    {
        "Job Title": "Project Manager",
        "Company": "BuildZim",
        "Location": "Chitungwiza",
        "Expiry Date": "2025-04-24",
        "Job Description": "Manage project execution, resources, and schedules."
    },
    {
        "Job Title": "Accountant",
        "Company": "AuditPro",
        "Location": "Masvingo",
        "Expiry Date": "2025-04-22",
        "Job Description": "Handle financial reporting and compliance audits."
    },
    {
        "Job Title": "HR Assistant",
        "Company": "PeopleFirst HR",
        "Location": "Harare",
        "Expiry Date": "2025-04-26",
        "Job Description": "Assist in recruitment and employee onboarding."
    },
    {
        "Job Title": "Data Analyst",
        "Company": "DataHub",
        "Location": "Bulawayo",
        "Expiry Date": "2025-04-25",
        "Job Description": "Interpret complex data and create dashboards."
    },
    {
        "Job Title": "Admin Assistant",
        "Company": "ZimAdmin",
        "Location": "Kadoma",
        "Expiry Date": "2025-04-27",
        "Job Description": "Maintain office operations and documentation."
    }
]

# Convert to DataFrame
df = pd.DataFrame(jobs_data)

# Create an Excel writer with styling
with pd.ExcelWriter("scraped_data.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="Jobs")

    # Get workbook and worksheet
    workbook = writer.book
    worksheet = writer.sheets["Jobs"]

    # Format headers
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'middle',
        'fg_color': '#4F81BD',
        'font_color': 'white',
        'border': 1
    })

    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        worksheet.set_column(col_num, col_num, 25)

    # Optional: add borders and wrap text for cells
    cell_format = workbook.add_format({
        'text_wrap': True,
        'valign': 'top',
        'border': 1
    })

    for row in range(1, len(df) + 1):
        for col in range(len(df.columns)):
            worksheet.write(row, col, df.iloc[row - 1, col], cell_format)

print("✅ 'scraped_data.xlsx' created with formatting.")
import pandas as pd

# Sample job data (replace with real scraped data if needed)
jobs_data = [
    {
        "Job Title": "Software Developer",
        "Company": "TechZim",
        "Location": "Harare",
        "Expiry Date": "2025-04-20",
        "Job Description": "Design, develop, and maintain software systems."
    },
    {
        "Job Title": "Marketing Officer",
        "Company": "ZimMarketing Inc.",
        "Location": "Bulawayo",
        "Expiry Date": "2025-04-22",
        "Job Description": "Develop marketing strategies and campaigns."
    },
    # ... Add more jobs as needed ...
]

# Convert to DataFrame
df = pd.DataFrame(jobs_data)

# Save to Excel with formatting
output_file = "scraped_data.xlsx"

# Write to Excel using xlsxwriter
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Jobs", index=False)

    workbook = writer.book
    worksheet = writer.sheets["Jobs"]

    # Style header
    header_format = workbook.add_format({
        "bold": True,
        "text_wrap": True,
        "valign": "center",
        "fg_color": "#4F81BD",
        "font_color": "white",
        "border": 1
    })

    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        worksheet.set_column(col_num, col_num, 25)  # Adjust width

    # Style cells
    cell_format = workbook.add_format({
        "text_wrap": True,
        "valign": "top",
        "border": 1
    })

    for row in range(1, len(df) + 1):
        for col in range(len(df.columns)):
            worksheet.write(row, col, df.iloc[row - 1, col], cell_format)

print(f"✅ '{output_file}' created successfully!")

import pandas as pd

# Read existing CSV file
df = pd.read_csv("scraped_data.csv")

# Optional cleanup: remove leading/trailing whitespace
df.columns = [col.strip().title() for col in df.columns]  # Capitalize column names
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Reorder columns (if needed)
desired_order = ["Job Title", "Company", "Location", "Expiry Date", "Job Description"]
df = df[[col for col in desired_order if col in df.columns]]

# Save the cleaned data back to the same CSV
df.to_csv("scraped_data.csv", index=False)

print("✅ 'scraped_data.csv' cleaned and updated successfully!")


