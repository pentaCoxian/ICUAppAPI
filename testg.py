import json
import scrape

testRegno = ["32504"]
#"32410","32411","32412","32501","32502","32503",


raw = scrape.getSyllabus("2022",testRegno)
for i in range(len(raw)):
    payload = json.dumps(raw[i])
    print(payload)
    print("\n")
    print("===============================================")
    print("\n")

