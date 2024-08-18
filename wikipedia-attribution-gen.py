import sys
import wikipedia
from urllib.parse import urlsplit
from pathlib import Path

def create_revision_url(url, revision_id):
    try:
        oldid = revision_id
        split_url = urlsplit(url)
        split_url_base = split_url.netloc
        split_url_title = Path(split_url.path).parts[-1]
        new_url = f"https://{split_url_base}/w/index.php?title={split_url_title}&oldid={oldid}"
    except:
        print("Whoops. Something went wrong.")
    return new_url

def generate_attribution(article_name):
    try:
        article = wikipedia.page(article_name)
        revision = create_revision_url(article.url, article.revision_id)
    except wikipedia.exceptions.PageError:
        print(f"Couldn't find {article_name} on Wikipedia.")
        return None

    title_string = f"Title of work: {article.title}"
    link_string = f"Link to work: {article.url}"
    revision_string = f"Revision: {revision}"
    license_string = "License of the work: CC-BY-SA-4.0"
    creator_string = "Creator names: Wikipedia Authors"

    # printing the strings to term for quick user validation
    print(title_string)
    print(link_string)
    print(revision_string)
    print(license_string)
    print(creator_string)

    # article_underscored = article.title.replace(" ", "_")

    output_file_name = f"attribution.txt"
    with open(output_file_name, 'w') as output_file:
        print(title_string, file=output_file)
        print(link_string, file=output_file)
        print(revision_string, file=output_file)
        print(license_string, file=output_file)
        print(creator_string, file=output_file)
    return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python3 wikipedia-attrib-gen.py <article_name>")
        sys.exit(1)

    for article_name in sys.argv[1:]:
        generate_attribution(article_name)
