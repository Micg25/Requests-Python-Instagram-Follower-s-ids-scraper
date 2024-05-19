import requests
import time
ig_id=" " #put the instagram ID of the profile you want to scrape from

cookie = {
    'csrftoken':' ',#add value
    'datr': ' ',#add value
    'ds_user_id': ' ',#add value
    'ig_did':' ',#add value
    'mid':' ',#add value
    'ps_l':' ',#add value
    'ps_n':' ',#add value
    'rur':'" "',#add value
    'sessionid':' ',#add value
    'shbid':'" "',#add value
    'shbts':'" "',#add value
    'wd':'',#add value
}

headerscURL = {
    #put here the values of your own header request

    #like this:

    #"User-Agent":
    #"Accept":
    #"Accept-Language":
    #"Accept-Encoding":
    #"X-CSRFToken":
    #"X-IG-App-ID":
    #"X-ASBD-ID":
    #"X-IG-WWW-Claim":
    #"X-Requested-With":
    #"Referer":
    #"Cookie":
    #"Connection":
    #"Sec-Fetch-Dest":
    #"Sec-Fetch-Mode":
    #"Sec-Fetch-Site":
}
params = { #api call's params
    'count': 12,
    'search_surface': 'follow_list_page',
    'max_id': '0'
}

# Creazione della sessione
session = requests.Session()
session.cookies.update(cookie)
time.sleep(2)
resp=session.get('https://www.instagram.com/')
print(resp.status_code)
print(resp.url)
api =f'https://www.instagram.com/api/v1/friendships/{ig_id}/followers/' #endpoint API
maxid=None
user_ids=set()
with open("response.txt","w", encoding='utf-8') as file: #saving all fetch response in a .txt file
    for i in range (2):
        print("Starting to fetch the set number:", i+1)
        chunk=1
        params['max_id'] = '0' #reset the max_id between fetch cycles 
        while True:
            time.sleep(3)
            pivot=len(user_ids)

            print("chunk number", chunk," set number: ", i+1)
            resp=session.get(api, headers=headerscURL,params=params) #api call

            file.write(str(resp.text))
            file.write("\n")
            print(resp.status_code)

            data = resp.json()
            for user in data['users']:
                user_ids.add(int(user['pk_id'])) #adding ids fetched in a set
            print("current length:", len(user_ids))

            if(i==0): #in the first chunk we take the max_id value in a different way than the second, in order to take more followers, in order to take more followers combining the two iterations 
                    maxid =  len(user_ids)
                    params['max_id'] = maxid
            if(i==1): #in the second chunk we take the max_id value in a different way than the first, in order to take more followers combining the two iterations
                try:
                    maxid = data['next_max_id']
                    params['max_id'] = maxid
                except:
                    break

            print("max_id: ",maxid)
            print("Chunk ",chunk," taken")
            chunk+=1
            if(pivot==len(user_ids) and i==0 ): #break condition, if the current chunk and the last chunk leght is the same there are no more followers to fetch
                break
        
with open("users_id.txt","w") as file:
    for id in user_ids:
        file.write(str(id)+"\n") #saving all ids in a .txt file

    
