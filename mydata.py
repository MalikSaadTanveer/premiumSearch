
import json
import pymongo


dataset = [
    {
        'name': 'A1',
        'id': '1',
        'projects':[
            {
                'desc':'i want mobile app for buy and sell of old things in java or flutter which show price of product some details of product pictures of product',
                'keywords':['java','flutter'],
                'ratings':3.5
            },
            {
                'desc':'require a game in java like tic tac toe user friendly interface work very smooth',
                'keywords':['java'],
                'ratings':4.5
            },
            {
                'desc':'i want a logo for cloth shop in 3d logo must be in mockup form shop name is azad cloth house',
                'keywords':['logo','3dlogo'],
                'ratings':5
            },
        ]
    },
    {
        'name': 'A2',
        'id': '2',
        'projects':[
            {
                'desc':'i want website for blogging in mern stack i am also a YouTuber i also want to link my social media accounts in website',
                'keywords':['mernstack','react','express','node','mongodb','js','website'],
                'ratings':4.5
            },
            {
                'desc':'i want software for my pharmacy like point of sale in c# provide all necessary fields related to pharmacy',
                'keywords':['c#','csharp'],
                'ratings':2.7
            },
            {
                'desc':'i want a video app like tiktok develop using kotlin for android and swift for ios',
                'keywords':['kotlin','swift'],
                'ratings':4.5
            },
            {
                'desc':'i want a video player like mx player develop using java xml for frontend php sql for backend',
                'keywords':['java','xml','sql','php'],
                'ratings':5
            },
        ]
    },
    {
        'name': 'A3',
        'id': '3',
        'projects':[
            {
                'desc':'develop software  using c# for my grocery store also mention delivery option in software',
                'keywords':['c#','csharp',],
                'ratings':4.5
            },
            {
                'desc':'i want android app for my daily workout develop using java or kotlin',
                'keywords':['java','kotlin'],
                'ratings':1.5
            },
        ]
    },
    {
        'name': 'A4',
        'id': '4',
        'projects':[
            {
                'desc':'i want app for win pridiction of daily cricket matches develop using python implement some AI algorithms',
                'keywords':['python','AI',],
                'ratings':4.5
            },
            {
                'desc':'i want a calculator app that is a school project which can add, subtract, multiply and divide, developed using c++',
                'keywords':['c++'],
                'ratings':5
            },
            {
                'desc':'i need a website for marketing purpose of my business about property sell and purchase system so for this i need a simple website in which my past deals were added and my contact for the people. use javascript, html and CSS technology',
                'keywords':['javascript', 'html', 'css','js','html5','css3','website'],
                'ratings':4.5
            },
            {
                'desc':'i need point of sale software for my shoe store for billing purpose which helps me to keep record of stock available and sold stock using C# technology',
                'keywords':['c#','csharp'],
                'ratings':5
            },
            {
                'desc':'i required e-commerce website which helps to run my business globally which helps me to sell clothes  through online services and also add different payment methods on this website using mern stack technology',
                'keywords':['mernstack','react','express','node','mongodb','js','website'],
                'ratings':5
            },
            {
                'desc':'i required a website which helps to order online food from different restaurants using mern stack technology',
                'keywords':['mernstack','react','express','node','mongodb','js','website'],
                'ratings':5
            },
        ]
    },
    ]

# jsonData = json.dumps(dataset,indent=4)
# print(jsonData)
# with open("sample.json", "w") as outfile:
#     outfile.write(jsonData)


# client = pymongo.MongoClient('mongodb://localhost:27017/')
# print(client)
# db = client['freelance-learning-app']
# collectin = db['premiumSearch']

# arr = []
# for x in collectin.find( { 'projects.keywords': { '$in': [ "flutter",'kotlin' ] } }):
#   arr = arr + [x]

# print(arr)