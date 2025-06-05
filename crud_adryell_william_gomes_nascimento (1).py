import json

def menup():
  print("""
      Página Inicial - Produtos

    1 - Cadastrar produto
    2 - Atualizar produto
    3 - Listar produto
    4 - Excluir produto
    0 - Sair

  """)

def cadp(produtos):
  id = input("Digite o indentificador do produto: ")
  qtd = int(input("Digite a quantidade do produto no estoque: "))
  preco = input("Digite o preço do produto: ")
  preco = preco.replace(",",".")
  preco = float(preco)
  prod_novo = {"id": id, "quantidade": qtd, "preco": preco}
  produtos.append(prod_novo)

def attp(produtos):
  if not produtos:
    print("Não existe nenhum produto cadastrado")
    return
  ind = input("Digite o id do produto que deseja atualizar: ")
  for produto in produtos:
    if produto["id"] == ind:
      ask = int(input("O que você quer atualizar? 0 = quantidade, 1 = preço: "))

      if ask == 0:
        produto["quantidade"] = int(input("Digite a nova quantidade do produto: "))
      elif ask == 1:
        preco = input("Digite o novo preço do produto: ")
        preco = preco.replace(",", ".")
        produto["preco"] = float(preco)
      else:
        print("Opção Inválida")

      print("Produto atualizado")
      return

  print("Produto não encontrado")

def lisp(produtos):
    if not produtos:
        print("Nenhum produto cadastrado")
        return

    print("\nLista de Produtos:")
    for produto in produtos:
        print(f"ID: {produto['id']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}")

def delp(produtos):
  if not produtos:
    print("Não existe nenhum produto cadastrado")
    return
  ind = input("Digite o id do produto que quer excluir: ")
  for produto in produtos:
    if produto["id"] == ind:
      ask = int(input("Tem certeza que quer apagar? 0 = sim, 1 = não: "))
      if ask == 0:
        produtos.remove(produto)
        print(f"Produto com id", {ind}, "removido")
        return
  print("Produto não encontrado")

def mainp():
  global produtos
  while True:
    menup()
    opcao = input("Digite uma opção: ")

    if opcao == "1":
      cadp(produtos)
    elif opcao == "2":
      attp(produtos)
    elif opcao == "3":
      lisp(produtos)
    elif opcao == "4":
      delp(produtos)
    elif opcao == "0":
      break
    else:
      print("Opção inválida")

"""mainp()"""

"""Cliente"""

def menuc():
    print("""
        Página Inicial - Clientes

        1 - Cadastrar Cliente
        2 - Atualizar Cliente
        3 - Listar Clientes
        4 - Excluir Cliente
        0 - Sair
    """)

def cadc(clientes):
    Nome = input("Digite o nome do cliente: ")
    Telefone = input("Digite o telefone do cliente: ")
    Email = input("Digite o e-mail do cliente: ")
    novo_cliente = {"Nome": Nome, "Telefone": Telefone, "Email": Email}
    clientes.append(novo_cliente)

def attc(clientes):
    if not clientes:
        print("Não existe nenhum cliente cadastrado")
        return
    ind = input("Digite o nome do cliente que deseja atualizar: ")
    for cliente in clientes:
        if cliente["Nome"] == ind:
            ask = int(input("O que você quer atualizar? 0 = Telefone, 1 = E-mail: "))
            if ask == 0:
                cliente["Telefone"] = input("Digite o novo telefone: ")
            elif ask == 1:
                cliente["Email"] = input("Digite o novo e-mail: ")
            else:
                print("Opção Inválida")
            print("Cliente atualizado")
            return
    print("Cliente não encontrado")

def lisc(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado")
        return
    print("\nLista de Clientes:")
    for cliente in clientes:
        print(f"Nome: {cliente['Nome']}, Telefone: {cliente['Telefone']}, E-mail: {cliente['Email']}")

def delc(clientes):
    if not clientes:
        print("Não existe nenhum cliente cadastrado")
        return
    ind = input("Digite o nome do cliente que quer excluir: ")
    for cliente in clientes:
        if cliente["Nome"] == ind:
            ask = int(input("Tem certeza que quer apagar? 0 = sim, 1 = não: "))
            if ask == 0:
                clientes.remove(cliente)
                print(f"Cliente {ind} removido")
                return
    print("Cliente não encontrado")

def mainc():
  global clientes
  while True:
    menuc()
    opcao = input("Digite uma opção: ")

    if opcao == "1":
      cadc(clientes)
    elif opcao == "2":
      attc(clientes)
    elif opcao == "3":
      lisc(clientes)
    elif opcao == "4":
      delc(clientes)
    elif opcao == "0":
      break
    else:
      print("Opção inválida")

"""MOVIMENTO DE ESTOQUE"""

def menue():
  print("""
      Menu de estoque

    1 - Listar Fornecedores e produtos
    2 - Verificar estoque do produto
    3 - Comprar produto
    4 - Relatórios de vendas
    5 - Abrir outros menus
    0 - Sair

  """)

def lisfp():
  if not produtos:
        print("Nenhum produto cadastrado")

  print("\nLista de Produtos:")
  for produto in produtos:
        print(f"ID: {produto['id']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}")

  if not clientes:
        print("Nenhum cliente cadastrado")

  print("\nLista de Clientes:")
  for fornec in clientes:
        print(f"Nome: {fornec['Nome']}, Produto: {fornec['Produto']}, Telefone: {fornec['Telefone']}, Endereço: {fornec['Endereço']}")

def verp():
  if not produtos:
    print("Não existe nenhum produto cadastrado")
    return
  ind = input("Digite o Id do produto que você quer verificar o estoque: ")
  for produto in produtos:
    if produto["id"] == ind:
      if produto["quantidade"] > 0:
        print(f"O produto com id de: '{produto['id']}' tem '{produto['quantidade']}' em estoque" )
      else:
        print("Produto sem estoque")
      return
  else:
    print("Produto não encontrado")

def salvar_dados():
    dados = {"clientes": clientes, "produtos": produtos, "vendas": vendas}
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_dados():
    global clientes, produtos, vendas
    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            clientes = dados.get("clientes", [])
            produtos = dados.get("produtos", [])
            vendas = dados.get("vendas", [])
    except FileNotFoundError:
        clientes = []
        produtos = []
        vendas = []

import json

def salvar_dados():
    dados = {"clientes": clientes, "produtos": produtos, "vendas": vendas}
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_dados():
    global clientes, produtos, vendas
    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            clientes = dados.get("clientes", [])
            produtos = dados.get("produtos", [])
            vendas = dados.get("vendas", [])
    except FileNotFoundError:
        clientes = []
        produtos = []
        vendas = []

def compp(clientes, produtos, vendas):
    if not produtos:
        print("Não existe nenhum produto cadastrado")
        return
    nome_cliente = input("Digite o nome do cliente que está comprando: ")
    for cliente in clientes:
        if cliente["Nome"] == nome_cliente:
            while True:
                id_produto = input("Digite o ID do produto que deseja comprar: ")
                for produto in produtos:
                    if produto["id"] == id_produto:
                        qtd = int(input(f"Existem {produto['quantidade']} unidades do produto disponíveis, quanto você deseja comprar?: "))
                        if qtd > produto["quantidade"]:
                            print("Erro: Quantidade desejada maior que o estoque disponível.")
                        else:
                            preco_total = qtd * produto['preco']
                            venda = {
                                "Cliente": nome_cliente,
                                "ID do Produto": produto["id"],
                                "Quantidade_cpd": qtd,
                                "Preço Total": preco_total
                            }
                            vendas.append(venda)
                            produto['quantidade'] -= qtd
                            salvar_dados()
                            print(f"Compra realizada com sucesso por {nome_cliente}! Restam {produto['quantidade']} unidades.")
                            
                            continuar = input("Deseja comprar mais produtos? (s/n): ").lower()
                            if continuar != "s":
                                return
                print("Produto não encontrado")
                return
    print("Cliente não cadastrado")

def rele(vendas):
  if not vendas:
    print("Nenhuma venda cadastrada")
    return

  for venda in vendas:
    print(f"Cliente: {venda['Cliente']}, ID do produto: {venda['ID do Produto']}, Quantidade comprada: {venda['Quantidade_cpd']}, preço da venda: {venda['Preço Total']:.2f}")

carregar_dados()

clientes = []
produtos = []
vendas = []

def maine():
    global vendas
    while True:

        print("""
            Menu de Estoque

            1 - Listar Produtos
            2 - Verificar estoque
            3 - Comprar produto
            4 - Relatórios de vendas
            5 - Gerenciar Clientes
            6 - Gerenciar produtos
            0 - Sair
        """)

        opcao = input("Digite uma opção: ")
        if opcao == "1":
            lisp(produtos)
        elif opcao == "2":
            verp()
        elif opcao == "3":
            compp(clientes, produtos, vendas)
        elif opcao == "4":
            rele(vendas)
        elif opcao == "5":
            mainc()
        elif opcao == "6":
            mainp()
        elif opcao == "0":
            salvar_dados()
            break
        else:
            print("Opção inválida")
maine()
