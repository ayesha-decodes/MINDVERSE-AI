from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'

def test_games_configuration():
    response = client.get('/api/games')
    assert response.status_code == 200
    assert len(response.json()['games']) == 5

def test_valid_summary_not_persisted():
    response = client.post('/api/sessions/summary', json={'games':[{'game_id':'reaction','score':80,'valid_trials':8,'detail':'520 ms median'}]})
    assert response.status_code == 202
    assert response.json()['persisted'] is False

def test_invalid_score_rejected():
    response = client.post('/api/results/validate', json={'games':[{'game_id':'reaction','score':120,'valid_trials':8}]})
    assert response.status_code == 422

def test_unknown_game_rejected():
    response = client.post('/api/results/validate', json={'games':[{'game_id':'mind_reading','score':50,'valid_trials':2}]})
    assert response.status_code == 422

def test_duplicate_games_rejected():
    payload={'games':[{'game_id':'reaction','score':50,'valid_trials':1},{'game_id':'reaction','score':60,'valid_trials':2}]}
    assert client.post('/api/results/validate',json=payload).status_code == 422

def test_extra_fields_rejected():
    payload={'games':[{'game_id':'reaction','score':50,'valid_trials':1,'email':'person@example.com'}]}
    assert client.post('/api/results/validate',json=payload).status_code == 422
