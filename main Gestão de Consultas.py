import datetime

class SistemaHospitalar:
    def __init__(self):
        self.utilizadores = {}
        self.pacientes = []
        self.consultas = []
        self.utilizador_atual = None

    def registar_utilizador(self):
        print("\n--- Registo de Utilizador ---")
        email = input("Email: ")
        if email in self.utilizadores:
            print("Erro: Este email já está registado.")
            return
        password = input("Password: ")
        self.utilizadores[email] = password
        print("Registo efetuado com sucesso!")

    def login(self):
        print("\n--- Login ---")
        email = input("Email: ")
        password = input("Password: ")
        if email in self.utilizadores and self.utilizadores[email] == password:
            self.utilizador_atual = email
            print("Login efetuado com sucesso.")
        else:
            print("Email ou password incorretos.")

    def registar_paciente(self):
        print("\n--- Registar Paciente ---")
        nome = input("Nome do paciente: ")
        idade = input("Idade: ")
        nif = input("NIF: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        paciente = {
            "nome": nome,
            "idade": idade,
            "nif": nif,
            "telefone": telefone,
            "email": email
        }
        self.pacientes.append(paciente)
        print("Paciente registado com sucesso!")

    def editar_paciente(self):
        print("\n--- Editar Paciente ---")
        nif = input("Indique o NIF do paciente: ")
        for paciente in self.pacientes:
            if paciente["nif"] == nif:
                print("Paciente encontrado.")
                paciente["nome"] = input(f"Novo nome ({paciente['nome']}): ") or paciente["nome"]
                paciente["idade"] = input(f"Nova idade ({paciente['idade']}): ") or paciente["idade"]
                paciente["telefone"] = input(f"Novo telefone ({paciente['telefone']}): ") or paciente["telefone"]
                paciente["email"] = input(f"Novo email ({paciente['email']}): ") or paciente["email"]
                print("Dados atualizados.")
                return
        print("Paciente não encontrado.")

    def listar_pacientes(self):
        print("\n--- Lista de Pacientes ---")
        if not self.pacientes:
            print("Nenhum paciente registado.")
            return
        for i, paciente in enumerate(self.pacientes):
            print(f"{i+1}. {paciente['nome']} | NIF: {paciente['nif']} | Idade: {paciente['idade']} | Telefone: {paciente['telefone']} | Email: {paciente['email']}")

    def agendar_consulta(self):
        print("\n--- Agendar Consulta ---")
        nif = input("NIF do paciente: ")
        paciente = next((p for p in self.pacientes if p["nif"] == nif), None)
        if not paciente:
            print("Paciente não encontrado.")
            return
        data_str = input("Data da consulta (DD/MM/AAAA): ")
        try:
            data = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()
        except ValueError:
            print("Formato de data inválido.")
            return
        especialidade = input("Especialidade: ")
        medico = input("Médico responsável: ")
        custo = input("Custo (€): ")

        consulta = {
            "paciente": paciente,
            "data": data,
            "especialidade": especialidade,
            "medico": medico,
            "custo": custo
        }
        self.consultas.append(consulta)
        print("Consulta agendada com sucesso.")

    def ver_consultas(self):
        print("\n--- Consultas Marcadas ---")
        if not self.consultas:
            print("Nenhuma consulta marcada.")
            return
        for i, consulta in enumerate(self.consultas):
            p = consulta["paciente"]
            print(f"{i+1}. {p['nome']} - {consulta['data'].strftime('%d/%m/%Y')} - {consulta['especialidade']} - Dr(a). {consulta['medico']} - {consulta['custo']}€")

    def menu(self):
        while True:
            print("\n--- Menu Principal ---")
            print("1 - Registar Utilizador")
            print("2 - Login")
            print("3 - Registar Paciente")
            print("4 - Editar Paciente")
            print("5 - Listar Pacientes")
            print("6 - Agendar Consulta")
            print("7 - Ver Consultas")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.registar_utilizador()
            elif opcao == "2":
                self.login()
            elif opcao == "3":
                if self.utilizador_atual:
                    self.registar_paciente()
                else:
                    print("É necessário efetuar login primeiro.")
            elif opcao == "4":
                if self.utilizador_atual:
                    self.editar_paciente()
                else:
                    print("É necessário efetuar login primeiro.")
            elif opcao == "5":
                if self.utilizador_atual:
                    self.listar_pacientes()
                else:
                    print("É necessário efetuar login primeiro.")
            elif opcao == "6":
                if self.utilizador_atual:
                    self.agendar_consulta()
                else:
                    print("É necessário efetuar login primeiro.")
            elif opcao == "7":
                if self.utilizador_atual:
                    self.ver_consultas()
                else:
                    print("É necessário efetuar login primeiro.")
            elif opcao == "0":
                print("A encerrar o sistema.")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    app = SistemaHospitalar()
    app.menu()
