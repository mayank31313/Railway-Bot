## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  
## Generated Story 8425276876080047331
* inform
    - action_list_trains
    - form{"name": "action_list_trains"}
    - slot{"requested_slot": "DESTINATION"}
* form: inform{"DESTINATION": "Jammu"}
    - slot{"DESTINATION": "Jammu"}
    - form: action_list_trains
    - slot{"DESTINATION": "Jammu"}
    - slot{"requested_slot": "ORIGIN"}
* form: inform{"ORIGIN": "Indore"}
    - slot{"ORIGIN": "Indore"}
    - form: action_list_trains
    - slot{"ORIGIN": "Indore"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -5173163635916392540
* know_user{"PERSON": "Mayank"}
    - slot{"PERSON": "Mayank"}
    - utter_greet_user
* inform
    - action_list_trains
    - form{"name": "action_list_trains"}
    - slot{"requested_slot": "DESTINATION"}
* form: inform{"ORIGIN": "Indore", "DESTINATION": "Odisha"}
    - slot{"DESTINATION": "Odisha"}
    - slot{"ORIGIN": "Indore"}
    - form: action_list_trains
    - slot{"ORIGIN": "Indore"}
    - slot{"DESTINATION": "Odisha"}
    - form{"name": null}
    - slot{"requested_slot": null}
