<h1>Ad Duration Extractor</h1>

<p>This Python script fetches ad data from a specified VAST ad service, parses the XML response, extracts the <code>&lt;Duration&gt;</code> tags, and calculates the total duration and response rates for each request. The script allows multiple requests to be made in a loop, based on user input, and outputs the total duration and average response rate.</p>

<h2>Features</h2>
<ul>
  <li>Generates a random cache buster for each request to ensure the response is not cached.</li>
  <li>Sends multiple requests to a VAST ad server to fetch ad XML responses.</li>
  <li>Extracts the <code>&lt;Duration&gt;</code> values from the XML responses, converts them to seconds, and calculates total duration.</li>
  <li>Calculates the response rate, which is the ratio of total ad duration to a pod duration of 120 seconds.</li>
  <li>Provides a final summary of the total duration and the average response rate over all requests.</li>
</ul>

<h2>Prerequisites</h2>
<p>Make sure you have Python installed on your system (version 3.x is recommended).</p>
<p>You will also need the following Python package:</p>
<ul>
  <li><code>requests</code>: For making HTTP requests to the ad server.</li>
</ul>
<p>If you don't have <code>requests</code> installed, you can install it using pip:</p>

<pre><code>pip install requests
</code></pre>

<h2>Usage</h2>
<ol>
  <li>Clone or download this repository.</li>
  <li>Open a terminal/command prompt and navigate to the project directory.</li>
  <li>Run the Python script by typing:</li>
</ol>

<pre><code>python ad_duration_extractor.py
</code></pre>

<p>You will be prompted to enter the number of times you want the script to run:</p>

<pre><code>How many times do you want to run the code? 5
</code></pre>

<p>The script will then fetch the ad data 5 times, extract the durations, and print the results for each request.</p>

<h2>Script Structure</h2>

<h3>Functions</h3>
<ul>
  <li><code>randomGen()</code>: Generates a random 10-digit number to be used as a cache buster in the URL.</li>
  <li><code>modify_CB(url)</code>: Modifies the URL by replacing the placeholder <code>[]</code> with the generated cache buster.</li>
  <li><code>extractDurations(xml_content)</code>: Parses the VAST XML response and extracts the <code>&lt;Duration&gt;</code> elements, converting them to seconds.</li>
  <li><code>run_ads(num)</code>: The main function that runs the process <code>num</code> times, prints the duration and response rate for each request, and calculates the total and average response rates.</li>
</ul>

<h3>Example Output</h3>

<pre><code>Pulling data from: https://ads.aistrm.net/v1/ads?app_bundle=com.cltv.cltv&format=vast&cb=1234567890&ip=108.84.47.69&content_channel=36&pod_duration=120&
Durations extracted: [30, 45, 60]
Total duration for this link is 135 seconds
Response rate for this link is 1.125

Pulling data from: https://ads.aistrm.net/v1/ads?app_bundle=com.cltv.cltv&format=vast&cb=0987654321&ip=108.84.47.69&content_channel=36&pod_duration=120&
Durations extracted: [15, 60, 30]
Total duration for this link is 105 seconds
Response rate for this link is 0.875

Total Duration after running 5 times is: 240 seconds.
The average response rate is: 1.000
</code></pre>

<h3>Error Handling</h3>
<ul>
  <li>If the XML response is malformed, the script will catch the parsing error and print an error message.</li>
  <li>If the HTTP request fails (non-200 status code), the script will display the status code of the failed request.</li>
</ul>

<h2>License</h2>
<p>This project is open-source and free to use.</p>
