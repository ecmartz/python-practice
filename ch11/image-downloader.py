#!python3

import requests, sys, bs4, os

if __name__ == "__main__":
    res = requests.get('https://imgur.com/search?q='+sys.argv[1])
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    soup.find_all()

    # Get the src of an image
    # soup.findAll('a', 'image-list-link')[0].find('img')['src']

    img_hrefs = []
    for i in soup.find_all('a', 'image-list-link'):
        img_href = 'http:'+str(i.find('img')['src'])
        img_hrefs.append(img_href)

    for a in img_hrefs:
        img_file = open(os.path.join(str(sys.argv[1]), os.path.basename(a)), 'wb')
        res = requests.get(a)
        for chunk in res.iter_content(10000):
            img_file.write(chunk)
        img_file.close()

    # TODO : Create the directory first

    # TODO : Could get higher res photos