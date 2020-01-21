from  geopy.geocoders import Nominatim
geolocator = Nominatim()
city ="Marathahalli"
country ="INDIA"
loc = geolocator.geocode(city+','+ country)
print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)