import requests

class SimpleAPIClient:
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com/posts"

    def get_posts(self):
        res = requests.get(self.url)
        if res.status_code == 200:
            return res.json()
        print("Failed to get posts")
        return None

    def get_post(self, post_id):
        res = requests.get(f"{self.url}/{post_id}")
        if res.status_code == 200:
            return res.json()
        print(f"Failed to get post {post_id}")
        return None

    def create_post(self, title, body, user_id):
        data = {"title": title, "body": body, "userId": user_id}
        res = requests.post(self.url, json=data)
        if res.status_code == 201:
            return res.json()
        print("Failed to create post")
        return None

# Example usage:
if __name__ == "__main__":
    client = SimpleAPIClient()
    
    print("First 5 posts:")
    posts = client.get_posts()
    if posts:
        for p in posts[:5]:
            print(p['title'])
    
    print("\nPost with ID 3:")
    print(client.get_post(3))
    
    print("\nCreating a new post:")
    print(client.create_post("My New Post", "Hello I am doing Lab 21", 1))
