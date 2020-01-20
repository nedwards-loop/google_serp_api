from serpapi.google_search_results import GoogleSearchResults
import csv
import time

data = []

with open("global_gkw.csv", 'r',encoding='utf-8-sig') as csv_file:
    for line in csv_file:
        new = line.strip()
        print ("new:"+new)
        params = {
            "api_key": "5b4695dcbf33b844d77818346074c2268857ec9c42f24202d18cce2fd1709ba3",
            "engine": "google",
            "q": new,
            "location": "London, England, United Kingdom",
            "google_domain": "google.co.uk",
            "gl": "uk",
            "hl": "en",
            "no_cache":"true",
             "device": "mobile",}
        client = GoogleSearchResults(params)
        #results = client.get_dict()
        time.sleep(2)
        json_results = client.get_json()
        


        
        try:
            for position in json_results['ads']:
                data.append(new+":"+position['displayed_link']+":"+str(position['position']))
                
                #print (json_results)
                
              #  with open('fileName.csv', "wb") as csv_file:
                   # writer = csv.writer(csv_file, delimiter =":")
                  # writer.writerow(data)
                
        except Exception:
            print ("there was an exception:"+new)
            data.append(new+":"+"bugger-no ads")
            #with open('fileName.csv', "w") as csv_file:
             #   writer = csv.writer(csv_file, delimiter =":")
              #  writer.writerow(data)
                
    
            pass
        
#print (data)    
    
#with open('fileName.csv', "a") as csv_file:
  ##  writer = csv.writer(csv_file, delimiter =":")
   # writer.writerow(data)


#for row in data:
 #   print (row)   
MyFile=open('output.txt','w')

for element in data:
    MyFile.write(element)
    MyFile.writ
