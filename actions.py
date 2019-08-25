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

class ListTrains(FormAction):
    def name(self):
        return "action_list_trains"

    @staticmethod
    def required_slots(tracker):
        return ["DESTINATION","ORIGIN"]

    def submit(self, dispatcher, tracker, domain):
        return []


class BookTicket(FormAction):
    def name(self):
        return "action_book_ticket"

    @staticmethod
    def required_slots(tracker):
        return ["PERSON","DESTINATION","ORIGIN"]

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message("%s %s %s"%(tracker.get_slot("PERSON"),tracker.get_slot("DESTINATION"),tracker.get_slot("ORIGIN")))
        return []