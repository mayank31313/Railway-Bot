# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#

from rasa_sdk import Action, Tracker
from rasa_sdk.forms  import FormAction
from rasa_sdk.executor import CollectingDispatcher
import json

class ListTrains(FormAction):
    trains = {
        "arrivals":[{
            "train":{
                    "number":"04921","name":"SRE-UMB MEMU SPECIAL","start_time":"04:45","type":"HSP"
                },
                "source":{"code":"SRE","name":"SAHARANPUR"},
                "dest":{"code":"UMB","name":"AMBALA CANT JN"}
            },{
            "train":{
                    "number":"04922","name":"UMB-SRE MEMU SPECIAL","start_time":"20:45","type":"HSP"
                },
                "source":{"code":"UMB","name":"AMBALA CANT JN"},
                "dest":{"code":"SRE","name":"SAHARANPUR"}
            }
        ]
    }

    def name(self):
        return "action_list_trains"

    @staticmethod
    def required_slots(tracker):
        return ["DESTINATION","ORIGIN"]

    def submit(self, dispatcher, tracker, domain):
        origin = tracker.get_slot("ORIGIN")
        destination = tracker.get_slot("DESTINATION")

        dispatcher.utter_message("Ok, we have found some trains for your journey from %s to %s"%(origin,destination));
        train_arrivals = self.trains["arrivals"]

        for trains in train_arrivals:
            dispatcher.utter_message(json.dumps(trains))
        return []


class BookTicket(FormAction):
    def name(self):
        return "action_book_ticket"

    @staticmethod
    def required_slots(tracker):
        train_number = tracker.get_slot("TRAIN_NUMBER")
        if train_number is None:
            return ["DESTINATION","ORIGIN"]
        else
            return ["TRAIN_NUMBER"]

    def submit(self, dispatcher, tracker, domain):
        train_number = tracker.get_slot('TRAIN_NUMBER')
        if train_number is None:
            origin = tracker.get_slot("ORIGIN")
            destination = tracker.get_slot("DESTINATION")

            dispatcher.utter_message("You want to book a ticket from %s to %s" % (origin,destination))
        else:
            dispatcher.utter_message("You want to book train %s"%train_number)
        return []