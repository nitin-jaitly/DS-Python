import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import concurrent.futures

# Global variable to store all files
all_files = []


def get_files(url, file_list):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    subdirs = []

    for link in soup.find_all('a'):
        href = link.get('href')
        full_url = urljoin(url, href)

        if href and href.endswith('/'):
            subdirs.append(full_url)
        elif href and not href.endswith('/') and (
                   href.endswith('7z') or
                   href.endswith('gz') or
                   href.endswith('txt') or
                   href.endswith('asc') or
                   href.endswith('mp3') or
                   href.endswith('ogg') or
                   href.endswith('html') or
                   href.endswith('bz2')
        ):
            print(full_url)
            file_list.append(full_url)

    return subdirs


def process_directory(url):
    subdirs = get_files(url, all_files)

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        future_to_url = {executor.submit(process_directory, subdir): subdir for subdir in subdirs}
        for future in concurrent.futures.as_completed(future_to_url):
            future.result()

    return all_files

def main():
    base_url = "https://gentoo.osuosl.org/distfiles/"
    all_files = process_directory(base_url)

    for file in all_files:
        print(file)


if __name__ == "__main__":
    main()