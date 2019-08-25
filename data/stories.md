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

## Generated Story 7173733492420794842
* book_ticket
    - action_book_ticket
    - form{"name": "action_book_ticket"}
    - slot{"requested_slot": "PERSON"}
* form: know_user{"PERSON": "Mayank"}
    - slot{"PERSON": "Mayank"}
    - form: action_book_ticket
    - slot{"PERSON": "Mayank"}
    - slot{"requested_slot": "DESTINATION"}
* form: book_ticket{"DESTINATION": "Bhopal"}
    - slot{"DESTINATION": "Bhopal"}
    - form: action_book_ticket
    - slot{"DESTINATION": "Bhopal"}
    - slot{"requested_slot": "ORIGIN"}
* form: book_ticket{"ORIGIN": "Indore"}
    - slot{"ORIGIN": "Indore"}
    - form: action_book_ticket
    - slot{"ORIGIN": "Indore"}
    - form{"name": null}
    - slot{"requested_slot": null}
