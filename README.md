Ad Duration Extractor
This Python script fetches ad data from a specified VAST ad service, parses the XML response, extracts the <Duration> tags, and calculates the total duration and response rates for each request. The script allows multiple requests to be made in a loop, based on user input, and outputs the total duration and average response rate.

Features
Generates a random cache buster for each request to ensure the response is not cached.
Sends multiple requests to a VAST ad server to fetch ad XML responses.
Extracts the <Duration> values from the XML responses, converts them to seconds, and calculates total duration.
Calculates the response rate, which is the ratio of total ad duration to a pod duration of 120 seconds.
Provides a final summary of the total duration and the average response rate over all requests.
Prerequisites
Make sure you have Python installed on your system (version 3.x is recommended).

You will also need the following Python packages:

requests: For making HTTP requests to the ad server.
xml.etree.ElementTree: This is a standard Python library, so you don't need to install it separately.
If you don't have requests installed, you can install it using pip:

bash
Copy code
pip install requests
Usage
Clone or download this repository.

Open a terminal/command prompt and navigate to the project directory.

Run the Python script by typing:

bash
Copy code
python ad_duration_extractor.py
You will be prompted to enter the number of times you want the script to run:

bash
Copy code
How many times do you want to run the code? 5
The script will then fetch the ad data 5 times, extract the durations, and print the results for each request.

Script Structure
Functions
randomGen(): Generates a random 10-digit number to be used as a cache buster in the URL.
modify_CB(url): Modifies the URL by replacing the placeholder [] with the generated cache buster.
extractDurations(xml_content): Parses the VAST XML response and extracts the <Duration> elements, converting them to seconds.
run_ads(num): The main function that runs the process num times, prints the duration and response rate for each request, and calculates the total and average response rates.
Example Output
text
Copy code
Pulling data from: https://ads.aistrm.net/v1/ads?app_bundle=com.cltv.cltv&format=vast&cb=1234567890&ip=108.84.47.69&content_channel=36&pod_duration=120&
Durations extracted: [30, 45, 60]
Total duration for this link is 135 seconds
Response rate for this link is 1.125

Pulling data from: https://ads.aistrm.net/v1/ads?app_bundle=com.cltv.cltv&format=vast&cb=0987654321&ip=108.84.47.69&content_channel=36&pod_duration=120&
Durations extracted: [15, 60, 30]
Total duration for this link is 105 seconds
Response rate for this link is 0.875

Total Duration after running 5 times is: 240 seconds.
The average response rate is: 1.000
Error Handling
If the XML response is malformed, the script will catch the parsing error and print an error message.
If the HTTP request fails (non-200 status code), the script will display the status code of the failed request.
License
This project is open-source and free to use.