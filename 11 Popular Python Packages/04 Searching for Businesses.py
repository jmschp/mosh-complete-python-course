# 04 Searching for Businesses
# After completing lesson 3 and create the Yesp API in https://www.yelp.com/developers
 
import requests
import config

businesses_search_url  = "https://api.yelp.com/v3/businesses/search"
http_header = {
    "Authorization": "Bearer " + config.api_key_yelp
    }
paramters = {
    "term": "Sex Shop",
    "location": "Los Angels"
}
response = requests.get(businesses_search_url, headers=http_header, params=paramters)
# print(response.text) # Use the ".text" methos to convert the response to text. It can be used in case of error so see the description of the erros.

result = response.json() # To convert the response into a dictoanry use the "json()" method.
businesses = result["businesses"] # Acssesing the "businesses" key in the dictoanary.
# print(businesses)

filter_busi = [business["name"] for business in businesses if business["rating"] >= 4.5] # We are using a comprehension list to filter all the businnes with rating over 4.5 and storing their name in a new list.
print(filter_busi)
