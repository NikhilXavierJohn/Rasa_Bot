# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from geopy.geocoders import Nominatim
from NearbyPlacesApi import GetLocality
from pymongo import MongoClient
from tabulate import tabulate
client = MongoClient('localhost', 27017)
db = client['Hotels']
class ActionBookHotel(Action):

    def name(self) -> Text:
        return "action_book_hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hotel List!\n")
        locality=tracker.get_slot('location')
        geolocator = Nominatim()
        country ="INDIA"
        loc = geolocator.geocode(locality+','+ country)
        data=GetLocality(loc.latitude,loc.longitude)
        # print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
        j=0
        if(data!=0):
            for i in range(len(data)):
                j= j+1
                message=str(i)+"."+data[i]['name']
                dispatcher.utter_message(message)
        else:
            dispatcher.utter_message("No hotels Available")
        return []
class ActionGetHotel(Action):
    def name(self) -> Text:
        return "action_mongo_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hotel Details!\n")
        locality=tracker.get_slot('location')

        locality=str(locality).lower().capitalize()
        print(locality)
        print(type(locality))
        command="{'City':'"+locality+"'}"
        # print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
        
        data=db.data.find(eval(command))
        lists=[]
        if(data!=None):
            for x in data:
                j=list(x.items())
                lists.append([j[3][1],j[5][1],j[6][1],j[7][1],j[8][1],j[9][1],j[10][1]])
            dispatcher.utter_message(tabulate(lists,headers=["Hotel","City","state","Owner","Phone","Mobile","Email"],tablefmt='psql'))
        else:
            dispatcher.utter_message("No hotels Available")
        return []
