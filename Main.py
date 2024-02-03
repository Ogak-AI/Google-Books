import requests

def search_books(query):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "projection": "lite",
        "key": "YOUR_API_KEY"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["totalItems"] > 0:
            volume = data["items"][0]
            print("Title: ", volume["volumeInfo"]["title"])
            print("Authors: ", ", ".join(volume["volumeInfo"].get("authors", [""])))
            print("Download Link: ", volume["volumeInfo"].get("accessInfo", {}).get("pdf", {}).get("downloadRoute", ""))
        else:
            print("No books found.")
    else:
        print("Error while searching books.")

if __name__ == "__main__":
    book_title = input("Enter the book title: ")
    search_books(book_title)
