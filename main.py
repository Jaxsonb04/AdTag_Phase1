import requests
import xml.etree.ElementTree as ET
import random

def randomGen():
    return random.randint(0000000000,9999999999) #this generates random cache buster everytime

# Original Office URL

url = "https://ads.aistrm.net/v1/ads?app_bundle=com.cltv.cltv&format=vast&cb=[]&ip=108.84.47.69&content_channel=36&pod_duration=120&" 

def modify_CB(url):
    new_cb = randomGen()

    modified_url = url.replace('[]', str(new_cb))
    return modified_url

def extractDurations(xml_content):
    durations = []
    try:
        root = ET.fromstring(xml_content)
        for duration in root.iter('Duration'):
            duration_text = duration.text
            time_parts = duration_text.split(':')
            seconds = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + int(time_parts[2])
            durations.append(seconds)
    except ET.ParaseError as e:
        print("Error parsing the XML: ", e)
    return durations

def run_ads(num):
    totalDuration = 0
    totalResponseRate = 0
    for count in range(num):
        new_url = modify_CB(url)
        print(f"pulling data from: {new_url}")
        response = requests.get(new_url)
        if response.status_code == 200:
            durations = extractDurations(response.text)
            if durations:
                print(f"Duration extraced: {durations}")
                CurrentDuration = sum(durations)
                print(f"total duration for this link is {CurrentDuration}\n")
                responseRate = CurrentDuration/120
                print(f"responseRate for this link is {responseRate}\n")
                totalDuration += CurrentDuration
                totalResponseRate += responseRate 
            else:
                print("cannot find duration in this link")
        else:
            print(f"Request failed with the reponse code: {response.status_code}.")
        averageResponseRate = totalResponseRate/num

    print(f"Total Duration after running {num} times is: {totalDuration}. The average response rate is: {averageResponseRate} ")

num = int(input("How many times you want to the run code? "))
run_ads(num)
        


    