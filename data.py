from datetime import datetime
from pytz import timezone, all_timezones


def data_da_consulta():
    """
    Função para verificar a data e hora na máquina do usuário
    Returns:
        str: Data e hora do usuário com referência fixada a São Paulo. 
    """
    data_hora_atual = datetime.now()
    fuso_horário = timezone('America/Sao_Paulo')
    # converter o tempo da máquina para o de São Paulo
    data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horário)
    data_hora_sao_paulo_texto = data_hora_sao_paulo.strftime('%d/%m/%Y  %H:%M')
    return data_hora_sao_paulo_texto


# Para ver lista de fusos horários
'''for tz in all_timezones:
    print(tz)'''
