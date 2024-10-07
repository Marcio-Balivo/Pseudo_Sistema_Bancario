# Pseudo Sistema Bancário
## Objetivo:
Criar um sistema que simule as funções de sacar, depositar e emitir extrato.

### Requisitos da função "sacar":
- 0 < valor <= 500
- Transações <= 10
- saldo >= valor
- Se a transação ocorrer, registrá-la no extrato.

### Requisitos da função "depositar:
- valor > 0
- Se a transação ocorrer, registrá-la no extrato.

### Requisitos da função "emitir extrato":
- Se extrato = "" então exibir "Nenhuma transação foi registrada!" senão exibir as transações registradas seguidas pelo saldo atualizado.
