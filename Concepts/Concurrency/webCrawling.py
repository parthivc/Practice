# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
#  https://code.dennyzhang.com/web-crawler-multithreaded

class HtmlParser(object):
    def __init__(self):
        self.something = 0

    def getUrls(self, url):
       # Gets the URLs from the input
       # Returning dummy value in this example
       return [url]

# A web crawler that implements multithreading

import concurrent.futures

class webCrawler():

    def getHostname(self, url):
        return url.split('/')[2]  # https://

    def crawl(self, baseURL):
        visited = {baseURL}
        queue = [baseURL]
        hostName = self.getHostname(baseURL)
        while queue:
            queue2 = []
            # Temporary set
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                threadResults = list(executor.map(HtmlParser.getUrls, queue))
                for urlLists in threadResults:
                    for url in urlLists:
                        if url not in visited and self.getHostname(url) == hostName:
                            visited.add(url)
                            # add to temporary set
                            queue2.append(url)
            queue = queue2
            # join temporary sets
            # pass temporary set to a consumer worker that actually downloads everything
        return list(visited)


def main():
    crawler = webCrawler()
    baseURL = "http://news.yahoo.com"
    results = crawler.crawl(baseURL)
    print(results)


if __name__ == "__main__":
    main()
