###Copying the image with chunks:
'''
with open("jijo.jpeg", "rb") as rf:
    with open("bronx_copy.jpeg", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        count = 0
        #print(rf_chunk)
        while len(rf_chunk) > 0:
            count += 1
            print(rf.tell())
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

print(count)
'''

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2
print(f'{total:,}')