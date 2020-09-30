# https://realpython.com/python-concurrency/

# Import for website testing
import requests

# No imports for synchronous version required

# Imports for threaded version:
import threading
import concurrent.futures

# Imports for the asyncio version
import asyncio
import aiohttp

# Imports for the multiprocessing version
import multiprocessing


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


# requests.Session() is not thread-safe, meaning that the data needs to be protected when its shared between threads
# Using a thread-safe data structure like `from queue import Queue` or ThreadPoolExecutor helps with this
# In the following example, `thread_local` creates an object specific to each thread making the operation thread-safe

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


# In the asyncio example, only a single session is created because they are all running on the same thread
# In the threading example, each thread got it's own session, but the use of a single thread here means there's only 1
# asyncio also scales much better than threading

def asyncioTest(sites):
    async def download_site(session, url):
        async with session.get(url) as response:
            print("", end="")

    async def download_all_sites(sites):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in sites:
                task = asyncio.ensure_future(download_site(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)

    print("\nRunning asyncio IO-bound test")
    startTime = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))  # asyncio.run(download_all_sites(sites))
    duration = time.time() - startTime
    print(f"Downloaded {len(sites)} sites in {duration} seconds\n")


# Multiprocessing is slower in this context because this operation is IO bound
# Meaning that the overhead required to spawn pool workers takes more time than it would with threading or asyncio
# Additionally, these methods are not within submethods like the other examples because of multiprocessing
# In order to map a function to a multiprocessing pool, it must be defined at the top layer of abstraction
# Meaning that it cannot be a nested method

session = None 

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def multiprocessingDownloadSite(url):
    with session.get(url) as response:
        # name = multiprocessing.current_process().name
        sys.stdout.write("\rContent: {} | URL: {}".format(len(response.content), url))
        sys.stdout.flush()

def multiprocessingDownloadAllSites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(multiprocessingDownloadSite, sites)

def multiprocessingTest(sites):
    print("\nRunning multiprocessing IO-bound test")
    startTime = time.time()
    multiprocessingDownloadAllSites(sites)
    duration = time.time() - startTime
    print(f"\nDownloaded {len(sites)} sites in {duration} seconds\n")


def main():
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice"] * 100
    synchronousTest(sites)
    threadedTest(sites)
    asyncioTest(sites)
    multiprocessingTest(sites)


if __name__ == "__main__":
    main()
    
