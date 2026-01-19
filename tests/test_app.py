from app import app

def test_root():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"Hello World from AWS Elastic Beanstalk!"

