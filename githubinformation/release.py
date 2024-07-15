def release_link(name_and_repo, tag):
    release = f"https://github.com/{name_and_repo}/releases/tag/{tag}"
    print(release)
    return release

if __name__ == "__main__":
    release_link("D-I-Projects/diec", "v1.0")
