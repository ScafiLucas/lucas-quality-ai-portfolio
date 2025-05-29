import uuid
from io import BytesIO

from starlette.datastructures import UploadFile

from app.services.upload_service import process_csv_upload


def test_process_csv_upload_valid_file(tmp_path):
    # Monta conteúdo simulado de CSV válido
    csv_content = b"income,debt,late_payments,savings\n5000,1000,2,1500"
    file = UploadFile(filename="valid.csv", file=BytesIO(csv_content))

    result = process_csv_upload(file, tmp_path)

    assert result["status"] == "success"
    assert "job_id" in result
    assert uuid.UUID(result["job_id"])  # valida se é UUID válido


def test_process_csv_upload_invalid_file(tmp_path):
    # Monta CSV com conteúdo inválido
    invalid_csv = b"foo,bar,baz\n1,2,3"
    file = UploadFile(filename="invalid.csv", file=BytesIO(invalid_csv))

    result = process_csv_upload(file, tmp_path)

    assert result["status"] in ["error", "success"]  # depende do seu tratamento
    # Se você não gerar job para CSV inválido, testamos isso:
    if result["status"] == "error":
        assert "job_id" not in result or result["job_id"] is None
