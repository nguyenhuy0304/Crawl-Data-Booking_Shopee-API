import re
import json
import requests
import pandas as pd

def get_product_reviews(url):
    """ get all review for one url product"""
    r = re.search(r"i\.(\d+)\.(\d+)", url)
    shop_id, item_id = r[1], r[2]
    ratings_url = "https://shopee.vn/api/v2/item/" \
                  "get_ratings?filter=0&flag=1&itemid={item_id}" \
                  "&limit=20&offset={offset}&shopid={shop_id}&type=0"
    offset = 0

    product_review = {"username": [], "rating": [], "comment": []}
    while True:
        data = requests.get(ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset)).json()
        i = 1
        # count = 1
        for i, rating in enumerate(data["data"]["ratings"], 1):
            product_review["username"].append(rating["author_username"])
            product_review["rating"].append(rating["rating_star"])
            product_review["comment"].append(rating["comment"])
            # count += 1
            # print(count)
            # print(rating["author_username"])
            # print(rating["rating_star"])
            # print(rating["comment"])
            # print("-" * 100)

        if i % 20:
            break

        offset += 20

    return product_review

def export2excel(data, file_name):
    """ export data to excel file"""
    try:
        df = pd.DataFrame(data)
        df.to_excel(file_name + '.xlsx', index=False)

        return True
    except Exception as e:
        return e
def rating_star_trans(data):
    """     transformation rating star
        return struct {key = mark:value=count}
        """
    try:
        df = pd.DataFrame(data)
        stars = set(df['rating'])
        d = {}
        sum = 0
        count = 0
        for i in stars:
            d[i] = df['rating'].tolist().count(i)
            sum += i * df['rating'].tolist().count(i)
            count += df['rating'].tolist().count(i)

        return d, round(sum/count,1)
    except Exception as e:
        return e
# Using 2 function to save review:
# Product url
shopee_url = "https://shopee.vn/%C3%81o-thun-280GSM-Tinble-HOTTER-T-shirt-Form-OVERSIZE-Black-i.179608213.23882830025"

# Get review data:
reviews = get_product_reviews(shopee_url)

print(rating_star_trans(reviews))


# print(set(df['rating']))
# print(df['rating'].tolist().count(5))
# print(df['rating'].tolist().count(4))
# print(df['rating'].tolist().count(3))

# Save to excel file:
# file_name = 'data_tshirt'
# result = export2excel(reviews, file_name)

# print(result)