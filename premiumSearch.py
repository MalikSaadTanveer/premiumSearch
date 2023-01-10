import re
import math
from collections import Counter
import mydata
from  spacyAlgo import removeStopWords
from removeWeightedWords import removeWeightedWords
from operator import itemgetter
from flask import Flask,request,jsonify
import json
import pymongo
from flask_cors import CORS
import bson.json_util as json_util
from datetime import date

# Initialize by Dataset
# client = pymongo.MongoClient('mongodb+srv://maliksaad:maliksaad123@cluster0.2ztru3w.mongodb.net/?retryWrites=true&w=majority')

# db = client.get_database('freelance-learning-platform')
# collection = db['premiumsearchs']
# collectionGigs = db['gigs']
# collectionUser = db['users']

# print("It is a client ",client.db)

# try:
#     client = pymongo.MongoClient('mongodb+srv://maliksaad:maliksaad123@cluster0.2ztru3w.mongodb.net/?retryWrites=true&w=majority')
#     db = client.get_database('freelance-learning-platform')
#     collection = db['premiumsearchs']
#     collectionGigs = db['gigs']
#     collectionUser = db['users']
#     print("Connected Successfully")
# except pymongo.errors.ConnectionFailure as e:
#     print("Could not connect to MongoDB: %s" % e)



client = pymongo.MongoClient('mongodb+srv://maliksaad:maliksaad123@cluster0.2ztru3w.mongodb.net/?retryWrites=true&w=majority')
# client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.get_database('test')
collection = db['premiumsearchs']
collectionGigs = db['gigs']
collectionUser = db['users']
print("Connected Successfully")





# Cosine Similarity between two vectors
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator




# String to Vector
def text_to_vector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    return Counter(words)


# get Single Result
def get_result(text1, text2):
    # text1 = content_a
    # text2 = content_b

    vector1 = text_to_vector(text1)
    # print(vector1)
    vector2 = text_to_vector(text2)
    # print(vector2)

    cosine_result = get_cosine(vector1, vector2)
    return cosine_result

app = Flask(__name__)
CORS(app)

@app.route('/premiumSearch',methods=['POST'])
def predict():
    
    # Input String for Search
    # inputString=input('Please enter your search string here..')
    inputString= request.json['searchString']

    # Predefined Keywords that have high weightage
    searchList = ['Python','Java','JavaScript','PHP','Ruby','Swift','Perl','SQL','Kotlin','Scala','Objective-C','Assemblylanguage','Rust','Fortran','MATLAB','COBOL','Ada','Haskell','Dart','VisualBasic','C++','c#','csharp','Lua','BASIC','Pascal','Prolog','Julia','Groovy','Erlang','HTML','ALGOL','APL','CSS','Elixir','Scriptinglanguage','CoffeeScript','Tcl','AppleScript','OCaml','ActionScript','VBScript','ECMAScript','AutoLISP','EmacsLisp','android','website','react','js','node','mongodb','express','mernstack','angular','vue','meanstack','jamstack','django','api','xml']


    # Get Keywords from the Search String
    searchString = inputString.lower().replace(" ",'')
    print(searchString)

    inputKeywordsList= []

    for word in searchList:
        if word.lower() in searchString:
            inputKeywordsList.append(word.lower())


    print(inputKeywordsList)

    str1 = ""
 
    # traverse in the string
    for ele in inputKeywordsList:
        str1 += ele+" "
   
    print(str1)
    # for x in collection.find():
    # for x in collection.aggregate([{"$search": {"index": 'search',"text": {"query": str1,"path": ['projects.keywords',],}}},]):
    # for x in collection.find({'projects.keywords': { '$in': [inputKeywordsList[0],inputKeywordsList] }}):

    arr = []
    for x in collection.aggregate([{"$search": {"index": 'search',"text": {"query": str1,"path": ['projects.keywords',],}}},]):
        arr = arr + [x]
    # arr = list(arr)
    print(arr)



    # return "Hello"
    # get All the freelancers who is having the similar projects done
    usersArray = []
    count = 0
    dataset= arr
    for data in dataset:
        for project in data['projects']:
            count = 0
            check = any(item in inputKeywordsList for item in project['keywords'])
            if check:
                if len(usersArray) == 0:
                    print('not in')
                    usersArray.append({
                        'sellerId':data['sellerId'],
                        'projects':[project]
                    })
                else:
                    print('yes In')
                    dum = usersArray
                    for userItem in dum:
                        if(userItem['sellerId'] == data['sellerId']):
                            count = count + 1
                            dummy = userItem
                            dummy['projects'].append(project)
                            usersArray.remove(userItem)
                            usersArray.append(dummy)

                    if count == 0:
                        usersArray.append({
                        'sellerId':data['sellerId'],
                        'projects':[project]
                    })
                


    # Here I have all the freelancers data
    print('This is my userArray:')
    print(len(usersArray))
    print(usersArray)

    dumUserArray = usersArray

    for singleOrder in usersArray:
        for projects in singleOrder['projects']:
            data = collectionGigs.find_one({"_id":projects['gigId']},{'title':1,'searchTags':1,'description':1})
            projects['gigTitle'] = data['title']
            projects['searchTags'] = data['searchTags']
            projects['gigDescription'] = data['description']
            
        data = collectionUser.find_one({"_id":singleOrder['sellerId']},{'ratings':1,'createdAt':1})
        singleOrder['ratings'] = data['ratings']
        singleOrder['createdAt'] = data['createdAt']


    

    print("NEW USER ARRAY")
    print(usersArray)

    # return jsonify({"data":'Yes'})


    # Here I have remove all the weighted keywords
    originalInput = removeWeightedWords(inputString)

    #Remove StopWords
    inputAfterSpacy = removeStopWords(originalInput)
    print(inputAfterSpacy)


    # Calculate the cosine Similarity
    calculateList = []
    descCal = 0
    titleCal = 0
    tagsCal = 0
    gigDesc = 0
    for user in usersArray:
        descCal = 0
        titleCal = 0
        tagsCal = 0
        gigDesc = 0
        for userProjects in user['projects']:
            out1 = removeWeightedWords(userProjects['desc'])
            out2 = removeStopWords(out1)
            print('Spacy WOrds'+out2)
            descCal = descCal + get_result(inputAfterSpacy,out2)
            titleCal = titleCal + get_result(inputString,userProjects['gigTitle'])
            gigDesc = gigDesc + get_result(inputString,userProjects['gigDescription'])
            tagsCal = tagsCal + get_result(''.join(inputKeywordsList),''.join(userProjects['searchTags']))
            print(get_result(inputAfterSpacy,out2))

        today = str(date.today()).split('-')
        today = list(map(int,today))
        createdDate = str(user['createdAt'])
        print(str(createdDate))
        createdDate = (createdDate[0:createdDate.index(' ')]).split('-')
        createdDate = list(map(int,createdDate))
        d0 = date(createdDate[0], createdDate[1], createdDate[2])
        d1 = date(today[0], today[1], today[2])
        delta = d1 - d0
        delta = int(str(delta).split(" ")[0]) / 100
        print(delta)

        newCal = ((descCal / len(user['projects'])) * 0.45) + ( (titleCal / len(user['projects'])) * 0.15) + ( (tagsCal / len(user['projects'])) * 0.15) + ( (gigDesc / len(user['projects'])) * 0.10) + ( user['ratings'] * 0.10) + (delta * 0.05)

        print("THIS is NEW CAL")
        print(newCal)
        if newCal > 0:
            data = collectionUser.find_one({"_id":user['sellerId']},{'name':1,'avatar':1})
            calculateList.append({
                'id':json.loads( json_util.dumps( user['sellerId']) ),
                'name':data['name'],
                'avatar': data['avatar'],
                # 'similarity': newCal
                'similarity': float("{:.4f}".format(newCal))
            })     


    # print(calculateList)
    newlist = sorted(calculateList, key=itemgetter('similarity'), reverse=True) 
    print(newlist)
    return jsonify({"data":newlist})
    # print(get_result('I need a C sharp Developer who can login into account', 'I need a C# Developer login developer account'))




if __name__ == '__main__':
    app.run(debug=True)