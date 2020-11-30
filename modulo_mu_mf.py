# ****************************************************************
# ********************** MÉDIA DAS UNIDADES **********************
# ****************************************************************
def mu_atingiu_media(media1_unid, media2_unid, media_final):
    print('********************************************')
    print('Média das Unidades exigida (MU): 6.0')
    print('Fórmula da MU: (({} * 4) + ({} * 6)) / 10'.format(media1_unid, media2_unid))
    print('Parabéns! Você atingiu a média exigida! {:.1f}'.format(media_final))
    print('********************************************')

def mu_nao_atingiu_media(media1_unid, media2_unid, media_final, diferenca):
    print('********************************************')
    print('Média das Unidades exigida (MU): 6.0')
    print('Fórmula da MU: (({} * 4) + ({} * 6)) / 10'.format(media1_unid, media2_unid))
    print('Ops! Você não atingiu a média exigida!: {:.1f}'.format(media_final))
    print('Diferença: {:.1f}'.format(diferenca))
    print('********************************************')


# ****************************************************************
# ************************* MÉDIA FINAL **************************
# ****************************************************************
def mf_atingiu_media(media_unid, prova_final, media_final):
    print('*******************************************')
    print('Média Final exigida (MF): 5.0')
    print('Fórmula da MF: (({} * 6) + ({} * 4)) / 10'.format(media_unid, prova_final))
    print('Parabéns! Você atingiu a média exigida! {:.1f}'.format(media_final))
    print('*******************************************')

def mf_nao_atingiu_media(media_unid, prova_final, media_final, diferenca):
    print('*******************************************')
    print('Média Final exigida (MF): 5.0')
    print('Fórmula da MF: (({} * 6) + ({} * 4)) / 10'.format(media_unid, prova_final))
    print('Ops! Você não atingiu a média exigida!: {:.1f}'.format(media_final))
    print('Diferença: {:.1f}'.format(diferenca))
    print('*******************************************')

