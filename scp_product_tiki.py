import re
import json
import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://tiki.vn/macbook-air-m1-13-inch-2020-p124742926.html?spid=73795623',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'product_id': '124742926',
    'sort': 'score|desc,id|desc,stars|all',
    'page': '1',
    'limit': '10',
    'include': 'comments'
}

def get_product_reviews(url):
    """Get all review for one url product"""
    # r = re.search(r"p.(\d+)\.html\?spid=(\d+)", url)
    # print(r[1], type(r[1]))
    # print(r[2], type(r[2]))
    # product_id = r[1]

    rating_url = "https://tiki.vn/api/v2/reviews"

    product_review = {"username": [], "rating": [], "comment": []}
    data = requests.get(rating_url, headers=headers, params=params).json()
    # print(data.status_code)
    # print(data)
    for i, value in enumerate(data['data']):
        # print(i)
        # print(value["content"], type(value["content"]))
        # print(value["created_by"]["full_name"], type(value["created_by"]["full_name"]))
        # print(value["rating"], type(value["rating"]))

        product_review["username"].append(value["created_by"]["full_name"])
        product_review["rating"].append(value["rating"])
        product_review["comment"].append(value["content"])

    return product_review

def export2excel(data, file_name):
    """export data to excel file"""
    try:
        df = pd.DataFrame(data)

        # Set the index to start from 1
        df.index = df.index + 1

        df.to_excel(file_name + '.xlsx', index=False)

        return True
    except Exception as e:
        return e

"""---------Main Programing-----------"""
#Product URL:
tiki_product_url = "https://tiki.vn/macbook-air-m1-13-inch-2020-p124742926.html?spid=73795623"

reviews = get_product_reviews(tiki_product_url)
# print(reviews)
# df = pd.DataFrame(reviews)

# # Set the index to start from 1
# df.index = df.index + 1

# Display the DataFrame with the adjusted index
# print(df)

#Save to excel file:
file_name = "data_apple_macbook"
result = export2excel(reviews, file_name)