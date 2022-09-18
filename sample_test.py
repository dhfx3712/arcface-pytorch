import pandas as pd

df = pd.read_csv('/Users/admin/data/peopleface/face/test.txt',sep=' ',names=['path','name'])
print(df.head())

df1 = df.sample(frac=1,random_state=1,ignore_index=True)
print (df1.head())

# df_merge = pd.concat([df, df1], axis=1)
df_merge =  pd.merge(df, df1,how='left', left_index=True, right_index=True)
print (df_merge.head())

df_merge["target"] =df_merge.apply(lambda x :1 if x['name_x']==x['name_y'] else 0,axis = 1)

print (df_merge.head())


df_merge_1 = df_merge[df_merge["target"]==1]
print (df_merge_1.head(),len(df_merge_1))
df_merge_0 = df_merge[df_merge["target"]==0][0:40]

tmp = pd.concat([df_merge_1,df_merge_0],axis=0)[["path_x","path_y","target"]]
print (tmp)

tmp.to_csv('./sample_test.csv',index=False,header=None,sep=' ')