import requests #requests should be installed-> pip install requests in cmd

BASE_URL = "https://fakestoreapi.com"


# ---------- Step 1: Login and Get Token ----------
def login():
    credentials = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=credentials)

    if response.status_code == 200:
        token = response.json().get("token")
        print("Logged in successfully. Token obtained.")
        return token
    else:
        print("Login failed:", response.status_code, response.text)
        return None


# ---------- Step 2: Authenticated GET Request ----------
def get_user(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/users/1", headers=headers)
    print("\nGET /users/1:", response.status_code)
    print(response.json())


# ---------- Step 3: POST - Create a Product ----------
def post_product():
    product_data = {
        "title": "New Product",
        "price": 29.99,
        "description": "Test product created via API",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }
    response = requests.post(f"{BASE_URL}/products", json=product_data)
    print("\nPOST /products:", response.status_code)
    print(response.json())


# ---------- Step 4: PUT - Update a Product (full update) ----------
def put_product():
    updated_data = {
        "title": "Updated Product Title",
        "price": 49.99,
        "description": "Updated full details",
        "image": "https://i.pravatar.cc",
        "category": "books"
    }
    response = requests.put(f"{BASE_URL}/products/7", json=updated_data)
    print("\nPUT /products/7:", response.status_code)
    print(response.json())


# ---------- Step 5: PATCH - Update Product Partially ----------
def patch_product():
    patch_data = {
        "price": 99.99
    }
    response = requests.patch(f"{BASE_URL}/products/7", json=patch_data)
    print("\nPATCH /products/7:", response.status_code)
    print(response.json())


# ---------- Step 6: DELETE - Delete Product ----------
def delete_product():
    response = requests.delete(f"{BASE_URL}/products/7")
    print("\nDELETE /products/7:", response.status_code)
    print(response.json())


# ---------- Main ----------
#Only run the code inside this block if the script is being run directly, and not when it's imported as a module in another file.
if __name__ == "__main__":
    token = login()
    if token:
        get_user(token)
    post_product()
    put_product()
    patch_product()
    delete_product()
