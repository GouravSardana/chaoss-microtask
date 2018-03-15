import urllib.request, json
import csv
#https://api.github.com/repos/aimacode/aima-python/contributors (know about the contributors)
d={} #save all the required name and contribution in dict. form
with urllib.request.urlopen("https://api.github.com/repos/aimacode/aima-python/contributors") as url:
    #open the link using urllib library
    data=json.loads(url.read().decode())   #decode the json code ans save it to data
    print(": Name                  : No Of Commits") #for table formation these are headers which is shown in the console
    for r in data:
        d[r['login']]= r['contributions'] 
        print(":" ,r['login']," "*(20-len(r['login'])),":", #reads the names and how many contribution
              str(r['contributions']))
with open('z.csv','w') as f:  #open a csv file (readmode) 
    w = csv.writer(f,delimiter=',') 
    fieldnames = ['Name', 'No of commits'] #headers
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader() #set the headers into csv
    for key,values in sorted(d.items()): #iterate through dict. (d) 
        w.writerow([key,values]) #write the required rows into csv 
