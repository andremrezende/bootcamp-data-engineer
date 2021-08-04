from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%D-%M-%Y'))

    print(data_atual.strftime('%A %B'))
    
def trabalhando_com_time():
    horario = time(hour=15, minute=10, second=30)
    print(horario.strftime('%H:%M:%S'))
    
def trabalhando_com_datetime():
    atual = datetime.now()
    print(atual)
    print(atual.strftime('%c'))
    print(atual.year)
    print(atual.minute)
    
def dia_semana():
    atual = datetime.now()
    dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(dias[atual.weekday()])

def stringData2datatime():
    data_string = '01/01/2020'
    print(type(datetime.strptime(data_string, '%d/%m/%Y')))
    
def diferencaDatas():
    anoPassado = datetime.now() - timedelta(days=365, hours=2, minutes=15)
    print(anoPassado)
    

if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()
    dia_semana()
    stringData2datatime()
    diferencaDatas()