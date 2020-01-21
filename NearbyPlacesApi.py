import requests, json 
def GetLocality(lat,longt):
    api_key = 'AIzaSyB7FlbcBr_7xxe5N_qbJWZNddv0xEOPfQY'
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    Latitude=lat
    Longitude=longt
    types="Hotel"
    location=str(Latitude)+","+str(Longitude)
    keyword="Hotel"
    r = requests.get(url + 'location=' + location +"&radius="+"1000"+"&type="+types+"&keyword="+keyword+
                            '&key=' + api_key) 
    
    x = r.json() 
    y = x['results'] 
    if(len(y)!=0):
        # for i in range(len( y)):
        #     print(y[i]['name'])
        return y
    else:
        return(0)
        # for i in range(len( y)):
        #     print(y[i]['name'])

# GetLocality()