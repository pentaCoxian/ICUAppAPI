import yakeluso
import scrape

def get_database():
    from pymongo import MongoClient
    import pymongo
    import certifi
    ca = certifi.where()

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://python:lolpython556@pythondev.etdrtaj.mongodb.net/pythondev"
    client = MongoClient(CONNECTION_STRING, tlsCAFile=ca)
    return client['icu']
    
if __name__ == "__main__":    
    

    # Get the database
    dbname = get_database()
    collection_name = dbname["courseOfferings"]
    collection_name.insert_many(yakeluso.getCourseInfo())


    regIdList = []
    for x in collection_name.find({}, {"rgno":1}):
        regIdList.append(x['_id'])
    print(regIdList)
    collection_name = dbname["courseSyllabus"]
    collection_name.insert_many(scrape.getSyllabus("2022",regIdList))