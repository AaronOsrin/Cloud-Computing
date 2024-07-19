import requests

base_url = 'http://localhost:5001/books'
book1 = {
    'title': 'Adventures of Huckleberry Finn',
    'ISBN': '9780520343641',
    'genre': 'Fiction'
}
book2 = {
    'title': 'Pride and Prejudice',
    'ISBN': '9780141199078',
    'genre': 'Romance'
}
invalid_book = {
    'title': '',
    'ISBN': '',
    'genre': ''
}

def test_create_books():
    response1 = requests.post(base_url, json=book1)
    print(f"Create book1 response: {response1.status_code}, {response1.json()}")
    assert response1.status_code == 201
    response2 = requests.post(base_url, json=book2)
    print(f"Create book2 response: {response2.status_code}, {response2.json()}")
    assert response2.status_code == 201

def test_get_book1():
    response = requests.get(f"{base_url}/isbn/{book1['ISBN']}")
    print(f"Get book1 response: {response.status_code}, {response.json()}")
    assert response.status_code == 200

def test_list_books():
    response = requests.get(base_url)
    print(f"List books response: {response.status_code}, {response.json()}")
    assert response.status_code == 200

def test_update_book():
    response = requests.get(f"{base_url}/isbn/{book1['ISBN']}")
    print(f"Get book1 for update response: {response.status_code}, {response.json()}")
    book_data = response.json()
    book_id = book_data.get('ID') or book_data.get('id')
    update_data = {
        'title': 'Adventures of Tom Sawyer'
    }
    response = requests.put(f"{base_url}/{book_id}", json=update_data)
    print(f"Update book response: {response.status_code}, {response.json()}")
    assert response.status_code == 200

def test_delete_book2():
    response = requests.get(f"{base_url}/isbn/{book2['ISBN']}")
    print(f"Get book2 for delete response: {response.status_code}, {response.json()}")
    book_data = response.json()
    book_id = book_data.get('ID') or book_data.get('id')
    response = requests.delete(f"{base_url}/{book_id}")
    print(f"Delete book2 response: {response.status_code}, {response.json()}")
    assert response.status_code == 200

def test_get_deleted_book2():
    response = requests.get(f"{base_url}/isbn/{book2['ISBN']}")
    print(f"Get deleted book2 response: {response.status_code}, {response.json()}")
    assert response.status_code == 404

def test_invalid_book():
    response = requests.post(base_url, json=invalid_book)
    print(f"Invalid book response: {response.status_code}, {response.json()}")
    assert response.status_code in [400, 500]
