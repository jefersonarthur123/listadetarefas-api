def test_listar_tarefas_vazio(client):
    response = client.get("/api/tarefas")
    assert response.status_code == 200
    assert response.json() == []

def test_criar_tarefa(client):
    payload = {"descricao": "Estudar FastAPI", "concluida": False}
    response = client.post("/api/tarefas", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["descricao"] == "Estudar FastAPI"
    assert data["concluida"] is False

def test_buscar_tarefa_por_id(client):
    create_resp = client.post("/api/tarefas", json={"descricao": "Comprar pão", "concluida": False})
    tarefa_id = create_resp.json()["id"]

    response = client.get(f"/api/tarefas/{tarefa_id}")
    assert response.status_code == 200
    assert response.json()["descricao"] == "Comprar pão"

    response_404 = client.get("/api/tarefas/999")
    assert response_404.status_code == 404

def test_atualizar_tarefa(client):
    create_resp = client.post("/api/tarefas", json={"descricao": "Lavar o carro", "concluida": False})
    tarefa_id = create_resp.json()["id"]

    update_resp = client.put(f"/api/tarefas/{tarefa_id}", json={"descricao": "Lavar o carro e aspirar", "concluida": True})
    assert update_resp.status_code == 200
    assert update_resp.json()["descricao"] == "Lavar o carro e aspirar"
    assert update_resp.json()["concluida"] is True

def test_deletar_tarefa(client):
    create_resp = client.post("/api/tarefas", json={"descricao": "Tarefa temporária", "concluida": False})
    tarefa_id = create_resp.json()["id"]

    delete_resp = client.delete(f"/api/tarefas/{tarefa_id}")
    assert delete_resp.status_code == 204

    get_resp = client.get(f"/api/tarefas/{tarefa_id}")
    assert get_resp.status_code == 404