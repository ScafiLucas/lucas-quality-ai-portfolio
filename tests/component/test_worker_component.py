import asyncio
import csv
import uuid

import pytest

from app.core.job_queue import job_queue
from app.core.job_tracker import job_status_map, JobStatus
from app.models.output.score_output import ScoreOutput
from app.services.worker import worker_loop

# Marca o teste como assíncrono para pytest
@pytest.mark.asyncio
async def test_worker_processes_valid_csv(tmp_path):
    # Arrange (Preparação)
    # Gera um ID único para o job
    job_id = str(uuid.uuid4())
    # Define o status inicial do job como PENDENTE
    job_status_map[job_id] = JobStatus.PENDING

    # Cria um arquivo CSV temporário com dados de teste
    test_csv_path = tmp_path / "test.csv"
    with open(test_csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["income", "debt", "late_payments", "savings"])
        writer.writeheader()
        writer.writerow({
            "income": 5000,
            "debt": 1000,
            "late_payments": 2,
            "savings": 1500
        })

    # Adiciona o job na fila de processamento, informando o caminho do arquivo CSV
    await job_queue.put({
        "job_id": job_id,
        "filepath": str(test_csv_path)
    })

    # Act (Ação)
    # Executa o loop do worker para processar o job, com timeout de 2 segundos
    try:
        await asyncio.wait_for(worker_loop(), timeout=2)
    except asyncio.TimeoutError:
        # Ignora o erro de timeout, pois o worker pode rodar indefinidamente
        pass

    # Assert (Verificação)
    # Verifica se o status do job foi atualizado para "done" (concluído)
    assert job_status_map[job_id]["status"] == "done"
    # Recupera os resultados do job
    results = job_status_map[job_id]["results"]
    # Verifica se os resultados são uma lista e contém um item
    assert isinstance(results, list)
    assert len(results) == 1

    # Verifica se o resultado é uma instância de ScoreOutput
    score_result = results[0]
    assert isinstance(score_result, ScoreOutput)
    # Verifica se o score está dentro do intervalo esperado
    assert 1 <= score_result.score <= 1000
    # Verifica se a categoria está entre as opções válidas
    assert score_result.category in {"Poor", "Fair", "Good", "Very Good", "Excellent"}
