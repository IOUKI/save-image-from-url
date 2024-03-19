from jsonEditor import readJsonFile
import requests
import threading

def downloadImage(url, imageName):
    response = requests.get(url)
    with open(f"images/{imageName}.jpg", "wb") as f:
        f.write(response.content)

def task(urls: list, groupCode: str):
    for index, url in enumerate(urls):
        imageName = groupCode + str(index + 1)
        downloadImage(url=url, imageName=imageName)
        print(f'{imageName}.jpg downloaded!')

groupCodeList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
threadArray = []

for i in range(7):

    urls = readJsonFile(f'imageUrl/{i + 1}.json')
    
    threadArray.append(threading.Thread(target=task, args=(urls, groupCodeList[i])))
    
for thread in threadArray:
    thread.start()
    print(f'{thread} start!')

for thread in threadArray:
    thread.join()
    print(f'{thread} join')

print('down.')
