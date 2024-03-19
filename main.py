from jsonEditor import readJsonFile
import requests
import threading
import os

def downloadImage(url, imageName):
    response = requests.get(url)
    with open(f"images/{imageName}.jpg", "wb") as f:
        f.write(response.content)

def task(urls: list, groupCode: str):
    for index, url in enumerate(urls):
        imageName = groupCode + str(index + 1)
        downloadImage(url=url, imageName=imageName)
        print(f'{imageName}.jpg downloaded!')

jsonFiles = os.listdir('./imageUrl')
print(f"讀取到json file: {jsonFiles}")

groupCodeList = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]
threadArray = []

for index, jsonFilename in enumerate(jsonFiles):

    urls = readJsonFile(f'imageUrl/{jsonFilename}')
    
    threadArray.append(threading.Thread(target=task, args=(urls, groupCodeList[index])))
    
for thread in threadArray:
    thread.start()
    print(f'{thread} start!')

for thread in threadArray:
    thread.join()
    print(f'{thread} join')

print('down.')
