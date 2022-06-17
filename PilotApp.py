# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 23:01:51 2022

@author: ACER
"""
import pandas as pd
import streamlit as st
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import xlsxwriter
import numpy as np

##################################################################################################################################################################################

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data

##################################################################################################################################################################################
#2. DATA CLEANING AND EXPLORATORY DATA ANALYSIS

df  = pd.read_excel('CopaLigaArgentina22Apertura_AllMetricsCalculated.xlsx')
df2 = pd.read_excel('PrimeraDivisiónChile22Apertura_AllMetricsCalculated.xlsx')
df3 = pd.read_excel('PrimeraDivisiónEcuador22Apertura_AllMetricsCalculated.xlsx')
df4 = pd.read_excel('Uruguay22Apertura160622_AllMetricsCalculated.xlsx')
df5 = pd.read_excel('Bolivia22Apertura_AllMetricsCalculated.xlsx')
df6 = pd.read_excel('Venezuela22Apertura160622_AllMetricsCalculated.xlsx')
df7 = pd.concat([df, df2, df3, df4, df5, df6])

# df.isnull().sum()
# df2.isnull().sum()
# df3.isnull().sum()

# df = df.fillna(0)
# df2 = df.fillna(0)
# df3 = df.fillna(0)

# df['Total successful defensive actions'] = df['Total successful defensive actions'].astype(np.int64)
# df['Total defensive duels'] = df['Total defensive duels'].astype(np.int64)
# df['Total defensive duels won'] = df['Total defensive duels won'].astype(np.int64)
# df['Total sliding tackles'] = df['Total sliding tackles'].astype(np.int64)
# df['Total interceptions'] = df['Total interceptions'].astype(np.int64)
# df['Total shots blocked'] = df['Total shots blocked'].astype(np.int64)

# df['Total successful attacking actions'] = df['Total successful attacking actions'].astype(np.int64)
# df['Total shots on target'] = df['Total shots on target'].astype(np.int64)
# df['Total offensive duels'] = df['Total offensive duels'].astype(np.int64)
# df['Total offensive duels won'] = df['Total offensive duels won'].astype(np.int64)
# df['Total touches in box'] = df['Total touches in box'].astype(np.int64)

# df['Total crosses'] = df['Total crosses'].astype(np.int64)
# df['Total crosses completed'] = df['Total crosses completed'].astype(np.int64)
# df['Total crosses to goalie box'] = df['Total crosses to goalie box'].astype(np.int64)
# df['Total shot assists'] = df['Total shot assists'].astype(np.int64)
# df['Total second assists'] = df['Total second assists'].astype(np.int64)
# df['Total third assists'] = df['Total third assists'].astype(np.int64)
# df['Total smart passes'] = df['Total smart passes'].astype(np.int64)
# df['Total smart passes completed'] = df['Total smart passes completed'].astype(np.int64)
# df['Total key passes'] = df['Total key passes'].astype(np.int64)
# df['Total passes to penalty area'] = df['Total passes to penalty area'].astype(np.int64)
# df['Total passes to penalty area completed'] = df['Total passes to penalty area completed'].astype(np.int64)
# df['Total through passes'] = df['Total through passes'].astype(np.int64)
# df['Total through passes completed'] = df['Total through passes completed'].astype(np.int64)
# df['Total deep completions'] = df['Total deep completions'].astype(np.int64)
# df['Total deep completed crosses'] = df['Total deep completed crosses'].astype(np.int64)

# df['Total passes'] = df['Total passes'].astype(np.int64)
# df['Total passes completed'] = df['Total passes completed'].astype(np.int64)
# df['Total forward passes'] = df['Total forward passes'].astype(np.int64)
# df['Total forward passes completed'] = df['Total forward passes completed'].astype(np.int64)
# df['Total back passes'] = df['Total back passes'].astype(np.int64)
# df['Total back passes completed'] = df['Total back passes completed'].astype(np.int64)
# df['Total lateral passes'] = df['Total lateral passes'].astype(np.int64)
# df['Total lateral passes completed'] = df['Total lateral passes completed'].astype(np.int64)
# df['Total short / medium passes'] = df['Total short / medium passes'].astype(np.int64)
# df['Total short / medium passes completed'] = df['Total short / medium passes completed'].astype(np.int64)
# df['Total long passes'] = df['Total long passes'].astype(np.int64)
# df['Total long passes completed'] = df['Total long passes completed'].astype(np.int64)
# df['Total passes to final third'] = df['Total passes to final third'].astype(np.int64)
# df['Total passes to final third completed'] = df['Total passes to final third completed'].astype(np.int64)
# df['Total progressive passes'] = df['Total progressive passes'].astype(np.int64)

# df['Total duels'] = df['Total duels'].astype(np.int64)
# df['Total duels won'] = df['Total duels won'].astype(np.int64)
# df['Total aerial duels'] = df['Total aerial duels'].astype(np.int64)
# df['Total aerial duels won'] = df['Total aerial duels won'].astype(np.int64)
# df['Total fouls'] = df['Total fouls'].astype(np.int64)
# df['Total dribbles'] = df['Total dribbles'].astype(np.int64)
# df['Total successful dribbles'] = df['Total successful dribbles'].astype(np.int64)
# df['Total progressive runs'] = df['Total progressive runs'].astype(np.int64)
# df['Total accelerations'] = df['Total accelerations'].astype(np.int64)
# df['Total received passes'] = df['Total received passes'].astype(np.int64)
# df['Total received long passes'] = df['Total received long passes'].astype(np.int64)
# df['Total fouls suffered'] = df['Total fouls suffered'].astype(np.int64)



# dfaux = df[['Player', 'Team']]

# dfx = df["Position"].str.split(",", expand = True)
# dfx.columns = ['Position', 'Pos2', 'Pos3']

# dfx["Position"] = dfx["Position"].replace(['LDMF', 'DMF', 'RDMF'],['CEM','CEM','CEM'])
# dfx["Position"] = dfx["Position"].replace(['LCMF', 'CMF', 'RCMF'],['MED','MED','MED'])
# dfx["Position"] = dfx["Position"].replace(['LAMF', 'AMF', 'RAMF'],['VOL','VOL','VOL'])
# dfx["Position"] = dfx["Position"].replace(['RCB', 'CB', 'LCB', 'GK'],['DEF', 'DEF', 'DEF', 'POR'])
# dfx["Position"] = dfx["Position"].replace(['RB', 'RWB', 'LB', 'LWB'],['LAT', 'LAT', 'LAT', 'LAT'])
# dfx["Position"] = dfx["Position"].replace(['RW', 'LW'],['BAN', 'BAN'])
# dfx["Position"] = dfx["Position"].replace(['RWF', 'LWF'],['EXT', 'EXT'])
# dfx["Position"] = dfx["Position"].replace(['CF'],['DEL'])

# dfc = df.drop(["Player", "Team", "Position", "Unnamed: 0"], axis=1)
# dfc.style.format("{:.5%}")
# df = pd.concat([dfaux, dfx, dfc], axis=1)

# df = df.drop(["Pos3"], axis=1)
#df.rename(columns = {'0':'Position', '1':'Pos2', '2':'Pos3'}, inplace=True)  
      
##################################################################################################################################################################################

st.set_page_config(layout="wide")
          
##################################################################################################################################################################################

with st.sidebar:
    st.image("https://i.ibb.co/qjvrH5y/win.png", width=250) 
    #st.title('Win Stats Data App')
    
    ligas = ['Todos los campeonatos', 'Primera División Argentina', 'Primera División Chile', 'Primera División Ecuador', 'Primera División Uruguay', 'Primera División Venezuela', 'Primera División Bolivia']
    defa = "Todos los campeonatos"
    leaguesel = st.multiselect('Selecciona los campeonatos:', ligas, default=defa)  
    for i in leaguesel:
        if i == "Primera División Argentina":
            df = df
        elif i == "Primera División Chile":
            df = df2
        elif i == "Primera División Ecuador":
            df = df3
        elif i == "Primera División Uruguay":
            df = df4
        elif i == "Primera División Bolivia":
            df = df5
        elif i == "Primera División Venezuela":
            df = df6
        elif i == "Todos los campeonatos":
            df = df7

    edadsel = st.slider('Selecciona rango de edad:', 15, 50, (15, 25), 1)
    df = df[df['Age'] <= edadsel[1]]
    df = df[df['Age'] >= edadsel[0]]
        
    teams = df['Team'].tolist()
    teams.append("Todos los equipos")
    teams = set(teams)   
    df30 = df
    defat = "Todos los equipos"
    teamsel = st.multiselect('Selecciona los equipos:', teams, default=defat)
    df = df[df['Team'].isin(teamsel)]    
    for i in teamsel:
        if i == 'Todos los equipos':
            df = df30
        else:
            df = df
        
    minsel  = st.slider('Selecciona mínimo de minutos disputados:', 0, 2000)    
    df = df[df['Minutes played'] >= minsel]
            
    positions = df['Position'].tolist()
    positions.append("Todas las posiciones")
    positions = set(positions)   
    defau = "Todas las posiciones" 
    possel = st.multiselect('Selecciona las posiciones:', positions, default=defau)
    df20 = df
    df = df[df['Position'].isin(possel)]
    for i in possel:
        if i == 'Todas las posiciones':
            df = df20
        else:
            st.write("None")
            df = df    

    dfsel = st.radio("Selecciona opción de datos:", ["Métricas Globales", "Métricas Normalizadas"])
    if dfsel == 'Normalizado':
        df = df[["Player", "Team", "Position", "Age", "Matches played", "Minutes played", "90s",
                  "Successful defensive actions per 90",
                  "Defensive duels per 90",
                  "Defensive duels won per 90",
                  "Sliding tackles per 90",
                  "PAdj Sliding tackles",
                  "Interceptions per 90",
                  "PAdj Interceptions",
                  "Shots blocked per 90",
                  "Goals per 90",
                  "xG per 90",
                  "Successful attacking actions per 90",
                  "NPxG per 90",
                  "Non-penalty goals per 90",
                  "Head goals per 90",
                  "Shots per 90",
                  "Shots on target per 90",
                  "Offensive duels per 90",
                  "Offensive duels won per 90",
                  "Touches in box per 90",
                  "Assists per 90",
                  "xA per 90",
                  "Crosses per 90",
                  "Crosses completed per 90",
                  "Crosses from left flank per 90",
                  "Crosses from right flank per 90",
                  "Crosses to goalie box per 90",
                  "Shot assists per 90",
                  "Second assists per 90",
                  "Third assists per 90",
                  "Smart passes per 90",
                  "Smart passes completed per 90",
                  "Key passes per 90",
                  "Passes to penalty area per 90",
                  "Passes to penalty area completed per 90",
                  "Through passes per 90",
                  "Through passes completed per 90",
                  "Deep completions per 90",
                  "Deep completed crosses per 90",
                  "Passes per 90",
                  "Passes completed per 90",
                  "Forward passes per 90",
                  "Forward passes completed per 90",
                  "Back passes per 90",
                  "Back passes completed per 90",
                  "Lateral passes per 90",
                  "Lateral passes completed per 90",
                  "Short / medium passes per 90",
                  "Short / medium passes completed per 90",
                  "Long passes per 90",
                  "Long passes completed per 90",
                  "Progressive passes per 90",
                  "Progressive passes completed per 90",
                  "Duels per 90",
                  "Duels won per 90",
                  "Aerial duels per 90",
                  "Aerial duels won per 90",
                  "Fouls per 90",
                  "Dribbles per 90",
                  "Successful dribbles per 90",
                  "Progressive runs per 90",
                  "Accelerations per 90",
                  "Received passes per 90",
                  "Received long passes per 90",
                  "Fouls suffered per 90",
                  "Conceded goals per 90",
                  "Shots against per 90",
                  "xG against per 90",
                  "Prevented goals per 90",
                  "Back passes received as GK per 90",
                  "Exits per 90",
                  "Aerial duels per 90.1",
                  "Free kicks per 90",
                  "Direct free kicks per 90",
                  "Corners per 90",
                  "Yellow cards per 90",
                  "Red cards per 90"]]
    else:
        df = df[["Player", "Team", "Position", "Age", "Matches played", "Minutes played", "90s",
                  "Total successful defensive actions",
                  "Total defensive duels",
                  "Total defensive duels won",
                  "Defensive duels won, %",
                  "Total sliding tackles",
                  "PAdj Sliding tackles",
                  "Total interceptions",
                  "PAdj Interceptions",
                  "Total shots blocked",
                  "Goals",
                  "xG",
                  "Total successful attacking actions",
                  "NPxG",
                  "Non-penalty goals",
                  "Head goals",
                  "Shots",
        #          "Shots",
                  "Total shots on target",
                  "Shots on target, %",
                  "Goal conversion, %",
                  "PENxG",
                  "Converted penalties",
                  "Total offensive duels",
                  "Total offensive duels won",
                  "Offensive duels won, %",
                  "Total touches in box",
                  "Assists",
                  "xA",
                  "Total crosses",
                  "Total crosses completed",
                  "Accurate crosses, %",
                  "Accurate crosses from left flank, %",
                  "Accurate crosses from right flank, %",
                  "Total crosses to goalie box",
                  "Total shot assists",
                  "Total second assists",
                  "Total third assists",
                  "Total smart passes",
                  "Total smart passes completed",
                  "Accurate smart passes, %",
                  "Total key passes",
                  "Total passes to penalty area",
                  "Total passes to penalty area completed",
                  "Accurate passes to penalty area, %",
                  "Total through passes",
                  "Total through passes completed",
                  "Accurate through passes, %",
                  "Total deep completions",
                  "Total deep completed crosses",
                  "Total passes",
                  "Total passes completed",
                  "Accurate passes, %",
                  "Total forward passes",
                  "Total forward passes completed",
                  "Accurate forward passes, %",
                  "Total back passes",
                  "Total back passes completed",
                  "Accurate back passes, %",
                  "Total lateral passes",
                  "Total lateral passes completed",
                  "Accurate lateral passes, %",
                  "Total short / medium passes",
                  "Total short / medium passes completed",
                  "Accurate short / medium passes, %",
                  "Total long passes",
                  "Total long passes completed",
                  "Accurate long passes, %",
                  "Average pass length, m",
                  "Average long pass length, m",
                  "Total passes to final third",
                  "Total passes to final third completed",
                  "Accurate passes to final third, %",
                  "Total progressive passes",
                  "Total progressive passes completed",
                  "Accurate progressive passes, %",
                  "Total duels",
                  "Total duels won",
                  "Duels won, %",
                  "Total aerial duels",
                  "Total aerial duels won",
                  "Aerial duels won, %",
                  "Total fouls",
                  "Total dribbles",
                  "Total successful dribbles",
                  "Successful dribbles, %",
                  "Total progressive runs",
                  "Total accelerations",
                  "Total received passes",
                  "Total received long passes",
                  "Total fouls suffered",
                  "Conceded goals",
                  "Shots against",
                  "Clean sheets",
                  "Save rate, %",
                  "xG against",
                  "Prevented goals",
                  "Direct free kicks on target, %",
                  "Penalties taken",
                  "Penalty conversion, %",
                  "Yellow cards",
                  "Red cards"]]
    
##################################################################################################################################################################################

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 3, .1, 1.3, .1))

with row0_1:
    st.header('Ligas Conmebol  2022  -  Data Explorer')

st.markdown("""---""")    
st.dataframe(df)      

    
space0, space1, space2, space3 = st.columns((1.5, 0.42, 0.5, 0.44))

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(255, 0, 70);
}
div.stButton > button:hover {
    background-color: #FFF;
    color:#ff0046;
    }    

</style>""", unsafe_allow_html=True)

with space0:
    see = st.expander('   Más información... ')
    with see:
        st.markdown("---")
        st.text("Nombre : " + str(leaguesel) + 
                "\nPaís : Argentina\nTemporada : 2022\nNúmero jugadores : " + str(df["Player"].count()) + "\nMáximo minutos : " + str(df["Minutes played"].max()) + "")

with space1:
    df_xlsx1 = to_excel(df)
    st.download_button(label='Download File',
                        data=df_xlsx1,
                        file_name= 'Argentina2022_AllMetricsCalculated.xlsx')
with space2:
    st.download_button(label='Download CSV File',
                        data=df_xlsx1,
                        file_name= 'Argentina2022_AllMetricsCalculated.xlsx')
    
with space3:
    st.button(label='Metrics Glossary')   

st.markdown("""---""")

        
# ##################################################################################################################################################################################



# ##################################################################################################################################################################################
# #st.write(df.style.format("{:.2}"))
# #st.dataframe(df.style.format(formatter="{:.2f}"))
# st.dataframe(df.style.format({"E": "{:.5f}"}))
# #df[]


# # def convert_df(df):
# #     # IMPORTANT: Cache the conversion to prevent computation on every rerun
# #     return df.to_excel("MetricasOfensivas.xlsx").encode('utf-8')

# # exc = convert_df(df)




spacer1, spacer2, spacer3, spacer4, spacer5 = st.columns((1, 1, 1, 1, 1))
# #spacer6 = st.columns(5)

with spacer1:
    btn1 = st.button('Métricas Ofensivas', key=1)
with spacer2:
    btn2 = st.button('Métricas Creación', key=2)
with spacer3:
    btn3 = st.button('Métricas Distribución', key=3)
with spacer4:
    btn4 = st.button('Métricas Posesión', key=4)
with spacer5:
    btn5 = st.button('Métricas Defensivas', key=5)    
    
if btn1:
    if dfsel == 'Normalizado':

        df = df[['Player','Team', 'Position', 'Age', '90s',
                  'Successful attacking actions per 90', 'Offensive duels per 90', 'Offensive duels won per 90', 'Touches in box per 90',
                  'Goals per 90', 'Non-penalty goals per 90','Head goals per 90', 'Shots per 90', 'Shots on target per 90','xG per 90', 'NPxG per 90']]
    else:
        
        df = df[['Player','Team', 'Position', 'Age', '90s',
                'Total successful attacking actions', 'Total offensive duels', 'Total offensive duels won', 'Offensive duels won, %', 'Total touches in box',
                'Goals', 'Non-penalty goals', 'Head goals', 'Shots', 'Total shots on target', 'Shots on target, %', 'Goal conversion, %',
                'xG', 'NPxG', 'PENxG', 'Converted penalties']]
        
    st.title('Métricas Ofensivas')
    st.markdown("""---""")
    st.dataframe(df)
    df_xlsx = to_excel(df)
    st.download_button(label='Download File',
                        data=df_xlsx ,
                        file_name= 'MetricasOfensivas.xlsx')

if btn2:
    if dfsel == 'Normalizado':

        df = df[['Player','Team', 'Position', 'Age', '90s',
                  'Assists per 90', 'Second assists per 90', 'Third assists per 90', 'Shot assists per 90', 'Key passes per 90', 'xA per 90',
                  'Crosses per 90', 'Crosses completed per 90', 'Crosses to goalie box per 90', 'Crosses from left flank per 90', 'Crosses from right flank per 90',
                  'Passes to penalty area per 90', 'Passes to penalty area completed per 90', 'Through passes per 90', 'Through passes completed per 90',
                  'Smart passes per 90', 'Smart passes completed per 90', 'Deep completions per 90', 'Deep completed crosses per 90']]
    else:
        
        df = df[['Player', 'Team', 'Position', 'Age', '90s',
                  'Assists', 'Total second assists', 'Total third assists', 'Total shot assists', 'Total key passes', 'xA',
                  'Total crosses', 'Total crosses completed', 'Accurate crosses, %', 'Total crosses to goalie box', 'Accurate crosses from left flank, %', 'Accurate crosses from right flank, %',
                  'Total passes to penalty area', 'Total passes to penalty area completed', 'Accurate passes to penalty area, %', 'Total through passes', 'Total through passes completed', 'Accurate through passes, %',
                  'Total smart passes', 'Total smart passes completed', 'Accurate smart passes, %', 'Total deep completions', 'Total deep completed crosses']]
        
    st.title('Métricas Creación')
    st.markdown("""---""")
    st.dataframe(df)
    df_xlsx = to_excel(df)
    st.download_button(label='Download File',
                        data=df_xlsx ,
                        file_name= 'MetricasCreacion.xlsx')

    
if btn3:
    if dfsel == 'Normalizado':

        df = df[['Player', 'Team', 'Position', 'Age', '90s', 
                  'Passes per 90', 'Passes completed per 90', 'Forward passes per 90', 'Forward passes completed per 90', 'Back passes per 90', 'Back passes completed per 90', 'Lateral passes per 90', 'Lateral passes completed per 90',
                  'Short / medium passes per 90', 'Short / medium passes completed per 90', 'Long passes per 90', 'Long passes completed per 90', 
                  'Passes to final third per 90', 'Passes to final third completed per 90', 'Progressive passes per 90', 'Progressive passes completed per 90']]
        
    else:
        
        df = df[['Player', 'Team', 'Position', 'Age', '90s',
                  'Total passes', 'Total passes completed', 'Accurate passes, %', 'Total forward passes', 'Total forward passes completed', 'Accurate forward passes, %', 'Total back passes', 'Total back passes completed', 'Accurate back passes, %',
                  'Total lateral passes', 'Total lateral passes completed', 'Accurate lateral passes, %',
                  'Total short / medium passes', 'Total short / medium passes completed', 'Accurate short / medium passes, %', 'Total long passes', 'Total long passes completed', 'Accurate long passes, %',
                  'Average pass length, m', 'Average long pass length, m', 'Total passes to final third', 'Total passes to final third completed', 'Accurate passes to final third, %', 
                  'Total progressive passes', 'Total progressive passes completed', 'Accurate progressive passes, %']]
                
        
    st.title('Métricas Distribución')
    st.markdown("""---""")
    st.dataframe(df)
    df_xlsx = to_excel(df)
    st.download_button(label='Download File',
                        data=df_xlsx ,
                        file_name= 'MetricasDistribucion.xlsx')
   

if btn4:
    df = df[['Player','Team', 'Position', 'Age', '90s', 'Duels per 90', 'Duels won per 90', 'Aerial duels per 90', 'Aerial duels won per 90', 'Dribbles per 90', 'Successful dribbles per 90', 'Total progressive runs', 'Progressive runs per 90']]
    st.title('Métricas Posesión')
    st.markdown("""---""")
    st.dataframe(df)
    df_xlsx = to_excel(df)
    st.download_button(label='Download File',
                        data=df_xlsx ,
                        file_name= 'MetricasPosesion.xlsx')

if btn5:
    df = df[['Player','Team', 'Position', 'Age', '90s', 'Successful defensive actions per 90', 'Defensive duels per 90', 'Defensive duels won per 90', 'Sliding tackles per 90', 'PAdj Sliding tackles', 'Shots blocked per 90', 'Interceptions per 90', 'PAdj Interceptions',]]
    st.title('Métricas Defensivas')
    st.markdown("""---""")
    st.dataframe(df)    
    df_xlsx = to_excel(df)
    st.download_button(label='Download File',
                        data=df_xlsx ,
                        file_name= 'MetricasDefensivas.xlsx')

    

# # with spacer1:    
# #     if st.button('Métricas Ofensivas'):
# #         df = df[['Player','Team', 'Position', 'Age', '90s','Goals', 'Goals per 90', 'xG', 'xG per 90', 'NPxG per 90', 'Shots per 90', 'Shots on target per 90','Successful attacking actions per 90']]
# #         #st.dataframe(df)

# # with spacer2:    
# #     if st.button('Métricas Creación'):
# #         df = df[['Player','Team', 'Position', 'Age', '90s','Assists', 'Assists per 90', 'xA', 'xA per 90', 'Shot assists per 90', 'Key passes per 90', 'Crosses per 90', 'Crosses completed per 90', 'Crosses to goalie box per 90']]
# #         #st.dataframe(df)    
# #         st.title('Métricas de Creación')
        
# # with spacer3:    
# #     if st.button('Métricas Distribución'):
# #         df = df[['Player','Team', 'Position', 'Age', '90s','Goals', 'Goals per 90', 'xG', 'xG per 90']]
# #         #st.dataframe(df)
# #         st.title('Métricas de Distribución')

# # with spacer4:    
# #     if st.button('Métricas Posesión'):
# #         df = df[['Player','Team', 'Position', 'Age', '90s', 'Duels per 90', 'Duels won per 90', 'Aerial duels per 90', 'Aerial duels won per 90', 'Dribbles per 90', 'Successful dribbles per 90', 'Total progressive runs', 'Progressive runs per 90']]
# #         #st.dataframe(df)    

# # with spacer5:    
# #     if st.button('Métricas Defensivas'):
# #         df = df[['Player','Team', 'Position', 'Age', '90s', 'Successful defensive actions per 90', 'Defensive duels per 90', 'Defensive duels won per 90', 'Sliding tackles per 90', 'PAdj Sliding tackles', 'Shots blocked per 90', 'Interceptions per 90', 'PAdj Interceptions',]]
# #         #st.dataframe(df)
# #st.dataframe(df)
 
# #df = df


# # dfx[1] = dfx[1].replace(['None'],['N'])
# # dfx[1] = dfx[1].replace(['LDMF', 'DMF', 'RDMF'],['CEM','CEM','CEM'])
# # dfx[1] = dfx[1].replace(['LCMF', 'CMF', 'RCMF'],['MED','MED','MED'])
# # dfx[1] = dfx[1].replace(['LAMF', 'AMF', 'RAMF'],['VOL','VOL','VOL'])
# # dfx[1] = dfx[1].replace(['RCB', 'CB', 'LCB', 'GK'],['DEF', 'DEF', 'DEF', 'POR'])
# # dfx[1] = dfx[1].replace(['RB', 'RWB', 'LB', 'LWB'],['LAT', 'LAT', 'LAT', 'LAT'])
# # dfx[1] = dfx[1].replace(['RW', 'LW'],['BAN', 'BAN'])
# # dfx[1] = dfx[1].replace(['RWF', 'LWF'],['EXT', 'EXT'])
# # dfx[1] = dfx[1].replace(['CF'],['DEL'])

# # dfx[2] = dfx[2].replace(['LDMF', 'DMF', 'RDMF'],['CEM','CEM','CEM'])
# # dfx[2] = dfx[2].replace(['LCMF', 'CMF', 'RCMF'],['MED','MED','MED'])
# # dfx[2] = dfx[2].replace(['LAMF', 'AMF', 'RAMF'],['VOL','VOL','VOL'])
# # dfx[2] = dfx[2].replace(['RCB', 'CB', 'LCB', 'GK'],['DEF', 'DEF', 'DEF', 'POR'])
# # dfx[2] = dfx[2].replace(['RB', 'RWB', 'LB', 'LWB'],['LAT', 'LAT', 'LAT', 'LAT'])
# # dfx[2] = dfx[2].replace(['RW', 'LW'],['BAN', 'BAN'])
# # dfx[2] = dfx[2].replace(['RWF', 'LWF'],['EXT', 'EXT'])
# # dfx[2] = dfx[2].replace(['CF'],['DEL']) 

