import requests, re, os, bs4, json


def get_res(url, cookies=None):
    res = requests.get(url=url, cookies=cookies)
    res.encoding = 'utf-8'
    res.raise_for_status()
    if res.status_code == 200:
        return res
    else:
        return None


def get_page_number(url, cookies=None):
    res = get_res(url, cookies)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    prev_urls = soup.find('div', 'btn-group-paging').find('a').next_sibling.next_sibling['href']
    page_number = int(''.join(re.findall(r'\d+', os.path.basename(prev_urls))))
    return page_number


def get_article(res, base_url=None):
    article = []
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for block in soup.select('div.r-ent'):
        push_star = block.find('div', 'nrec').text
        push_star_count = 0
        if push_star:
            try:
                push_star_count = int(push_star)
            except:
                if push_star == '爆':
                    push_star_count = 99
                elif push_star.startswith('X'):
                    push_star_count = -10
        # print(push_star_count)
        try:
            mark = block.find('div', 'mark').text
            title = block.find('div', 'title').text.strip()
            href = base_url + block.find('a')['href']
            # date = block.find('div', 'meta').text.replace('\n', ' ').strip().split(' ')[0]
            date = block.find('div', 'date').text.strip()
            author = block.find('div', 'author').text.strip()

            article.append({
                'star': push_star_count,
                'title': title,
                'date': date,
                'author': author,
                'mark': mark,
                'href': href
            })
        except:
            continue

    # for link_buttons in soup.select('div.btn-group-paging'):
    #     prev_url = base_url + link_buttons.a.next_sibling.next_sibling['href']
    prev_url = base_url + soup.find('div', 'btn-group-paging').find('a').next_sibling.next_sibling['href']

    return article, prev_url


def write_file(file_name, stuff):
    file = open(file_name, 'a')
    json_format = json.dumps(stuff)
    file.write(json_format)
    file.write('\n')
    file.close()
    return json_format


WANTED_STARS = 99
PPT_URL = 'https://www.ptt.cc'
while True:
    try:
        # wanted_pages = input('How many pages do you want to crawl? (numbers, all)\n')
        wanted_pages = input('What index page do you want to begin crawling with? (numbers or all)\n')
        if wanted_pages == 'all':
            url = PPT_URL + '/bbs/Gossiping/index.html'
            html_index_number = get_page_number(url, {'over18': '1'}) + 1
            url = PPT_URL + '/bbs/Gossiping/index%s.html' % str(html_index_number)
            break
        elif int(wanted_pages):
            html_index_number = int(wanted_pages) + 1
            url = PPT_URL + '/bbs/Gossiping/index%s.html' % str(html_index_number)
            break
        else:
            continue
    except Exception as err:
        print('Don\'t mess around!  numbers or all.\n')
        # print('Error: %s' % err)

while html_index_number > 1:
    res = get_res(url, {'over18': '1'})
    articles, prev_urls = get_article(res, PPT_URL)
    print('Crawling ' + prev_urls + '...')
    for article in articles:
        if article['star'] >= WANTED_STARS:
            print(article['star'], article['title'], article['href'])
            print('    ' + article['date'], article['author'])
            print(write_file('test.json', article))
            print()
            # for k, v in article.items():
            #     print(k + ': ' + str(v))
            # print()

    url = prev_urls
    html_index_number = int(''.join(re.findall(r'\d+', os.path.basename(prev_urls))))
print('Done...')

