import requests


def api_post_put(url, headers, data, user=""):
    "Test post requests"
    print("\n POST: \n", requests.post(url, data=data, headers=headers).json())


def api_delete(url, mov_name):
    "Test delete requests"
    print("\n DELETE: \n", requests.delete(f"{url}del_by_mov_name/{mov_name}/"))


def api_get(url, headers, data, user = ""):
    "Test get requests"
    response = requests.get(url, data, headers=headers)
    print ("\n GET: \n", response.json())
    print (len(response.json()))




url = "http://127.0.0.1:8001/"
headers = {"Authorization": 'Token 1f914a0bd2981832591ab963b2c4db0511c2878a'}
data = {
        "name": "Genr2",
        "imdb_score": 15,
        "popularity": 100,
        "director": "Akash Swain8",
        "genre": ["testa", "nesta", "vesaa", "hessa", "gessa"]
        }

# For api_delete
mov_name = ""

api_post_put(url,headers,data)
api_get(url,headers,{})
api_delete(url,mov_name)
