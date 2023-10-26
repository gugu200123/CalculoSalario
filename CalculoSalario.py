opcao = 0 
while opcao != 4:
  print("-----------------------------------------")
  print("Menu de opções:")
  print("1.Novo salário")
  print("2.Férias")
  print("3.Décimo terceiro")
  print("4.Calcular Inss")
  print("-----------------------------------------")
  opcao=int(input("Digite a opção desejada:"))
  if opcao == 1:
    salario = float(input("Digite o salário:"))
    if salario < 3500.00:
      salario = salario * 1.15
    elif salario >= 3500 and salario <= 6000:
      salario= salario * 1.10
    elif salario > 6000:
      salario =salario * 1.05
    print("O novo salário é:", salario)
  elif opcao == 2:
    salario = float(input("Digite o salário:"))
    ferias = salario * 1.33
    print("O valor das ferias é:", ferias)
  elif opcao == 3:
    salario = float(input("Digite o salário:"))
    mesesTrabalhados = int(input("Quantos meses trabalhou na empresa este ano?"))
    if mesesTrabalhados <= 12:
      print("O valor do décimo terceiro é:", salario * mesesTrabalhados / 12)
    else:
      print("Valor incorreto detectado!!!!!!!")
  elif opcao ==4:
    print("Encerrando o programa...")
  else:
    print("Opção inválida!!!")
   
      
      
  
    