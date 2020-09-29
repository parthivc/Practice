# https://realpython.com/python-concurrency/

# Import for website testing
import requests

# No imports for synchronous version required

# Imports for threaded version:
import threading
import concurrent.futures


# Imports for system functions
import time
import sys



def synchronousTest(sites):
    def download_site(url, session):
        with session.get(url) as response:
            sys.stdout.write("\rContent: {} | URL: {}".format(len(response.content), url))
            sys.stdout.flush()

    def download_all_sites(sites):
        with requests.Session() as session:
            for url in sites:
                download_site(url, session)
    
    print("\nRunning synchronous IO-bound test")
    startTime = time.time()
    download_all_sites(sites)
    duration = time.time() - startTime
    print(f"\nDownloaded {len(sites)} sites in {duration} seconds")


def threadedTest(sites):
    thread_local = threading.local()

    def get_session():
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session

    def download_site(url):
        session = get_session()
        with session.get(url) as response:
            sys.stdout.write("\rContent: {} | URL: {}".format(len(response.content), url))
            sys.stdout.flush()

    def download_all_sites(sites):
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(download_site, sites)

    print("\nRunning threaded IO-bound test")
    startTime = time.time()
    download_all_sites(sites)
    duration = time.time() - startTime
    print(f"\nDownloaded {len(sites)} sites in {duration} seconds\n")

def main():
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice"] * 50
    synchronousTest(sites)
    threadedTest(sites)


if __name__ == "__main__":
    main()
    
