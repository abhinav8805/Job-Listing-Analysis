## 🐍 Python Job Scraper (TimesJobs)

This project scrapes job listings for **Python-related roles** from [TimesJobs](https://www.timesjobs.com/) and visualizes job availability across major Indian cities. It also detects your **current city using IP info** and checks for job openings nearby.

---

## 🚀 Features

* Scrapes live Python job postings from TimesJobs using **BeautifulSoup** and **Requests**.
* Automatically detects your **current city** via [ipinfo.io](https://ipinfo.io).
* Categorizes jobs into:

  * Pune
  * Bangalore (Bengaluru)
  * Mumbai
  * NCR region (Delhi, Noida, Gurgaon, Gurugram)
  * Your City (based on IP detection)
  * Others
* Prints company names and job locations in the terminal.
* Creates a **bar chart** visualization of job counts across cities with **Matplotlib**.

---

## 📂 Project Structure

```
.
├── job_scraper.py   # Main script
├── README.md        # Project documentation
```

---

## 🛠️ Requirements

Install dependencies before running:

```bash
pip install requests beautifulsoup4 lxml matplotlib
```

---

## ▶️ Usage

Run the script:

```bash
python job_scraper.py
```

You’ll see:

* Company names and job locations printed in the terminal.
* A summary of job counts in each city.
* A **bar chart** showing the distribution of Python jobs across cities.

---

## 📊 Example Output

**Terminal log:**

```
Tata Consultancy Services
Job is in Pune

Infosys
Job is in Bangalore

Total jobs in Pune are 12 for python enggs and in Bangalore 25,
while Mumbai has 8 jobs, and NCR region has 15 jobs.
Congrats, you have 3 jobs in your own city, Hyderabad
```

**Bar chart:**

Each bar shows the number of jobs in different cities, with values displayed above the bars.

---

PS - I have also shared a clip showing its working.

## ⚠️ Disclaimer

This project is for **educational purposes only**. Frequent scraping may violate TimesJobs’ Terms of Service. Use responsibly.


