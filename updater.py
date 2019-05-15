import json
import urllib.request as urllib2

def check_for_updates():
    path_json = "./version.json"
    path_remote = "https://raw.githubusercontent.com/CatLearned/CelsiusArteTeint/master/version.json"

    print("Hello world")

    with open(path_json) as json_file:
        print(open(path_json))
        json_data = json.load(json_file)
        print(json_data)
        p_name = json_data['Program name']
        p_vers = json_data['Version']
    print("Program name is", p_name, "\nVersion is", p_vers)
    response = urllib2.urlopen(path_remote)
    html = response.read().decode('cp1251')
    print(html)
    #with html as json_file:
    #json_data = json.load(html)
    #a_name = json_data['Program name']
    #a_vers = json_data['Version']
    #print("Actual name is", a_name, "\nVersion is", a_vers)

check_for_updates()