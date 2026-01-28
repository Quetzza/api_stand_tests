import sender_stand_request
import get_user_body

def negative_assert_symbol(first_name):

    user_body = get_user_body.get_body(first_name)

    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400

    assert response.json()["code"] == 400

    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."

    # print("Status code:")

    # print(response.json()["code"])
    
    # print("\nRespuesta del servidor:")
    
    # print(response.text)

def negative_assert_no_firstname(user_body):

    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400

    assert response.json()["code"] == 400

    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

def negative_assert_type(arg):

    user_body = get_user_body.get_body(arg)

    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400

    assert response.json()["code"] == 400