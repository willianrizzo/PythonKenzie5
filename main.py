from residencias.residencia import Residencia, Apartamento

def main():
    residencia = Residencia(2, 7.2, "rua dois", 40000, "10|07|2022")
    print(residencia)
    # print("-"*72)
    print(residencia.monstrar_detalhes())
    print("-"*72)

    apt = Apartamento(4, 50.12,"Rua Cinco", 8200.6, "11|03|1999", 7, 3)
    print(apt)
    print(apt.monstrar_detalhes())
    
    
if __name__ == "__main__":
    main()