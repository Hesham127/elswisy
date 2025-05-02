from auth import Auth

def test_signup():
    auth = Auth()
    user_data = {
        'user_name': 'hamada__',
        'password_': '123456789',
        'email': 'hamada@gmail.com',
        'user_phone': 1234567890,
        'addr_city': 'Cairo',
        'addr_street': '123 Test Street',
        'addr_bn': 1
    }
    print("\nTesting Sign Up:")
    success, message = auth.signup(**user_data)
    print(f"Signup Result: {message}")

def test_login():
    auth = Auth()
    print("\nTesting Correct Login:")
    success, message = auth.login('hamada__', '123456789')
    print(f"Login Result: {message}")

    print("\nTesting Wrong Password:")
    success, message = auth.login('hamada__', 'wrongpass')
    print(f"Login Result: {message}")

    print("\nTesting Non-existent User:")
    success, message = auth.login('not_a_user', 'password')
    print(f"Login Result: {message}")

if __name__ == "__main__":
    print("Starting Authentication Tests...")
    test_signup()
    test_login()
    print("\nAll tests completed!") 