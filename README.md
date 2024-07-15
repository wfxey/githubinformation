# githubrepoinfo

A tool that lets you check your GitHub Project for updates.

## Installation

You can install `githubrepoinfo` using pip:

```bash
pip install githubrepoinfo
```
# .repo

<hr>

# .user

### user_link(user)

```python
import githubrepoinfo 

githubrepoinfo.user.user_link("wfxey")
```
## Output
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
## Output 
```bash
https://github.com/D-I-Projects/diec/releases/tag/v1.0
```

