import requests, bs4, os

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        imgSrc = soup.find('div', attrs={'id': 'comic'}).img.get('src')
        imgUrl = 'http:' + imgSrc
        imgTitle = soup.find('div', attrs={'id': 'ctitle'}).text
        print('Going to url: %s (%s)' % (imgTitle, prevUrl.replace('/', '')))
        res = requests.get(imgUrl)
        imgFile = open(os.path.join(os.getcwd(), 'xkcd', os.path.basename(imgUrl)), 'wb')
        for chuck in res.iter_content(1000000):
            imgFile.write(chuck)
        imgFile.close()
        print('Downloading image: %s...' % imgUrl)
    except Exception as err:
        print('Oops, there\'s an error: %s' % err)

    prevUrl = soup.find('a', attrs={'rel': 'prev'}).get('href')
    url = 'https://xkcd.com' + prevUrl
print('done!')
