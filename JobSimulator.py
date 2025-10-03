from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

from bs4 import BeautifulSoup
import requests

def yourCity():
    response = requests.get('http://ipinfo.io/json')
    data = response.json()
    return data.get('city', 'Unknown')

city = yourCity()

jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
puneJobCount = 0 
yourCityJobCount = 0
bloreJobCount = 0
mumJobCount = 0
ncrJobCount = 0
otherJobCount = 0

for job in jobs:

	company_name = job.find('h3', class_ ='joblist-comp-name').text.strip()
	job_location = job.find('li', class_ = 'srp-zindex location-tru').text.strip()

	if "Pune" in job_location:
		puneJobCount += 1
		print(f'''
			{company_name}
			Job is in {job_location}
			''')
		
	elif city in job_location:
		yourCityJobCount += 1
		print(f'''
			{company_name}
			Job is in {job_location}
			''')

	elif "Bangalore" in job_location or "Bengaluru" in job_location:
		print(f'''
			{company_name}
			Job is in {job_location}
			''')
		bloreJobCount += 1

	elif "Mumbai" in job_location:
		print(f'''
			{company_name}
			Job is in {job_location}
			''')
		mumJobCount += 1

	elif "Noida" in job_location or "Gurgaon" in job_location or "Delhi" in job_location or "Gurugram" in job_location:
		ncrJobCount += 1
		print(f'''
			{company_name}
			Job is in {job_location}
			''')
	else:
		otherJobCount += 1

print(f"Total jobs in Pune are {puneJobCount} for python enggs and in Bangalore {bloreJobCount}, ")
print(f"while Mumbai has {mumJobCount} jobs, and NCR region has {ncrJobCount} jobs. ")

if yourCityJobCount:
	print(f"Congrats, you have {yourCityJobCount} jobs in your own city, {city}")
else:
	print(f"Unfortunatly, we have no jobs around {city}")


#now plotting the jobs in these cities

cities = ['Pune', 'Bangalore', 'Mumbai', 'NCR', city, 'Others']
job_counts = [puneJobCount, bloreJobCount, mumJobCount, ncrJobCount, yourCityJobCount, otherJobCount]

plt.figure(figsize=(12, 8))
bars = plt.bar(cities, job_counts, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'])

for bar, count in zip(bars, job_counts):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
             str(count), ha='center', va='bottom', fontweight='bold')

plt.title('Python Jobs Distribution Across Cities in India', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Cities', fontsize=12)
plt.ylabel('Number of Jobs', fontsize=12)
plt.grid(axis='y', alpha=0.3)

plt.show()