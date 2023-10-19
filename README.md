# FB_Ads_Data_Fetcher
   The FB_Ads_Data_Fetcher is a Python script that uses Facebook Graph API to fetch,validate and store data from Facebook Ad Account about its Ads and Campaigns.The FB_Ads_Data_Fetcher repository have data_fetch_store.py which is our main file comprises the entire script of the FB_Ads_Data_Fetcher.

## Installation instructions
  After downloading the repository install the following libraries:
                                * requests
                                * ratelimit
                                * jsonschema
  * To retrieve data from a Facebook Ad Account, we use Facebook Graph API and we need access token of the account, to access the data of the account.So, to get the access token follow the procedure in the following website **(login with email attached with your ad account to access the ad account)**.
    
 [https://elfsight.com/blog/how-to-get -facebook-access-token/](url)
 
 * After getting Access Token, Know API version and Ad Account ID
   
 **To find Ad Account ID, follow the link**
[https://www.facebook.com/business/help/1492627900875762](url)
## Configuration details
  After having your access token, Ad Account ID and API version. Run the script on your python compiler.
  * Enter your access token
  * Enter your Ad Accound ID
  * Enter your API version
    
    ![Demo output of Entering credentials](user_input.png)
    
After entering the above details request will be made to the API. Afer successfull API response, predefined data will be fetched *provided the given credentials are correct*
After this, the ouput terminal will ask for file location and file name.
  * Enter the folder path where you want to create the file in which the retrieved data will be stored.
  * Enter the name of the file with extension *.json*.
    
    ![Demo output of entering folder path and file name](file_location.png)
    
After the successfull storing of the data in that file. Output will confirm the successfull execution through text.

Now the file you entered will be created in the entered folder with the fetched data.
You can now open and see the data.
You can also see the execution and error details in the *LogRecorder.log* file which will be created in the current directory where the script is running.
## Usage guidelines
* ***Do not try to make more than 200 API calls per hour***
* ***Access token will be expired every hour.So, you should re-generate access tokens for every hour***
* ***Make sure the file location is accessible by the directory in which the script runs***
