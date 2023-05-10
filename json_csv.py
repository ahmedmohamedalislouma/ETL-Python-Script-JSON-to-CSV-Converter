import argparse
import json
import pandas as pd
import time

parser = argparse.ArgumentParser()

parser.add_argument("jsonPath", help = "Enter json path to be converted to csv")


parser.add_argument("-u", action="store_true", dest="unix", default=False, help="keep unix format")


args = parser.parse_args()




if args.unix:
    st = time.time()
    
    records = [json.loads(line) for line in open(args.jsonPath)]

    records_df=pd.DataFrame(records)
    records_df['web_browser']=records_df['a'].str.extract(r'(^[A-Z][^\s\(]*)').fillna('Unspecified')
    records_df['operating_sys']=records_df['a'].str.extract(r'([\(][^)]*)').replace(r'\(','',regex=True).fillna('Unspecified')
    records_df['from_url']=records_df['r'].str.split('/').str[2].fillna('Unspecified')
    records_df['to_url']=records_df['u'].str.split('/').str[2].fillna('Unspecified')
    records_df['longitude'] = records_df['ll'].str.get(0).fillna('Unspecified')
    records_df['latitude'] = records_df['ll'].str.get(1).fillna('Unspecified')

    records_df.drop(columns=['nk', 'c','gr','g','al','hh','h','l','ll','a','u','r']
                             ,inplace=True)

    records_df.rename(
      
        columns={ "cy":"city","tz":"time_zone",'hc':'time_out','t':'time_in'},
        inplace=True
    )
    records_df['time_zone']=records_df['time_zone'].replace('','Unspecified')
    records_df=records_df[[ 'web_browser','operating_sys', 'from_url','to_url','city','time_zone','time_in','time_out','longitude','latitude']]

    a=f'{args.jsonPath}'.replace('json','csv')
    s=f'{args.jsonPath}'.replace('json','')
    records_df.to_csv(f'{s}csv')
    
    count_row = records_df.shape[0]
    
    
    et = time.time()
    elapsed_time = et - st
    
    print('Number of rows:', count_row ,'row','  File Path:',a)
    print('Execution time:', elapsed_time, 'seconds')
    
else: 
    st = time.time()
    

    records = [json.loads(line) for line in open(args.jsonPath)]
    # Print the first occurance
    records_df=pd.DataFrame(records)
    records_df['web_browser']=records_df['a'].str.extract(r'(^[A-Z][^\s\(]*)').fillna('Unspecified')
    records_df['operating_sys']=records_df['a'].str.extract(r'([\(][^)]*)').replace(r'\(','',regex=True).fillna('Unspecified')
    records_df['from_url']=records_df['r'].str.split('/').str[2].fillna('Unspecified')
    records_df['to_url']=records_df['u'].str.split('/').str[2].fillna('Unspecified')

    records_df['city']=records_df['cy'].fillna('Unspecified')
    records_df['time_zone']=records_df['tz'].replace('','Unspecified')

    records_df['longitude'] = records_df['ll'].str.get(0).fillna('Unspecified')
    records_df['latitude'] = records_df['ll'].str.get(1).fillna('Unspecified')
    records_df['time_out'] = pd.to_datetime(records_df['hc'],unit='s',errors='coerce').fillna('Unspecified')
    records_df['time_in'] = pd.to_datetime(records_df['t'],unit='s').fillna('Unspecified')
    records_df.drop(columns=['nk', 'c','gr','g','al','hh','h','l','ll','a','u','r','t','hc','tz','cy']
                             ,inplace=True)

    records_df=records_df[[ 'web_browser','operating_sys', 'from_url','to_url','city','time_zone','time_in','time_out','longitude','latitude']]
    
    a=f'{args.jsonPath}'.replace('json','csv')
    s=f'{args.jsonPath}'.replace('json','')
    records_df.to_csv(f'{s}csv')
    
    count_row = records_df.shape[0]
    
    
    et = time.time()
    elapsed_time = et - st
    
    print('Number of rows:', count_row ,'row','  File Path:',a)
    print('Execution time:', elapsed_time, 'seconds')
