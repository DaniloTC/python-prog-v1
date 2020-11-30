import modulo_mu_mf as calc

def calcular_mu():
    media1_unid = float(input('Digite sua Média da 1a Unid.: '))
    media2_unid = float(input('Digite sua Média da 2a Unid.: '))
    diferenca = 0

    # Fórmula para calcular a média das unidades, segundo a instituição de ensino.
    media_final = ((media1_unid * 4) + (media2_unid * 6)) / 10

    # Calculando a diferença caso a média exigida não seja atingida.
    # A média final das unidades precisava ser maior ou igual a 6
    if media_final < 6:
        diferenca = 6 - media_final

    # Imprimindo mensagem com base na média obtida
    if media_final >= 6:
        calc.mu_atingiu_media(media1_unid, media2_unid, media_final)
    else:
        calc.mu_nao_atingiu_media(media1_unid, media2_unid, media_final, diferenca)

if __name__ == '__main__':
    calcular_mu()
