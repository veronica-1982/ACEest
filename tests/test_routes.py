def test_home_page(client):
    res = client.get("/")
    assert res.status_code == 200


def test_program_api_valid(client):
    res = client.post("/program", json={
        "program": "Fat Loss (FL)",
        "weight": 70
    })

    assert res.status_code == 200
    data = res.get_json()

    assert "workout" in data
    assert "diet" in data
    assert "calories" in data
    assert data["calories"] == 1400   


def test_program_api_invalid(client):
    res = client.post("/program", json={
        "program": "INVALID",
        "weight": 70
    })

    assert res.status_code == 400


def test_save_client_create(client):
    res = client.post("/save_client", data={
        "name": "Test User",
        "age": 25,
        "height": 170,
        "weight": 70,
        "program": "Fat Loss (FL)"
    })

    assert res.status_code == 200
    data = res.get_json()

    assert data["status"] == "success"


def test_save_client_update(client):

    client.post("/save_client", data={
        "name": "Test User",
        "age": 25,
        "height": 170,
        "weight": 70,
        "program": "Fat Loss (FL)"
    })

    
    res = client.post("/save_client", data={
        "name": "Test User",
        "age": 30,
        "height": 175,
        "weight": 80,
        "program": "Muscle Gain (MG)"
    })

    assert res.status_code == 200


def test_bmi_api(client):
  
    client.post("/save_client", data={
        "name": "BMI User",
        "age": 25,
        "height": 170,
        "weight": 70,
        "program": "Fat Loss (FL)"
    })

    res = client.get("/bmi/BMI User")

    assert res.status_code == 200
    data = res.get_json()

    assert "bmi" in data
    assert "category" in data
    assert "risk" in data


def test_bmi_missing_user(client):
    res = client.get("/bmi/UnknownUser")

    assert res.status_code == 404