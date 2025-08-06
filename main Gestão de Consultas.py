import csv
import os
from datetime import datetime

class SistemaHospitalar:
    def __init__(self):
        self.utilizador_logado = None
        self.ficheiro_utilizadores = "utilizadores.csv"
        self.ficheiro_pacientes = "pacientes.csv"
        self._criar_ficheiros_se_nao_existirem()

    def _criar_ficheiros_se_nao_existirem(self):
        for ficheiro, cabecalho in [
            (self.ficheiro_utilizadores, ["email", "password"]),
            (self.ficheiro_pacientes, ["nome", "nif", "data_nascimento", "telefone"])
        ]:
            if not os.path.exists(ficheiro):
                with open(ficheiro, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(cabecalho)

    def registar_utilizador(self):
        email = input("Introduza o seu email: ").strip()
        password = input("Introduza a sua password: ").strip()

        if self._utilizador_existe(email):
            print("Email já registado!")
            return

        with open(self.ficheiro_utilizadores, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([email, password])

        print(f"Registo efetuado com sucesso! Um email de verificação foi enviado para {email} (simulado).")

    def _utilizador_existe(self, email):
        with open(self.ficheiro_utilizadores, 'r') as f:
            reader = csv.DictReader(f)
            return any(row['email'] == email for row in reader)

    def login(self):
        email = input("Email: ").strip()
        password = input("Password: ").strip()

        with open(self.ficheiro_utilizadores, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['email'] == email and row['password'] == password:
                    self.utilizador_logado = email
                    print(f" Login bem-sucedido! Bem-vindo, {email}")
                    return
        print(" Email ou password incorretos!")

    def registar_paciente(self):
        if not self.utilizador_logado:
            print(" Tem de estar autenticado para registar pacientes.")
            return

        nome = input("Nome do paciente: ").strip()
        nif = input("NIF: ").strip()
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        telefone = input("Telefone: ").strip()

        with open(self.ficheiro_pacientes, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([nome, nif, data_nascimento, telefone])

        print(" Paciente registado com sucesso!")

    def listar_pacientes(self):
        if not self.utilizador_logado:
            print(" Tem de estar autenticado para consultar pacientes.")
            return

        print("\n Lista de Pacientes:")
        with open(self.ficheiro_pacientes, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"- {row['nome']} | NIF: {row['nif']} | Nasc: {row['data_nascimento']} | Tel: {row['telefone']}")
        print()