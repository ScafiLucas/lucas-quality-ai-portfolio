# 📘 User Story — Upload e Cálculo de Score via CSV

Como uma empresa parceira de concessão de crédito,
Quero poder enviar um arquivo CSV contendo informações de clientes,
Para que o sistema possa processar os dados, calcular o score de crédito usando IA e me retornar o resultado de forma confiável.

---

## 🧩 Contexto

A empresa atua concedendo crédito para pequenos empreendedores. Parceiros e correspondentes bancários frequentemente usam planilhas (.csv) para consolidar dados de clientes interessados. Essa planilha deve ser enviada para uma API segura que realiza:

- Validação e parsing do conteúdo
- Armazenamento em nuvem (simulado com S3/local)
- Enfileiramento do processo
- Cálculo de score por IA com base no histórico e nos dados do CSV
- Retorno do resultado de forma assíncrona

---

### ✅ Critérios de Aceitação

- [ ] A API deve aceitar um arquivo `.csv` via `POST /upload-csv`
- [ ] O CSV deve conter colunas obrigatórias (`nome`, `documento`, `renda`, etc.)
- [ ] O arquivo deve ser salvo de forma organizada
- [ ] O processamento deve acontecer de forma assíncrona
- [ ] A IA deve calcular um score com base nos dados
- [ ] Deve ser possível consultar o status e o resultado por um endpoint específico (`/credit-score/{id}`)
- [ ] Toda falha deve ser tratada com mensagens claras e HTTP apropriado

---

### 🎯 Valor de Negócio

- Acelera o processo de análise de crédito com suporte de IA
- Integra facilmente com sistemas legados que exportam dados em CSV
- Escalável para múltiplos parceiros e grandes volumes de dados
- Garante rastreabilidade e histórico dos cálculos realizados

---
