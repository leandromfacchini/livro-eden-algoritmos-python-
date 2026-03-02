# Exemplo: decidir o que vestir com base na temperatura

def vestir(temperatura) -> str:
    if temperatura < 18:
        return "Coloque um casaco"
    elif temperatura < 25:
        return "Vista uma camiseta"
    else:
        return "Use roupas leves"


print(vestir(22))
