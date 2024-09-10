import requests
import xml.etree.ElementTree as ET
import random

# Generates a random cache buster number each time the function is called
def randomGen():
    return random.randint(1000000000, 9999999999)  # Ensures a 10-digit random number

# Original Office URL
url = "https://ads.aistrm.net/v1/ads?app_bundle=com.cltv.cltv&format=vast&cb=[]&ip=108.84.47.69&content_channel=36&pod_duration=120&"

# Function to replace the '[]' in the URL with a random cache buster value
def modify_CB(url):
    new_cb = randomGen()
    modified_url = url.replace('[]', str(new_cb))
    return modified_url

# Function to extract durations from the XML response
# This function searches for <Duration> tags and converts the HH:MM:SS format into seconds
def extractDurations(xml_content):
    durations = []
    try:
        root = ET.fromstring(xml_content)  # Parse the XML response
        for duration in root.iter('Duration'):  # Iterate through all <Duration> elements
            duration_text = duration.text  # Extract the text content of the <Duration> element
            time_parts = duration_text.split(':')  # Split by ":" to get hours, minutes, and seconds
            # Convert HH:MM:SS format to seconds
            seconds = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + int(time_parts[2])
            durations.append(seconds)  # Add the duration in seconds to the list
    except ET.ParseError as e:  # Handle any parsing errors
        print("Error parsing the XML: ", e)
    return durations  # Return the list of extracted durations in seconds

# Function that runs the ad requests `num` times and calculates total duration and response rates
def run_ads(num):
    totalDuration = 0  # Variable to accumulate the total duration in seconds
    totalResponseRate = 0  # Variable to accumulate the total response rate

    for count in range(num):
        new_url = modify_CB(url)  # Modify the URL with a random cache buster
        print(f"Pulling data from: {new_url}")
        
        # Send a GET request to the modified URL
        response = requests.get(new_url)
        
        if response.status_code == 200:  # Check if the request was successful
            durations = extractDurations(response.text)  # Extract durations from the XML response
            
            if durations:
                print(f"Durations extracted: {durations}")
                CurrentDuration = sum(durations)  # Sum all durations for this response
                print(f"Total duration for this link is {CurrentDuration} seconds\n")
                
                # Response rate is the duration divided by the pod duration (120 seconds in this case)
                responseRate = CurrentDuration / 120
                print(f"Response rate for this link is {responseRate}\n")
                
                # Accumulate the total duration and response rate
                totalDuration += CurrentDuration
                totalResponseRate += responseRate
            else:
                print("Cannot find duration in this link.")
        else:
            print(f"Request failed with the response code: {response.status_code}.")

    # Calculate the average response rate
    averageResponseRate = totalResponseRate / num if num > 0 else 0

    # Print the total duration and average response rate after all iterations
    print(f"Total Duration after running {num} times is: {totalDuration} seconds.")
    print(f"The average response rate is: {averageResponseRate}")

# Get the number of times the user wants to run the code
num = int(input("How many times do you want to run the code? "))
run_ads(num)
