import urllib.request
import json
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        return super().handle_comment(data)
    
    def handle_starttag(self, tag, attrs):
        return super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        return super().handle_endtag(tag)

    def handle_data(self, data):
        return super().handle_data(data)

def main():
    webUrl = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printJsonData(data)
    else:
        print("Error in opening the URL")

def printJsonData(data):
    jsonData = json.loads(data)

    if "title" in jsonData["metadata"]:
        print(jsonData["metadata"]["title"])

    if "count" in jsonData["metadata"]:
        count = jsonData["metadata"]["count"]
        print(str(count) + " events recorded")

    if "features" in jsonData:
        features = jsonData["features"]
        for f in features:
            place = f["properties"]["place"]
            magnitude = f["properties"]["mag"]
            feltBy = f["properties"]["felt"]
            print("Earthquake of magnitude " + str(magnitude) + " felt by " + str(feltBy) + " people at " + place)

def parseHtml():
    myParser = MyHTMLParser()
    f = open("sample.html")
    if (f.mode == 'r'):
        contents = f.read()
        myParser.feed(contents)

if __name__ == "__main__":
    main()