class Residencia:
    def __init__(self, 
        num_quartos: int, 
        area: float, 
        endereco: str, 
        preco: float, 
        alugado_em: str
    ) -> None:
        self.num_quartos = num_quartos
        self.area = area
        self.endereco = endereco
        self.preco = preco
        self.alugao_em = alugado_em

    def __repr__(self) -> str:
        return f"<Residencia: {self.endereco} - {self.preco}>"

    def monstrar_detalhes(self) -> str:
        return(
            f"<Localiado em: {self.endereco}\n"
            f"QTD quartos {self.num_quartos}\n"
            f"Alugado em : {self.alugao_em}\n"
            f"Valor total: {self.preco}>"
        )
        # return f"<Localiado em: {self.endereco}\n QTD quartos {self.num_quartos}\n Valor total: {self.preco}"


class Apartamento(Residencia):
    def __init__(self, 
        num_quartos: int, 
        area: float, 
        endereco: str, 
        preco: float, 
        alugado_em: str,
        andar: int, 
        num_elevadores: int

        ) -> None:
        super().__init__(num_quartos, area, endereco, preco, alugado_em)
        self.andar = andar
        self.num_elevadores = num_elevadores