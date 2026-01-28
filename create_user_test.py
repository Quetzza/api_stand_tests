import positive_test
import negative_test
import data
import get_user_body

""""
    Test 1
"""

def test_create_user_2_letter_in_first_name_get_success_response():
    
   positive_test.positive_assert("Aa")
    

""""
    Test 2
"""

def test_create_user_15_letter_in_first_name_get_success_response():
    
   positive_test.positive_assert("Aaaaaaaaaaaaaaa")


""""
    Test 3
"""

def test_create_user_1_letter_in_first_name_get_error_response():

    negative_test.negative_assert_symbol("A")

""""
    Test 4
"""

def test_create_user_16_letter_in_first_name_get_error_response():
    
    negative_test.negative_assert_symbol("Aaaaaaaaaaaaaaaa")

""""
    Test 5
"""

def test_create_user_english_letter_in_first_name_get_success_response():
    positive_test.positive_assert("QWErty")

""""
    Test 6
"""

def test_create_user_has_special_symbol_in_first_name_get_error_response():

    negative_test.negative_assert_symbol("\"№%@\",")

""""
    Test 7
"""

def test_create_user_has_number_in_first_name_get_error_response():

    negative_test.negative_assert_symbol("123")

""""
    Test 8
"""

def test_create_user_no_first_name_get_error_response():
    
    user_body = data.user_body.copy() # The information is obtained from the dictionary

    user_body.pop("firstName") # The key firstName is removed from the list

    negative_test.negative_assert_no_firstname(user_body)

""""
    Test 9
"""

def test_create_user_empty_first_name_get_error_response():
    
    user_body = get_user_body.get_body("") # The data is sent without the value of the firstName key

    negative_test.negative_assert_no_firstname(user_body)

""""
    Test 10
"""

def test_create_user_number_type_first_name_get_error_response():
   
    negative_test.negative_assert_type(12)