# Process Scheduling Simulation

Este repositório contém uma implementação em Python de algoritmos de escalonamento de processos: **First Come, First Served (FCFS)** e **Round Robin (RR)**.

## 📌 Algoritmos Implementados

1. **FCFS (First Come, First Served)**
   - Processos são atendidos na ordem em que chegam.
   - Nenhuma preempção ocorre.
   - O tempo de espera pode ser alto para processos que chegam tarde.

2. **Round Robin (RR)**
   - Usa um tempo fixo (quantum) para cada processo.
   - Se um processo não terminar dentro do quantum, ele volta para o final da fila.
   - Garante tempos de resposta mais rápidos para todos os processos.

## 🚀 Como Executar

### Pré-requisitos
- Python 3 instalado

### Passos
1. Clone o repositório:
   ```sh
   git clone https://github.com/mttue7/process_scheduling.git
   cd process_scheduling
   ```
2. Execute o script:
   ```sh
   python escalonar.py
   ```
3. Escolha um dos algoritmos no menu interativo.

## 📄 Exemplo de Saída

```sh
1 - FCFS: First Come, First Served
2 - RR: Round Robin
3 - Sair
Escolha uma opção: 1

 === FCFS: First Come, First Served ===
PID     Chegada     Execução    Início    Término    Espera    TAT
-----------------------------------------------------------------
1       2          5           2         7          0         5
2       3          8           7         15         4         12
...
```

## 🛠️ Contribuição
Fique à vontade para abrir issues e pull requests para melhorias!

## 📜 Licença
Este projeto está sob a licença MIT.
