# Sistema simples: aula cedo = dentro | aula à tarde = fora

turno = input("Digite o turno da aula (cedo/tarde): ").lower()

if turno == "cedo":
    print("✅ Você está dentro")
elif turno == "tarde":
    print("❌ Você está fora")
else:
    print("⚠️ Turno inválido")