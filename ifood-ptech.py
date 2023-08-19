# import csv
# import os

# def ler_transacoes():
#     """Função para ler as transações armazenadas no arquivo CSV."""
#     transacoes = []
#     if os.path.exists("transacoes.csv"):
#         with open("transacoes.csv", "r") as arquivo_csv:
#             leitor_csv = csv.reader(arquivo_csv)
#             for linha in leitor_csv:
#                 transacoes.append(linha)
#     return transacoes

# def salvar_transacao(tipo, valor):
#     """Função para salvar uma transação no arquivo CSV."""
#     with open("transacoes.csv", "a", newline="") as arquivo_csv:
#         escritor_csv = csv.writer(arquivo_csv)
#         escritor_csv.writerow([tipo, valor])

def depositar():
    """Operação de depósito."""
    valor = float(input("Digite o valor a ser depositado: R$ "))
    salvar_transacao("DEPÓSITO", valor)
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

def sacar():
    """Operação de saque."""
    valor = float(input("Digite o valor a ser sacado: R$ "))
    transacoes = ler_transacoes()
    saques_diarios = sum(1 for transacao in transacoes if transacao[0] == "SAQUE")
    saldo_atual = sum(float(transacao[1]) for transacao in transacoes if transacao[0] == "DEPÓSITO") - sum(float(transacao[1]) for transacao in transacoes if transacao[0] == "SAQUE")
    if saques_diarios >= 3:
        print("Limite diário de saques atingido (máximo de 3 saques por dia).")
    elif valor > 500.0:
        print("Valor de saque excede o limite diário de R$ 500,00.")
    elif valor > saldo_atual:
        print("Saldo insuficiente para realizar o saque.")
    else:
        salvar_transacao("SAQUE", valor)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def extrato():
    """Operação de extrato."""
    transacoes = ler_transacoes()
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        saldo_atual = sum(float(transacao[1]) for transacao in transacoes if transacao[0] == "DEPÓSITO") - sum(float(transacao[1]) for transacao in transacoes if transacao[0] == "SAQUE")
        print("Extrato:")
        for tipo, valor in transacoes:
            print(f"{tipo}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo_atual:.2f}")

def main():
    """Função principal que exibe o menu e gerencia as operações bancárias."""
    while True:
        menu = """
        Menu:
        (1) Depositar
        (2) Sacar
        (3) Extrato
        (4) Sair

        => """
        opcao = input(menu)
        if opcao == "1":
            depositar()
        elif opcao == "2":
            sacar()
        elif opcao == "3":
            extrato()
        elif opcao == "4":
            print("Obrigado por utilizar nossos serviços!")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()
