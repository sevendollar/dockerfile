import bs4, re, os, time, requests, sys, threading
from urllib.request import urlretrieve


def get_res(url, cookies=None, timeout=2):
    for _ in range(3):
        try:
            res = requests.get(url, cookies=cookies, timeout=timeout)
            return res
        except:
            pass
    return None


def get_picture(start_point=''):
    BASE_URL = 'https://xkcd.com'
    url = BASE_URL + '/' + str(start_point)
    # while not url.endswith('#'):
    for _ in range(50):
        res = get_res(url)
        if res is None:
            print('Connection failed...')
            break
        else:
            try:
                soup = bs4.BeautifulSoup(res.text, 'lxml')
                prev_link = soup.find('ul', 'comicNav').li.next_sibling.next_sibling.a['href']
                img_link = soup.find(attrs={'id': 'comic'}).img['src']
                img_url = 'https:' + img_link
                url = BASE_URL + str(prev_link)
                print('Downloading %s...' % os.path.basename(img_link))
                urlretrieve(img_url, os.path.join('xkcd', os.path.basename(img_link)))
            except TypeError as err:
                pass
            except:
                pass
    return None


os.makedirs('xkcd', exist_ok=True)
thread_list = []
start_time = time.time()
for i in range(1900, 0, -50):
    thread_i = threading.Thread(target=get_picture, args=(i,))
    thread_list.append(thread_i)
    thread_i.start()
for thread in thread_list:
    thread.join()
end_time = time.time()
print('\nDone!')
print('It took %s to download all pictures...' % str(round(end_time - start_time)))
