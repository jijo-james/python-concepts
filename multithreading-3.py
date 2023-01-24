
import time
import concurrent.futures

#threading using context managers
start_time = time.time()
def do_something(seconds):
    print('Sleeping for {} seconds'.format(seconds))
    time.sleep(seconds)
    return 'Done sleeping for {} seconds'.format(seconds)


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

print('finished in {} seconds'.format(time.time() - start_time))