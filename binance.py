from bs4 import BeautifulSoup
import requests
import os
import json
# from apify_client import ApifyClient


base_url = "https://academy.binance.com"
response = requests.get('https://academy.binance.com/en/articles?page=1')
soup = BeautifulSoup(response.content, 'html.parser')



base_url += soup.find_all("a", attrs={"class": "e1i1pr7a0"})[0].get("href")
print(base_url)

response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

tags = []
for tag in soup.select('.el6ax900') :
       tags.append(tag.get_text())

image = soup.select('.coverImage')[0].get('src')

title = soup.select('.egdm8r30')[0].get_text()

difficulty = soup.select('.epoxe0d0')[0].get_text()

readtime = soup.select('.css-1j75qc1')[0].get_text()

body = soup.select('.css-1y1kitk')[0].get_text()


data = {
                'tags': tags,
                'title': title,
                'image_url': image,
                'difficulty':difficulty,
                'readtime':readtime,
                'body' :body
        }  


headers = {'Accept': 'application/json', 'content-type': 'application/json'}

r = requests.post('https://hook.integromat.com/8jfy3d48koa8trg4mbjkdxbpotwouv53', data=json.dumps(data), headers=headers)

print (r)

# # Initialize the main ApifyClient instance
# client = ApifyClient(os.environ['APIFY_TOKEN'], api_url=os.environ['APIFY_API_BASE_URL'])

# # Get the resource subclient for working with the default dataset of the actor run
# default_dataset_client = client.dataset(os.environ['APIFY_DEFAULT_DATASET_ID'])

# # Finally, push all the results into the dataset
# default_dataset_client.push_items(data)

# print(f'Results have been saved to the dataset with ID {os.environ["APIFY_DEFAULT_DATASET_ID"]}')

