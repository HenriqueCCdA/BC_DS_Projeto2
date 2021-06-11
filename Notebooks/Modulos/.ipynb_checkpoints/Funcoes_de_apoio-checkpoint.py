import pandas as pd

def lendo_o_df(path, head = True, tail = True):
    '''
    Le o dataframe
    
    @param path - Caminho do DataFrame
    @param head - Plot o head DataFrame
    @param tail - Plot o tail DataFrame
    
    @return retorna do DataFrame lido
    '''
    
    df = pd.read_csv(path, 
                     index_col = 0,
                     usecols=['Ano', '072 BCG'],
                     encoding="ISO-8859-1",
                     skiprows = 5, sep=";", 
                     skipfooter=19,
                     thousands=".",
                     decimal=",",
                     engine="python"  )
    
    df.drop("Total", inplace=True)
    df.reset_index(inplace=True)
   
    df.Ano = df.Ano.astype('int64')
    df.set_index('Ano', inplace=True)

    if head:
        display(df.head())
    if tail:
        display(df.tail())
    
    return df

def caracteristica_data_frame(df):
    '''
    Obtem algumas informações do DataFrame
    
    @param df - DataFrame
    
    @return Nenhum tipo de retorno
    '''    
    
    l, c = df.shape
    anos = df.index.tolist()
    
    print(f"Numero de linhas: {l}")
    print(f"Numero de colunas: {c}")
    
    for ano in anos:
         print(ano, end=' ')
    
    print()  
    df.info()  
    print('\n')  