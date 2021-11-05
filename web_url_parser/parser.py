from bs4 import BeautifulSoup
import requests
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="set url for search", required=True)
parser.add_argument("--file", help="save results in file")
args = parser.parse_args()


def trim_url(url):
    return url.replace('https://', '').replace('http://', '').split('/')[0]


def get_all_a_href(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.prettify()

    urls = []
    for some_url in soup.find_all('a', href=True):
        for external_tag in ['http://', 'https://']:
            if external_tag in some_url['href']:
                if trim_url(url) not in trim_url(some_url['href']):
                    urls.append(some_url['href'])
    return urls


def format_urls(url_list):
    return '\n'.join(url_list)


parent_results = get_all_a_href(args.url)
if len(parent_results) > 0:

    if args.file:
        with open(args.file, 'w') as file:
            file.write(format_urls(parent_results))
            for parent_url in parent_results:
                result_child_url = get_all_a_href(parent_url)
                file.write(f"\n\n--- For {parent_url} found {len(result_child_url)} links: ---\n")
                file.write(format_urls(result_child_url))
        print(f'Result saved in file {args.file}')
    else:
        print('Founded results:')
        print(format_urls(parent_results))
        for parent_url in parent_results:
            result_child_url = get_all_a_href(parent_url)
            print(f"--- For {parent_url} found {len(result_child_url)} links: ---")
            print(format_urls(result_child_url))
else:
    print('Not found')
