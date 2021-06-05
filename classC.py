class Calculadora:
    _area_parede : float
    _area_teto : float
    _cal_litragem : float

    def calcular_area_parede(largura,profundidade,altura):
        area_parede = (2*(largura + profundidade)*altura)
        return area_parede
    def calcular_area_teto(largura,profundidade):   
        area_teto = (largura * profundidade)
        return area_teto 
    def calcular_cal_litragem(area_parede,area_teto):
        if area_parede <= 0 or area_teto <=0:
            print('não é possivel calcular a litragem com os valores informados')
            exit()
        return (area_parede + area_teto) / 10
        