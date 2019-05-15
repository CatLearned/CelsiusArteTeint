import json
import urllib2

def check_for_updates():
    print("Hello world")
    path_json = "./version.json"
    with open(path_json) as json_file:
        json_data = json.load(json_file)
        p_name = json_data['Program name']
        p_vers = json_data['Version']
    print("Program name is", p_name, "\nVersion is", p_vers)

check_for_updates()