import sender_stand_request
import get_user_body

def positive_assert(first_name):

    user_body = get_user_body.get_body(first_name) 
    # {

    #     "firstName": "Aa",

    #     "phone": "+11234567890",

    #     "address": "123 Elm Street, Hilltop"

    # }

    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # si el campo authToken no esta vacío

    users_table_response = sender_stand_request.get_users_table()
   
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    
    # print("Status code:")

    # print(user_response.status_code)
    
    # print("String que buscamos:")

    # print(str_user)
    
    # print("\nRespuesta del servidor:")
    
    # print(users_table_response.text)
    
    # print(f"\nVeces que aparece: {users_table_response.text.count(str_user)}")
    
    assert users_table_response.text.count(str_user) == 1 # si first_name aparece por lo menos 1 vez 