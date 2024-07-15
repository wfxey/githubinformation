import requests
from packaging import version

def check(repo_url, current_version):
    api_url = f"https://api.github.com/repos/{repo_url}/tags"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        tags = response.json()
        if tags:
            latest_tag = tags[0]['name']
            if version.parse(latest_tag) > version.parse(current_version):
                print(f"New version available {latest_tag} / https://github.com/{repo_url}/releases/tag/{latest_tag}")
            else:
                print("No updates found!")
        else:
            print("No tags found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check("D-I-Projects/diec", "v0.3")
