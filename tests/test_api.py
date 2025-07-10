import pytest
import json
from app.api import app

@pytest.fixture
def client():
    """Fixture for Flask test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calcular_precio_endpoint_sales10(client):
    """Test the POST /precio endpoint with SALES10 coupon"""
    data = {
        "price": 100,
        "coupon": "SALES10",
        "tax_rate": 0.19
    }
    response = client.post('/precio', 
                          data=json.dumps(data),
                          content_type='application/json')
    
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["final_price"] == 107.1

def test_calcular_precio_endpoint_super20(client):
    """Test the POST /precio endpoint with SUPER20 coupon"""
    data = {
        "price": 200,
        "coupon": "SUPER20",
        "tax_rate": 0.19
    }
    response = client.post('/precio',
                          data=json.dumps(data),
                          content_type='application/json')
    
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["final_price"] == 190.4  # 200 * 0.8 * 1.19

def test_calcular_precio_endpoint_welcome(client):
    """Test the POST /precio endpoint with WELCOME coupon"""
    data = {
        "price": 100,
        "coupon": "WELCOME",
        "tax_rate": 0.19
    }
    response = client.post('/precio',
                          data=json.dumps(data),
                          content_type='application/json')
    
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["final_price"] == 101.15  # 100 * 0.85 * 1.19

def test_precio_sin_cupon_valido(client):
    """Test price with invalid coupon"""
    data = {
        "price": 100,
        "coupon": "INVALID",
        "tax_rate": 0.19
    }
    response = client.post('/precio',
                          data=json.dumps(data), 
                          content_type='application/json')
    
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["final_price"] == 119.0  # 100 * 1.19

def test_precio_con_impuesto_personalizado(client):
    """Test with custom tax rate"""
    data = {
        "price": 100,
        "coupon": "SALES10",
        "tax_rate": 0.21  # 21% instead of default 19%
    }
    response = client.post('/precio',
                          data=json.dumps(data),
                          content_type='application/json')
    
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["final_price"] == 108.9  # 100 * 0.9 * 1.21

def test_precio_sin_impuesto_especificado(client):
    """Test that uses default tax rate (19%)"""
    data = {
        "price": 100,
        "coupon": "SALES10"
        # No tax specified, should use 0.19 default
    }
    response = client.post('/precio',
                          data=json.dumps(data),
                          content_type='application/json')
    
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["final_price"] == 107.1

def test_precio_cero(client):
    """Test with zero price"""
    data = {
        "price": 0,
        "coupon": "SALES10",
        "tax_rate": 0.19
    }
    response = client.post('/precio',
                          data=json.dumps(data),
                          content_type='application/json')
    
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["final_price"] == 0.0