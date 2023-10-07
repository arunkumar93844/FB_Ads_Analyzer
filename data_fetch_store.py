import requests
import json
import os

def user_input():
    access_token = input('Enter your access token here: ')
    ad_account_id = input('Enter your ad account id here: ')
    api_version = input('Enter your api version here: ')
    folder_path = input('Enter your folder path here (preferably copy and paste the folder path): ')
    file_name = input('Enter your filename with its .extension like "mynewpython.py" here: ')    return access_token,ad_account_id,api_version,folder_path,file_name
    return access_token, ad_account_id, api_version, folder_path, file_name

def basic_data_fetch(access_token,ad_account_id,api_version):
    graph_api_url = f'https://graph.facebook.com/v{api_version}/{ad_account_id}'
    feilds={'access_token':access_token,
            'ad_accounts',
            'customaudiences',
            'ads{id,name,creative,insights,targeting}',
            'campaigns{id,name,start_time,end_time,creative,insights,targeting}'
            }
    response_raw = requests.get(url= graph_api_url, params= feilds)
    return response_raw

def data_process_store(response_raw,folder_path,file_name):
    response_json_raw = response_raw.json()
    response_json =json.dumps(response_json_raw,indent=4)
    with open(f'{folder_path}\{file_name}','a+') as file:
        json.dump(response_json,file)
    
            
def main(response_raw):
    
    access_token, ad_account_id, api_version, folder_path, file_name= user_input()
    basic_data_fetch(access_token,ad_account_id,api_version)
    if response_raw.status_code == 200:
        data_process_store(response_raw,folder_path,file_name)
    else:
        print('Request failed')
                
main()

    




    

