def editar_dados(id, tarefa):
    requests.put(f"https://api.pontomais.com.br/external_api/v1/employees/{{employee_id}}/user
{id}",
                 data=json.dumps(tarefa.__dict__))
