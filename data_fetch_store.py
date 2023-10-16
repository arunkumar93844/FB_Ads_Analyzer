from ratelimit import limits,sleep_and_retry
import logging
import requests
import json
import os
logging.basicConfig(level=logging.DEBUG,filename="LogRecorder.log", format='%(asctime)s %(message)s\n',filemode='+w')
def user_input():
    logging.info('Gathering user informations: access_Token,ad_Account_Id,api_Version\n')
    access_Token = input('Enter your access token here: ')
    ad_Account_Id = input('Enter your ad account id here: ')
    api_Version = input('Enter your api version here: ')
    logging.info(f"Successfully gathered user informations:\n access_Token = {access_Token}\n ad_Account_Id = {ad_Account_Id}\n api_Version = {api_Version}\n")
    return access_Token,ad_Account_Id,api_Version

@sleep_and_retry
@limits(calls=1,period=18)
def data_fetch(access_token,ad_account_id,api_version):
    graph_api_url = f'https://graph.facebook.com/v{api_version}/{ad_account_id}'
    feilds={'access_token':access_token,
            'ad_accounts',
            'customaudiences',
            'ads{id,name,creative,insights,targeting}',
            'campaigns{id,name,start_time,end_time,creative,insights,targeting}'
            }
    try:
        logging.info("Making API request...\n") 
        response_raw = requests.get(url= graph_api_url, params= feilds)
        response_raw.raise_for_status()
        logging.info("API request was successfull and Informations were fetched...\n")
        return response_raw
    
    except requests.exceptions.RequestException as error:
        logging.exception(f'API request failed:{str(error)}\n Skipping information processing and storing...\n')
        print(f'API request failed:{str(error)}')
        return False

def data_process_store(response):
        if response:
            folder_path = input('Enter your folder path where you file should be created (remove "" while pasting): ')
            file_name = input('Enter your filename with its .extension like "mynewpython.py" here: ')

            try:
                response_json = response.json()
                logging.info("Information is proccessed into JSON format...\n")
                with open(f'{folder_path}\\{file_name}','a+') as file:
                    file.seek(0)
                    json.dump(response_json,file,indent=4)
                    logging.info(f"Information is stored at the location {folder_path}\\{file_name}...\n")
                    file.close()
            except json.JSONDecodeError as error:
                logging.exception(f'Failed to parse JSON response: {str(error)...\n'}
                print(f"Failed to parse JSON response: {str(error)}")
                return True
            except OSError as error:
                logging.exception(f'Information storing failed:{str(error)}...\n')
                print(f'Error Occured:{str(error)}\nEnter the file path correctly.')
                data_process_store(response)
                logging.info(f'Information is successfully stored in {file_name}...\n')
                return True
            
def main():
    logging.info('FB_Manager has started...\n')
    access_token, ad_account_id, api_version= user_input()
    response= data_fetch(access_token,ad_account_id,api_version)
    data_process_store(response)
    logging.info('FB_Manager has stoped...\n\n')
    return True

if __name__=="__main__":
    main()



