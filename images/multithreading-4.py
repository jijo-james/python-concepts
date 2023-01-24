import requests
import time
import concurrent.futures


img_urls = ['https://images.unsplash.com/photo-1666085596628-66d4306f3728?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=411&q=80', 
    'https://images.unsplash.com/photo-1669462126732-95d06d81e066?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80', 
    'https://images.unsplash.com/photo-1669410612248-3bee35aa32ff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80', 
    'https://images.unsplash.com/photo-1669476526639-e390ead82f4b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80', 
    'https://images.unsplash.com/photo-1669054078259-9f305691b761?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=388&q=80']

t_1 = time.perf_counter()

def download_image(url):
    img_bytes = requests.get(url).content
    img_name = url.split('/')[3].split('-')[1]
    img_name = '{}.jpg'.format(img_name)
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print('{} downloaded'.format(img_name))

with concurrent.futures.ThreadPoolExecutor() as executor:
    result = [executor.submit(download_image, url) for url in img_urls]


t_2 = time.perf_counter()
print('\nCompleted in {} seconds'.format(t_2 - t_1))