import PySimpleGUI as sg

sg.theme('DarkAmber')

def janela_menu():
    layout = [
        [sg.Text('MENU', font='Courier 18')],
        [sg.Button('Calcular Média das Unidades', key='calc_mu')],
        [sg.Button('Calcular Média Final', key='calc_mf')]
    ]
    return sg.Window('Sistema de Cálculo', layout=layout, finalize=True)

def calcular_mu():
    layout = [
        [sg.Text('Calcular Média das Unidades', font='Courier 18')],
        [sg.Text('Obs. Use ponto (.) para separar inteiro de décimo.')],
        [sg.Text('')],
        [sg.Text('Media 1a Unid.'), sg.InputText(key='media1unid', size=(15,0), focus=True), sg.Text('Media 2a Unid.'), sg.InputText(key='media2unid', size=(15,0))],
        [sg.Output(size=(58,10))],
        [sg.Button('<< Menu', key='voltar1'), sg.Button('Calcular', key='calc1')]
    ]
    return sg.Window('Cálculo da Média das Unidades', layout=layout, finalize=True)

def calcular_mf():
    layout = [
        [sg.Text('Calcular Média Final', font='Courier 18')],
        [sg.Text('Obs. Use ponto (.) para separar inteiro de décimo.')],
        [sg.Text('')],
        [sg.Text('Media das Unid.'), sg.InputText(key='mediaUnid', size=(15,0), focus=True), sg.Text('Prova Final.'), sg.InputText(key='provaFinal', size=(15,0))],
        [sg.Output(size=(57,10))],
        [sg.Button('<< Menu', key='voltar2'), sg.Button('Calcular', key='calc2')] 
    ]
    return sg.Window('Cálculo da Média Final', layout=layout, finalize=True)

# inicializando variáveis
menu, calc_media_unidades, calc_media_final = janela_menu(), None, None

while True:
    # setando leitura de eventos e valores em todas as janelas
    window, event, values = sg.read_all_windows()

    # critério para sair do laço
    if (window == menu and event == sg.WIN_CLOSED) or (window == calc_media_unidades and event == sg.WIN_CLOSED) or (window == calc_media_final and event == sg.WIN_CLOSED):
        break

    # acessar janela para calcular media das unidades
    elif window == menu and event == 'calc_mu':
        menu.hide()
        calc_media_unidades = calcular_mu()
    
    # acessar janela para calcular media final
    elif window == menu and event == 'calc_mf':
        menu.hide()
        calc_media_final = calcular_mf()

    # janela para calcular MU
    elif window == calc_media_unidades and event == 'calc1':
        media1 = float(values['media1unid'])
        media2 = float(values['media2unid'])
        media_unid = ((media1 * 4) + (media2 * 6)) / 10

        if media_unid < 6:
            diferenca = 6 - media_unid

        if media_unid >= 6:
            print('Média das Unidades exigida (MU): 6.0')
            print('Fórmula da MU: (({} * 4) + ({} * 6)) / 10'.format(media1, media2))
            print('Parabéns! Você atingiu a média exigida! {:.1f}'.format(media_unid))
            print('')
        else:
            print('Média das Unidades exigida (MU): 6.0')
            print('Fórmula da MU: (({} * 4) + ({} * 6)) / 10'.format(media1, media2))
            print('Ops! Você não atingiu a média exigida! {:.1f}'.format(media_unid))
            print('Diferença: {:.1f}'.format(diferenca))
            print('')
    
    # janela para calcular MF
    elif window == calc_media_final and event == 'calc2':
        media_unid = float(values['mediaUnid'])
        prova_final = float(values['provaFinal'])
        media_final = ((media_unid * 6) + (prova_final * 4)) / 10

        if media_final < 5:
            diferenca = 5 - media_final

        if media_final >= 5:
            print('Média Final exigida (MF): 5.0')
            print('Fórmula da MF: (({} * 6) + ({} * 4)) / 10'.format(media_unid, prova_final))
            print('Parabéns! Você atingiu a média exigida! {:.1f}'.format(media_final))
            print('')
        else:
            print('Média Final exigida (MF): 5.0')
            print('Fórmula da MF: (({} * 6) + ({} * 4)) / 10'.format(media_unid, prova_final))
            print('Ops! Você não atingiu a média exigida!: {:.1f}'.format(media_final))
            print('Diferença: {:.1f}'.format(diferenca))
            print('')
    
    # do cálculo MU voltar para menu
    elif window == calc_media_unidades and event == 'voltar1':
        calc_media_unidades.hide()
        menu.un_hide()
    
    # do cálculo MF voltar para menu
    elif window == calc_media_final and event == 'voltar2':
        calc_media_final.hide()
        menu.un_hide()

window.close()
