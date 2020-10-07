def test_request_list_success(client):
    resp = client.get('/api/v1/request')
    assert resp.status_code == 200


def test_request_retrieve_success(client):
    resp = client.get(f'/api/v1/request/{1}')
    assert resp.status_code == 200


def test_request_create_success(client):
    resp = client.post(f'/api/v1/request')
    assert resp.status_code == 200


def test_request_destroy_success(client):
    resp = client.delete(f'/api/v1/request/{1}')
    assert resp.status_code == 200
