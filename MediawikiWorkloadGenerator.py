# Example 1: asynchronous requests with larger thread pool
import asyncio
import concurrent.futures
import requests
import random
import math
import time
import sys
import datetime

counter = 0

random.seed(0)

maxWorkers = int(sys.argv[1])
numberOfRequests = int(sys.argv[2])
runningDuration = float(sys.argv[3])
fileName = str(sys.argv[4])

#numberOfRequests = int(sys.argv[1])
#runningDuration = float(sys.argv[2])
#fileName = str(sys.argv[3])

out = open(fileName, "a")
Links = open("links.out", 'r')

links = Links.readlines()
links = [l.strip() for l in links]

host = 'http://192.168.245.53:8082'
#LINK = 'gw/index.php/Porsche_935'

print('Experiment is launching ...')
print('Experiment start time:', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=out)

async def main(executor):
    global counter

    #with concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkers) as executor:
    #with concurrent.futures.ProcessPoolExecutor(max_workers=maxWorkers) as executor:
        
        #selected_link = random.choice(links)
    random.seed(0)
    
    loop = asyncio.get_event_loop()
        
    futures = [
        loop.run_in_executor(
            executor, 
            requests.get, 
            str(host + random.choice(links))               
        )
            
        for i in range(numberOfRequests)
    ]

    for response in await asyncio.gather(*futures):
        print(response.status_code, response.elapsed.total_seconds(), file=out)
    
    #completed, pending = await asyncio.wait(futures)
    #results = [ response.result() for response in completed ]
    #print(results(0) + "," + str(results.elapsed.total_seconds()), file=out)

    counter = counter + 1
 
experiment_start_time = time.time()

executor = concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkers)

event_loop = asyncio.get_event_loop()

while (time.time() - experiment_start_time) < runningDuration:
    try:
        event_loop.run_until_complete(main(executor))
    finally:
        #event_loop.close()
        print('Current iteration number', counter)
   
print('Experiment finish time:', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=out)
print ('Total number of iteration:', counter, file=out)
