import requests
from lxml import html

def amazon_scrapper_parse(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response)
            tree = html.fromstring(response.text)
            item_blocks = tree.xpath(
                "//text()[contains(., 'Results')]/following::div[@data-index]//text()[contains(., 'WF-1000XM4')]/ancestor-or-self::div[5]"
            )
            data = []

            for item in item_blocks:
                item_name = item.xpath(".//text()[contains(., 'Sony')]").get()
                item_price = item.xpath(
                    './/descendant::span[@class="a-offscreen"][1]//text()'
                ).get()
                item_link = item.xpath(
                    ".//text()[contains(., 'Sony')]/ancestor-or-self::a[1]/@href"
                ).get()

                # review_data = [item_name, {"Price": item_price}]
                review_data = []

                # Request 2: Inside one Product Page
                product_response = requests.get(
                    f"https://www.amazon.com{item_link}", headers=headers
                )
                if product_response.status_code == 200:
                    product_tree = html.fromstring(product_response.text)
                    reviews = product_tree.xpath('//*[@data-hook="review"]')
                    for review in reviews:
                        commented_names_text = review.xpath(
                            '(.//descendant::*[@class="a-profile-name"]//text())[1]'
                        ).get()
                        commented_rating = review.xpath(
                            '(.//descendant::*[contains(@class, "a-icon a-icon-star")]//text())[1]'
                        ).get()

                        review_data.append(
                            {
                                "commented name": commented_names_text,
                                "commented rating": commented_rating,
                            }
                        )

                    data.append(
                        {
                            "item_name": item_name,
                            "item_price": item_price,
                            "review_data": review_data,
                            "item_link": item_link,
                        }
                    )
                else:
                    print(
                        f"Failed to retrieve data from product page. Status code: {product_response.status_code}"
                    )
            # yield {'data': data}
            print(data)
            return data
            
        else:
            print("Failed to retrieve data. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None
    
# def main():
#     special_offers_data = amazon_scrapper_parse('https://www.amazon.com/s?k=sony+wf-1000xm4')

#     if special_offers_data:
#         print(special_offers_data)
#     else:
#         print("No data available.")

# if __name__ == "__main__":
#     main()

amazon_scrapper_parse('https://www.amazon.com/s?k=sony+wf-1000xm4')