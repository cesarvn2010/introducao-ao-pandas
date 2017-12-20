import numpy as np

def os_testes_passaram():
    print("Parabéns! Os testes passaram.")

def verificar_cenario_01(df):
    ex = Exception("O dataframe não foi criado corretamente.")

    if df is None:
        raise ex

    columns = ['Id','ValorVencido','Sexo','EstadoCivil','DataNascimento','ValorPago']

    for c in columns:
        if c not in df.columns:
            raise ex

    os_testes_passaram()

def verificar_cenario_02(cinco_primeiras_linhas):
    ex = Exception("As cinco primeiras linhas foram extraídas incorretamente.")

    if cinco_primeiras_linhas is None:
        raise ex

    if len(cinco_primeiras_linhas) != 5:
        raise ex

    os_testes_passaram()

def verificar_cenario_03(fn):
    ex = Exception("A função não foi definida corretamente.")

    if fn is None:
        raise ex

    valor1 = fn("123,45")

    if valor1 != 123.45:
        raise ex

    valor2 = fn("1.234,56")

    if valor2 != 1234.56:
        raise ex

    valor3 = fn(1.23)

    if valor3 != 1.23:
        raise ex

    os_testes_passaram()

def verificar_cenario_04(df):
    ex = Exception("As colunas não foram convertidas corretamente.")

    if df is None:
        raise ex

    if 'ValorVencido' not in df:
        raise ex

    if 'ValorPago' not in df:
        raise ex

    if df['ValorVencido'].dtype != np.float64:
        raise ex

    if df['ValorPago'].dtype != np.float64:
        raise ex

    os_testes_passaram()

def verificar_cenario_05(tipo, valor):
    ex = Exception("Cálculos incorretos.")

    if tipo is None or valor is None:
        raise ex

    if "media_das_dividas" == tipo:
        if valor < 547.83 or valor > 547.84:
            raise ex

    if "media_dos_pagamentos" == tipo:
        if valor < 281.33 or valor > 281.34:
            raise ex

    if "razao_entre_total_pago_e_total_devido" == tipo:
        if valor < 0.5135 or valor > 0.5136:
            raise ex

    os_testes_passaram()

def verificar_cenario_06_dataframe(tipo, df):
    ex = Exception("O dataframe não foi separado corretamente.")

    if tipo is None or df is None:
        raise ex

    if "casados" == tipo:
        if len(df) != 16337:
            raise ex

    if "solteiros" == tipo:
        if len(df) != 7558:
            raise ex

    if "outros" == tipo:
        if len(df) != 5147:
            raise ex

    os_testes_passaram()

def verificar_cenario_06_razao(tipo, valor):
    ex = Exception("Cálculo incorreto.")

    if tipo is None or valor is None:
        raise ex

    if "casados" == tipo:
        if valor < 0.53 or valor > 0.54:
            raise ex

    if "solteiros" == tipo:
        if valor < 0.46 or valor > 0.47:
            raise ex

    if "outros" == tipo:
        if valor < 0.53 or valor > 0.54:
            raise ex

    os_testes_passaram()

def verificar_desafio_01_dataframe(tipo, df):
    ex = Exception("O dataframe não foi separado corretamente.")

    if tipo is None or df is None:
        raise ex

    if "mulheres" == tipo:
        if len(df) != 18862:
            raise ex

    if "homens" == tipo:
        if len(df) != 10585:
            raise ex

    os_testes_passaram()


def verificar_desafio_01_razao(tipo, valor):
    ex = Exception("Cálculo incorreto.")

    if tipo is None or valor is None:
        raise ex

    if "mulheres" == tipo:
        if valor < 0.50 or valor > 0.51:
            raise ex

    if "homens" == tipo:
        if valor < 0.53 or valor > 0.54:
            raise ex

    os_testes_passaram()

def verificar_desafio_02_decada(fn):
    ex = Exception("A função foi implementada incorretamente.")

    year60 = 1961
    year70 = 1977
    year80 = 1989

    if fn(year60) != 60:
        raise ex

    if fn(year70) != 70:
        raise ex

    if fn(year80) != 80:
        raise ex

    os_testes_passaram()

def verificar_desafio_02_serie_decada(df):
    ex = Exception("A série Decada não foi criada corretamente.")

    if df is None:
        raise ex

    if 'Decada' not in df:
        raise ex

    for decada in df['Decada']:
        if decada % 10 != 0:
            print('Década incorreta:', decada)
            raise ex

    os_testes_passaram()

def verificar_desafio_02_razao_decadas(dicionario):
    ex = Exception("O dicionário de cálculos foi preenchido incorretamente.")

    if dicionario is None:
        raise ex

    if len(dicionario) != 9:
        raise ex

    if dicionario[20] != 1.0:
        raise ex

    if dicionario[30] < 0.20 or dicionario[30] > 0.21:
        raise ex

    if dicionario[40] < 0.43 or dicionario[40] > 0.44:
        raise ex

    if dicionario[50] < 0.40 or dicionario[50] > 0.41:
        raise ex

    if dicionario[60] < 0.42 or dicionario[60] > 0.43:
        raise ex

    if dicionario[70] < 0.48 or dicionario[70] > 0.49:
        raise ex

    if dicionario[80] < 0.58 or dicionario[80] > 0.59:
        raise ex

    if dicionario[90] < 0.58 or dicionario[90] > 0.59:
        raise ex

    if dicionario[100] < 0.20 or dicionario[100] > 0.21:
        raise ex

    os_testes_passaram()