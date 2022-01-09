import os
import pandas as pd 


# print the current 
import os
print(os.path.abspath('.'))

#read all the files under a folder
emptyL = []

x = [x for x in allFiles if 'A' in x]
len(x)
for a in x:
    singDf =pd.read_csv(wantDir+a)
    emptyL.append(singDf)
    
b = pd.concat(emptyL)


#pivot_table & plot
d = c.pivot_table(index='Date',columns='which',values='Open',aggfunc='first')
ax = d.reset_index().plot(kind='line',x='Date',figsize=(24,36))
ax.figure.savefig('demo-file.pdf')

df_app_tr = df_app_dedup.groupby('appname_p').agg({'user_id':['size','count']})

#cut
e = pd.DataFrame(d.mean()).reset_index()
e.columns=['which','meanP']
e['seg']=pd.cut(e.meanP, [0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,10000], labels=False)
e.seg.value_counts()

#value_counts&plot
e.seg.value_counts().plot(kind='bar')

#intersect
a = [x for x in useList ]
d[d.columns.intersection(a) ][:10]

#select the null obs
df_app[df_app['appname_p'].isnull()]

#drop duplicates
df_app_dedup = df_app.drop_duplicates(['user_id','appname_p'])


#dic increase and map
dict_ref = dict(zip(df_app_tr.index.values+1,df_app_tr['appname_p']))
dict_ref_r = dict(zip(df_app_tr['appname_p'],df_app_tr.index.values+1))

df_app_dedup['appname_id'] = df_app_dedup['appname_p'].map(dict_ref_r)

#from path readline
path=""
open(path).readline()

import json
rath=""
records =[json.loads(line) for line in open(path)]


by_tz_os = cframe.groupby(['tz',operation_system])
agg_counts= by_tz_os.size().unstack().fillna(0)

#create a dataframe contain a list and then sum the column
a1 =pd.DataFrame({'a':[[1,2,3,4],[1,2,3]]})
a1['a2']= a1.a.apply(lambda x: sum([m for m in x ]))

#flatten the nested list
m = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
m1=sum(m, [])
m1