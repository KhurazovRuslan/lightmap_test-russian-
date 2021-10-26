# imports
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# функция преобразования дат событий
def unix_to_date(df,columns,units='s'):
    """
    Меняет unix timestamp в читаемую дату
    
    df - датафрейм для преобразований
    column - список названий колонок для преобразований
    units - str, шаг преобразований, секунды по умолчанию
    
    Возвращает исходный датафрейм с преобразованными колонками с датами
    """
    
    for column in columns:
        df[column] = pd.to_datetime(df[column], unit=units)
    
    return df


# функция для создания нового датафрейма из исходных данных
# будет показывать количество событий 'install', количество событий 'login' на следующий день
# после события 'install'
# и удержание первого дня для пользователей, разбитых по дате установки

def d1_retention(df):
    """
    Строит датафрейм с количестовм событий install и количеством событий login на следующий день
    
    df - датафрейм для работы с колонками:
        'event_timestamp' - дата и время события
        'event_name' - событие install или login
        'player_id' - id пользователя
    
    Возвращает датафрейм с количеством событий install, login на следующий день и 
    % удержания первого дня по дням
    """
    
    # преобразуем время события из unix timestamp в читаемую дату
    df = unix_to_date(df,['event_timestamp'])
    
    # определяем количество пользователей, установивших приложение, по дням
    cohorts = df[df['event_name']=='install'].groupby(df['event_timestamp'].dt.date)['player_id'].agg(['count'])
    cohorts.columns = ['num_installs']
    
    # количество пользователей с событием 'login' на следующий после установки день
    next_day_logins = []
    
    for day in sorted(df['event_timestamp'].dt.day.unique()):
        
        cohort = df[(df['event_name']=='install')&(df['event_timestamp'].dt.day==day)]
        
        next_day_login_df = df[(df['event_name']=='login')&(df['event_timestamp'].dt.day==day+1)\
                        &(df['player_id'].isin(cohort['player_id']))]
        
        if len(next_day_login_df)==0:
            next_day_logins.append(np.nan)
        else:
            next_day_logins.append(len(next_day_login_df))
            
    cohorts['next_day_logins'] = next_day_logins
    
    cohorts['d1_retention (%)'] = round(cohorts['next_day_logins']/cohorts['num_installs']*100)
    
    return cohorts

# функция для построения графиков
def plot_lines(x_axes,y_axes,labels,line_style=['g-'],markers=['o'],figsize=(10,6),x_rotation=True):

    """
    Строит график с заданными параметрами

    x_axes - список, данные для оси х
    y_axes - список, данные для оси y
    labels - список, пояснения к графику(-ам)
    line_style - список, вид и цвет графика, по умолчанию зеленая линия (один график)
    markers - списко, вид и цвет маркеров, по умолчанию точка (один график)
    figsize - (длина графика, высота графика), измеряется в дюймах
    x_rotation - если True, то наклон надписей оси х 45 градусов

    Возвращает график по заданным параметрам
    """

    plot = plt.figure(figsize=figsize)

    for x_axe,y_axe,label,line,marker in zip(x_axes,y_axes,labels,line_style,markers):

        plt.plot(x_axe,y_axe,line, marker=marker, label=label)

    for pos in ['right', 'top', 'bottom', 'left']:
        plt.gca().spines[pos].set_visible(False)

    if x_rotation:
        plt.xticks(rotation=45)
        
    plt.tick_params(axis='both',which='both',bottom=False,left=False)
    plt.legend()

    return plot

