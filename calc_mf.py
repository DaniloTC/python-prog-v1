import modulo_mu_mf as calc

def calcular_mf():
    media_unid = float(input('Digite sua Média das Unid.: '))
    prova_final = float(input('Digite sua nota na Prova Final.: '))
    diferenca = 0

    # Fórmula para calcular a média final, segundo a instituição de ensino.
    media_final = ((media_unid * 6) + (prova_final * 4)) / 10

    # Calculando a diferença caso a média exigida não seja atingida.
    # A média final precisava ser maior ou igual a 5
    if media_final < 5:
        diferenca = 5 - media_final

    # Imprimindo mensagem com base na média obtida
    if media_final >= 5:
        calc.mf_atingiu_media(media_unid, prova_final, media_final)
    else:
        calc.mf_nao_atingiu_media(media_unid, prova_final, media_final, diferenca)

if __name__ == '__main__':
    calcular_mf()
