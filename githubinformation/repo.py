import requests

def get_repo_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching repository information: {response.status_code}, {response.json().get('message')}")
        return None

def get_description(repo_info):
    return repo_info.get('description', 'No description available.')

def get_stars(repo_info):
    return repo_info.get('stargazers_count', 0)

def get_forks(repo_info):
    return repo_info.get('forks_count', 0)

def get_open_issues(repo_info):
    return repo_info.get('open_issues_count', 0)

def repo_link(name_and_repo):
    return f"https://github.com/{name_and_repo}/releases"

if __name__ == "__main__":
    owner = "wfxey"
    repo = "binaryconvert"
    repo_info = get_repo_info(owner, repo)

    if repo_info:
        print(f"Repository: {repo_info['full_name']}")
        print(f"Description: {get_description(repo_info)}")
        print(f"Stars: {get_stars(repo_info)}")
        print(f"Forks: {get_forks(repo_info)}")
        print(f"Open Issues: {get_open_issues(repo_info)}")
    
    repo_link(f"{owner}/{repo}")
    