✅ Project Overview

Scrapes the 10 most recent job posts.

Extracts key information:

Job Title

Company

Location

Expiry Date

Job Description

Saves data into scraped_data.csv.

Enhances CSV file for better readability (improved formatting).

🛠️ Prerequisites

Before running this project, make sure you have the following installed:

1. Install Python

Download and install Python from the official website:
👉 https://www.python.org/downloads/

2. Install Visual Studio Code (Optional but Recommended)

Download and install VS Code to easily write and run your code:
👉 https://code.visualstudio.com/

3. Install Required Libraries

Once Python is installed, open Command Prompt or VS Code Terminal and install these packages:

pip install requests beautifulsoup4 pandas

🧾 Project Files

web_scraper.py: The script that performs the scraping.

scraped_data.csv: The output file where scraped job data is saved.

README.md: This instruction guide.

🧑‍💻 Step-by-Step Guide

🔹 Step 1: Create the Project Folder

Create a folder on your desktop or any convenient location:

Selwyn 2nd Project

🔹 Step 2: Open the Folder in VS Code

Launch VS Code and open the project folder you just created.

🔹 Step 3: Create the Python Script

Create a new Python file inside the folder and name it:

web_scraper.py

Paste your scraping code in this file.

🔹 Step 4: Run the Script

Open the terminal in VS Code (View > Terminal), then run:

python web_scraper.py

This will create or update the scraped_data.csv file with the latest job listings.

🔹 Step 5: View the Output

Check your project folder. You will see a file:

scraped_data.csv

Open it using Excel or Google Sheets to view the jobs in table format.

🔹 Step 6: Improve CSV Formatting (Optional but Recommended)

You can use pandas to style the CSV content if converting it to Excel later. For now, make sure the content is clean and columns are clear.

📂 How It Works (Behind the Scenes)

The script sends a request to the VacancyMail jobs page.

Parses the HTML using BeautifulSoup.

Extracts data from job cards (title, company, location, etc.).

Writes this data into a structured CSV file.

📌 Important Tips

Make sure you are connected to the internet when running the scraper.

If the site structure changes, the code may need updates.

Always double-check that the file path and Python version are correct when running.

✨ Features to Add Later

Convert to Excel with styled headers.

Add date of scrape.

Schedule daily scraping.

Add error logging and retry logic.

👨‍🔧 Author Notes

This was created as a Python learning project focused on real-world applications of web scraping, file handling, and data presentation.

Feel free to fork, reuse, or extend it for your own job board scraper!

Thanks for checking out this project! 🚀

✅ Project Overview

Scrapes the 10 most recent job posts.

Extracts key information:

Job Title

Company

Location

Expiry Date

Job Description

Saves data into scraped_data.csv.

Enhances CSV file for better readability (improved formatting).

🛠️ Prerequisites

Before running this project, make sure you have the following installed:

1. Install Python

Download and install Python from the official website:
👉 https://www.python.org/downloads/

2. Install Visual Studio Code (Optional but Recommended)

Download and install VS Code to easily write and run your code:
👉 https://code.visualstudio.com/

3. Install Required Libraries

Once Python is installed, open Command Prompt or VS Code Terminal and install these packages:

pip install requests beautifulsoup4 pandas

🧾 Project Files

web_scraper.py: The script that performs the scraping.

scraped_data.csv: The output file where scraped job data is saved.

README.md: This instruction guide.

🧑‍💻 Step-by-Step Guide

🔹 Step 1: Create the Project Folder

Create a folder on your desktop or any convenient location:

Selwyn 2nd Project

🔹 Step 2: Open the Folder in VS Code

Launch VS Code and open the project folder you just created.

🔹 Step 3: Create the Python Script

Create a new Python file inside the folder and name it:

web_scraper.py

Paste your scraping code in this file.

🔹 Step 4: Run the Script

Open the terminal in VS Code (View > Terminal), then run:

python web_scraper.py

This will create or update the scraped_data.csv file with the latest job listings.

🔹 Step 5: View the Output

Check your project folder. You will see a file:

scraped_data.csv

Open it using Excel or Google Sheets to view the jobs in table format.

🔹 Step 6: Improve CSV Formatting (Optional but Recommended)

You can use pandas to style the CSV content if converting it to Excel later. For now, make sure the content is clean and columns are clear.

📂 How It Works (Behind the Scenes)

The script sends a request to the VacancyMail jobs page.

Parses the HTML using BeautifulSoup.

Extracts data from job cards (title, company, location, etc.).

Writes this data into a structured CSV file.

📌 Important Tips

Make sure you are connected to the internet when running the scraper.

If the site structure changes, the code may need updates.

Always double-check that the file path and Python version are correct when running.

✨ Features to Add Later

Convert to Excel with styled headers.

Add date of scrape.

Schedule daily scraping.

Add error logging and retry logic.

👨‍🔧 Author Notes

This was created as a Python learning project focused on real-world applications of web scraping, file handling, and data presentation.

Feel free to fork, reuse, or extend it for your own job board scraper!

Thanks for checking out this project! 🚀

