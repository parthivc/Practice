# System that takes in a list of URLs and distributes them across many threads

import io
import random
import shutil
import sys
import multiprocessing
import pathlib
import requests
from PIL import Image
import time


def getURLs():
    try:
        urlInput = sys.argv[1]
    except IndexError:
        print('ERROR: Please provide the txt file\n Example \n\n$python imageDownloader.py dogs.txt \n\n')
        sys.exit()
    with open(urlInput, 'r') as f:
        imageURLs = f.read().splitlines()
    print('{} images detected'.format(len(imageURLs)))
    return imageURLs


def imageDownloader(urls):
    print(f'Downloading: {img_url}')
    res = requests.get(img_url, stream=True)
    count = 1
    while res.status_code != 200 and count <= 5:
        res = requests.get(img_url, stream=True)
        print(f'Retry: {count} {img_url}')
        count += 1
    # checking the type for image
    if 'image' not in res.headers.get("content-type", ''):
        print('ERROR: URL does not appear to be an image')
        return False
    try:
        imageName = str(img_url[(img_url.rfind('/')) + 1:])
        if '?' in imageName:
            image_name = image_name[:image_name.find('?')]
    except:
        image_name = str(random.randint(11111, 99999))+'.jpg'

    i = Image.open(io.BytesIO(res.content))
    download_location = get_download_location()
    i.save(download_location + '/'+image_name)
    return f'Download complete: {img_url}'


def downloadURLs(process: int, images_url: list):
    print(f'MESSAGE: Running {process} process')
    results = ThreadPool(process).imap_unordered(imageDownloader, images_url)
    for r in results:
        print(r)


def main():
    startTime = time.time()
    processCount = multiprocessing.cpu_count() // 2
    urls = getURLs()
    downloadURLs(processCount, urls)
    duration = time.time() - startTime
    print("\nTime Taken: {:.4f} seconds\nURLs downloaded: {}\n".format(duration, len(urls)))


if __name__ == "__main__":
    main()
