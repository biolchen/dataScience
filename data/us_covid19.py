us_county=pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv',na_values=0)
df= us_county.dropna(subset=['fips'])
df=df.astype({'fips': 'int32'})
df=df[df.date=='2020-04-06']
df.head()
df= df[['state','county','fips','cases']]
unem=pd.read_csv('https://raw.githubusercontent.com/biolchen/dataScience/master/data/unemployment.tsv', sep='\t')
unem
df=pd.merge(unem,df,left_on='id',right_on='fips')[['id','cases','county','state']]
df[df.state=='California']
df
df.to_csv('/Users/liangchen/Downloads/dataScience/data/us_counties.csv',index=False, sep="\t")
unem.dtypes

pd.read_json('/Users/liangchen/Downloads/dataScience/data/a.json')
