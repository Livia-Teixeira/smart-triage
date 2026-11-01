from paciente import Paciente, PacientePreferencial
from triagem import Triagem
from banco import criar_tabelas

triagem = Triagem()


triagem.adicionar(Paciente('Carlos', 30, 'dor de garganta'), 3)
triagem.adicionar(PacientePreferencial('Ana', 68, 'dor no peito', 'idoso'), 1)
triagem.adicionar(Paciente('Rita', 25, 'febre alta'), 2)


while triagem.quantidade() != 0:
    print("Bem vindo a Smart Triage! Selecione a opção desejada:")
    print("1. Adicionar novo paciente. \n2. Ver fila atual. \n3. Chamar próximo da fila. \n4. Historico de atendimento")
    try:
        opcao = int(input("Opção selecionado: "))
    except Exception:
        raise ValueError("Opção inválida. Tente novamente.")

    match opcao:
        case 1:
            print("Tipo de atendimento: \n1. Atendimento Regular\n2. Atendimento Prioritario")
            tipo_opcao = int(input("Tipo de atendimento selecionado: "))
            if tipo_opcao == 1:
                triagem.adicionar(Paciente(str(input("Nome: ")), int(input("Idade: ")), str(input("Sintoma: "))), int(input("Nivel da prioridade: ")))
            elif tipo_opcao == 2:
                triagem.adicionar(PacientePreferencial(str(input("Nome: ")), int(input("Idade: ")), str(input("Sintoma: ")), str(input("Motivo: "))),1)
            else:
                break
        case 2:
            a = triagem.mostrar()
            print(a)
        case 3:
            ...
        case 4:
            ...
        case _:
            break





"""while triagem.quantidade() > 0:
    proximo = triagem.chamarProximo()
    proximo.mostrar()

criar_tabelas()
print("banco feito")"""