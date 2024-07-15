# githubrepoinfo

A tool that lets you check your GitHub Project for updates.

## Installation

You can install `githubrepoinfo` using pip:

```bash
pip install githubrepoinfo
```
# .repo

### get_repo_info(owner, repo)

```python
import githubrepoinfo

repo_info = githubrepoinfo.repo.get_repo_info("wfxey", "binaryconvert")
```

### All subinfos

```python
import githubrepoinfo

repo_info = githubrepoinfo.repo.get_repo_info("wfxey", "binaryconvert")

if repo_info:
  print(f"Repository: {repo_info['full_name']}")
  print(f"Description: {get_description(repo_info)}")
  print(f"Stars: {get_stars(repo_info)}")
  print(f"Forks: {get_forks(repo_info)}")
  print(f"Open Issues: {get_open_issues(repo_info)}")
    
repo_link(f"{owner}/{repo}")
```

### Output 

```bash
Repository: wfxey/binaryconvert
Description: A super easy python tool that converts your text in binary language 8x Bit
Stars: 1
Forks: 0
Open Issues: 0
```
<hr>

# .user

### user_link(user)

```python
import githubrepoinfo 

githubrepoinfo.user.user_link("wfxey")
```
### Output
```bash
https://github.com/wfxey
```

<hr>

# .release

### release_link(name_and_repo, tag)

```python
import githubrepoinfo 

githubrepoinfo.release.release_link("D-I-Projects/diec", "v1.0")
```
### Output 
```bash
https://github.com/D-I-Projects/diec/releases/tag/v1.0
```

<hr>

