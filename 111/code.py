import statistics
from cv2 import mean
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random

df=pd.read_csv('medium_data.csv')
data=df['reading_time'].to_list()

population_mean=statistics.mean(data)
population_stdev=statistics.stdev(data)

def random_set_of_means(counter):
    dataset=[]
    for i in range(0,counter):
        index=random.randint(0,len(data)-1)
        value=data[index]              
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_means(30)
    mean_list.append(set_of_mean)
    
mean=statistics.mean(mean_list)
std_dev=statistics.stdev(mean_list)


std_dev_1_start,std_dev_1_end=population_mean-population_stdev,population_mean+population_stdev
std_dev_2_start,std_dev_2_end=population_mean-(2*population_stdev),population_mean+(2*population_stdev)
std_dev_3_start,Std_dev_3_end=population_mean-(3*population_stdev),population_mean+(2*population_stdev)

df=pd.read_csv('sample_2.csv')
data_2=df['reading_time'].to_list()  

mean_of_sample_2=statistics.mean(data_2)

fig = ff.create_distplot([mean_list], ["reading time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
fig.add_trace(go.Scatter(x=[mean_of_sample_2,mean_of_sample_2],y=[0,0.17],mode='lines',name='Mean of sample 2'))
fig.add_trace(go.Scatter(x=[std_dev_1_end,std_dev_1_end],y=[0,0.17],mode='lines',name='Std dev 1 end'))
fig.add_trace(go.Scatter(x=[std_dev_2_end,std_dev_2_end],y=[0,0.17],mode='lines',name='std dev 2 end'))
fig.add_trace(go.Scatter(x=[Std_dev_3_end,Std_dev_3_end],y=[0,0.17],mode='lines',name='Std dev 3 end'))
fig.show()

z_score=(mean-mean_of_sample_2)/std_dev
print(f'The z score of the given dataset is-{z_score}') 
