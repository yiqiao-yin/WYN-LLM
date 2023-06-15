import json

def call_yin_test1(query: str, user_key: str = "123") -> json:
    api_url = f"https://y3q3szoxua.execute-api.us-east-1.amazonaws.com/dev/my-openai-api-test1?query={query}&key={user_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle any potential errors
        return None