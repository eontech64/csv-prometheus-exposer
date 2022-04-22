from prometheus_client import start_http_server, Gauge
from time import sleep

def process_request(csvFilePath):

    # Read file last line
    with open(csvFilePath) as file:
        content = file.readlines()
    row = content[-1]
    row = row[20:-1].split(",")

    # function to dump data
    index = 0
    for item in row:
        gauge[index].set(item)   # Set to a given value
        index+=1

if __name__ == '__main__':

    # CSV File path
    csvFilePath= r'kpis.csv'
    gauge = []

    # Read file header
    with open(csvFilePath) as file:
        content = file.readlines()
    header = content[:1]
    header = header[0][5:-1]
    header = header.split(",")

    for item in header:
        g = Gauge(item, 'Description')
        gauge.append(g)
    
    # Start up the server to expose the metrics.
    start_http_server(3000)
    while True:
        process_request(csvFilePath)
        sleep(15)
