import data

def get_body(first_name):

    current_body = data.user_body.copy()
    # {

    #     "firstName": "Andrea",

    #     "phone": "+11234567890",

    #     "address": "123 Elm Street, Hilltop"

    # }

    current_body["firstName"] = first_name # Aa

    return current_body

    # Salida: 

    # {

    #     "firstName": "Aa",

    #     "phone": "+11234567890",

    #     "address": "123 Elm Street, Hilltop"

    # }
    