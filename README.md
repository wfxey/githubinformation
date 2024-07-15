
<div align="center">
  
# githubinformation

[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/wfxey/githubrepoinfo#license)  [![PyPi](https://img.shields.io/badge/PyPi%20Link-FFFF00)](https://pypi.org/project/githubrepoinfo/)  <a href="https://github.com/wfxey/githubrepoinfo/blob/master/CONTRIBUTING.md"><img src="https://img.shields.io/github/contributors-anon/wfxey/githubrepoinfo" alt="Contributors badge" /></a>  

A tool that lets you check your GitHub Project for updates.

</div>

## Installation

You can install `githubinformation` using pip:

```bash
pip install githubinformation
```
# .repo

### get_repo_info(owner, repo)

```python
import githubinformation

repo_info = githubinformation.repo.get_repo_info("wfxey", "binaryconvert")
```

### All subinfos

```python
import githubinformation

repo_info = githubinformation.repo.get_repo_info("wfxey", "binaryconvert")

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
import githubinformation

githubinformation.user.user_link("wfxey")
```
### Output
```bash
https://github.com/wfxey
```

<hr>

# .release

### release_link(name_and_repo, tag)

```python
import githubinformation

githubinformation.release.release_link("D-I-Projects/diec", "v1.0")
```
### Output 
```bash
https://github.com/D-I-Projects/diec/releases/tag/v1.0
```

<hr>

