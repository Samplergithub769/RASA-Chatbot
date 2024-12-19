# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher


class ActionSayData(Action):

    def name(self) -> Text:
        return "action_say_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot("name")
        city = tracker.get_slot("city")
        phone = tracker.get_slot("phone")
        
        
        dispatcher.utter_message(text=f"Hey {name}, {city} is a very beautiful place. your phone number is {phone} :)")

        return []

class ValidateSimpleForm(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_simple_form"
    
    def validate_phone(self, slot_value: Any, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict [Text, Any]]:
        
        phone = tracker.get_slot("phone")
        
        if (int(len(phone))>10):
            dispatcher.utter_message(text="Invalid phone number")
            return{"phone":None}
        if(int(len(phone))<10):
            dispatcher.utter_message(text="Invalid phone number")
            return{"phone":None}
        else:
            return{"phone":phone}


