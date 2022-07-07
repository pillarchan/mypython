import os
from dotenv import load_dotenv
load_dotenv()

items = [{'name':'kf','ymlPath1':'kfkfkf1','ymlPath2':'kfkfkf2','hostsPath':'kfkfkf'},
{'name':'kf1','ymlPath1':'kfkfkf11','ymlPath2':'kfkfkf21','hostsPath':'kfkfkf1'},
{'name':'kf2','ymlPath1':'kfkfkf12','ymlPath2':'kfkfkf22','hostsPath':'kfkfkf2'},
{'name':'kf3','ymlPath1':'kfkfkf13','ymlPath2':'kfkfkf23','hostsPath':'kfkfkf3'},
{'name':'kf4','ymlPath1':'kfkfkf14','ymlPath2':'kfkfkf24','hostsPath':'kfkfkf4'}
]
def readenv():
    ID = os.getenv('ID')
    return ID
def main():
    ID = readenv()
    def getitem():
        for i in items:
            if(i['name'] == 'kf'):
                return i
    item = getitem()
    if(False):
        print(item['ymlPath1'])
    else:
        print(item['ymlPath2'])

if __name__ == "__main__":
    main()