import random
import time

def criando_processos():
    print('Criando processos\n')
    processos = [] 
    for i in range(1,10):
        tempo_chegada = random.randint(0, 10)
        tempo_saida = random.randint(1, 10)
        processos.append({"PID": i, "Chegada": tempo_chegada, "Saida": tempo_saida})
    return processos 
       
# Função FCFS de processos
def FCFS():
    print("\n === FCFS: First Come, First Served ===")
    gerar = criando_processos()
    gerar.sort(key=lambda x: x['Chegada'])  # Ordena pelo tempo de chegada
    tempo_atual = 0 

    print('\nTAT = O Turnaround Time (TAT) é o tempo total desde a chegada até a finalização do processo.\n')
    print('Tempo de espera = O tempo de espera é o tempo que um processo aguarda na fila antes de ser executado.\n')
    
    print("\n" + "-" * 75)
    print(f"{'PID':<8}{'Chegada':<12}{'Execução':<12}{'Inicio':<12}{'Termino':<12}{'Espera':<12}{'TAT':<12}")
    print("-" * 75)   
    
    for p in gerar:
        if tempo_atual < p['Chegada']:
            tempo_atual = p['Chegada']  # Garante que o processo inicie no tempo correto
        
        tempo_inicio = tempo_atual
        tempo_espera = tempo_atual - p['Chegada']
        tempo_termino = tempo_atual + p["Saida"]
        turnaround_time = tempo_termino - p["Chegada"]

        print(f"{p['PID']:<8}{p['Chegada']:<12}{p['Saida']:<12}{tempo_inicio:<12}{tempo_termino:<12}{tempo_espera:<12}{turnaround_time:<12}")
        
        time.sleep(p["Saida"]) 
        tempo_atual += p["Saida"] 
        
        print(f"Processo {p['PID']} finalizado.")
    print("\nTodos os processos foram finalizados !!\n")

# Função Round Robin de processos
def round_robin():
    print("\n=== Round Robin ===")
    gerar1 = criando_processos()
    quantum = 3
    fila = sorted(gerar1, key=lambda x: x['Chegada']) 
    print("PID\tTempo de Chegada\tTempo de Execução")
    print("-" * 50)

    for p in fila:
        print(f"{p['PID']}\t{p['Chegada']}\t\t\t{p['Saida']}")

    print("\nProcessos estão sendo executados com o quantum = ", quantum)
    print("-" * 50)

    while fila:
        processo = fila.pop(0)
        if processo["Saida"] > quantum:
            print(f"\n[Processo {processo['PID']}] executado por {quantum} segundos.")
            time.sleep(quantum)
            processo["Saida"] -= quantum
            print(f"[Processo {processo['PID']}] não finalizado, restando {processo['Saida']} segundos.")
            fila.append(processo)
        else:
            print(f"\n[Processo {processo['PID']}] executado por {processo['Saida']} segundos.")
            time.sleep(processo["Saida"])
            print(f"[Processo {processo['PID']}] Finalizado ✅")
    print("\n=== Todos os processos foram finalizados! ===\n")


if __name__ == '__main__': 

    while True:
        print('\n1 - FCFS: First Come, First Served')
        print('2 - RR: Round Robin')
        print('3- Sair')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            FCFS()
        elif opcao == 2:
            round_robin()
        elif opcao == 3:
            exit(False)
        else: 
            print('Opção inválida')
            continue