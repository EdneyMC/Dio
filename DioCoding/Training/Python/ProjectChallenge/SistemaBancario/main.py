depositar = []
sacar = []
extrato = 0.0
saldoConta = 0.0
saldoDepositar = 0.0 dfgsggsg
saldoSacar = 0.0
contadorSaque = 0
contadorValorMinimoSaque = 0
contadorValorMaximoSaque = 0
contadorValorMinimoDeposito = 0
contadorSaldoInsuficiente = 0

redirecionarMenu = '\nVocê será redirecionado ao menu incial!\n'
menu = ('''
SISTEMA BANCÁRIO
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
''').center(88, "#")

while True:
  print(menu)
  valorMenu = input("\nDigite a opção desejada: \n")
  
  if valorMenu == '1':
                
    while True: 
    
      if contadorValorMinimoDeposito < 2:
        valorDepositar = float(input("\nDigite o valor que deseja depositar: "))
      
        if valorDepositar <= 0:
          print("\nAtenção! Digite valor acima de 0!")
          contadorValorMinimoDeposito += 1
        
        else:
          depositar.append(valorDepositar)
          saldoDepositar += float(valorDepositar)
          saldoConta += valorDepositar
          print(f"\nDeposito concluído com sucesso!\n{redirecionarMenu}")
          break
      else:
        print(f"{redirecionarMenu}")
        break
      
  elif valorMenu == '2':
    
    if contadorSaque >= 3:
      print(f"\nAtenção! Você já realizaou o limite de 3 saques por dia!\n{redirecionarMenu}\n")
      
    else:

      contadorValorMinimoSaque = 0
      contadorValorMaximoSaque = 0
      contadorSaldoInsuficiente = 0
      
      while (contadorValorMinimoSaque and contadorValorMaximoSaque and contadorSaldoInsuficiente) < 2:
        
        if (contadorValorMinimoSaque or contadorValorMaximoSaque or contadorSaldoInsuficiente) < 2:
          valorSacar = float(input("\nDigite o valor que deseja sacar: \n"))

          if valorSacar > saldoConta:
            print(f"Atenção! Saldo insuficiente!\nSeu saldo atual é: R$ {saldoConta:.2f}\n")
            contadorSaldoInsuficiente += 1
            
          elif valorSacar < 2:
            print("\nAtenção! Digite valor a partir de R$ 2.00!\n")
            contadorValorMinimoSaque += 1
            
          elif valorSacar > 500:
            print("\nAtenção! O seu limite por saque é de R$ 500.00!")
            contadorValorMaximoSaque += 1
            
          else:
            sacar.append(valorSacar)
            saldoSacar += float(valorSacar)
            saldoConta -= valorSacar
            print(f"\nSaque concluído com sucesso!\n{redirecionarMenu}\n")
            contadorSaque += 1
            break
            
        else:
          print(f"{redirecionarMenu}\n")
          break
          
  elif valorMenu == '3':
    
    if (depositar == []) and (sacar == []):
      print(f"\nNão existem movimentações!\n{redirecionarMenu}\n")
      
    else: 
      print("EXTRATO BANCÁRIO".center(18, "#"))
      print("\nDEPóSITOS\n")

      if (depositar == []):
        print("Não existem movimentações para depósitos!")

      else:
        for i in depositar:
          print(f'R$ {i:5.2f}')
        print(f"\nTotal de depósitos: R$ {saldoDepositar:.2f}")
    
      print("\nSAQUES\n")

      if (sacar == []):
        print("Não existem movimentações para saques!")

      else:
        for i in sacar:
          print(f'R$ {i:.2f}')
        print(f"\nTotal de saques: R$ {saldoSacar:.2f}")
        
      saldoAtual = saldoDepositar-saldoSacar
      print(f"\nSEU SALDO ATUAL É: R$ {saldoAtual:.2f}\n{redirecionarMenu}\n")
      
  elif valorMenu == '0':
    print("\nObrigado por utilizar nosso sistema bancário!\n")
    break
    
  else:
    print("\nAtenção! Digite uma opção válida!!!\n\n")