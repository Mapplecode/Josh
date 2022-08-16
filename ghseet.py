import requests,json
sheet_id = "1H9KPCUPRCwVEzy0S7dsJ9cRqSG9Ot7SwDTdJq_j5tpU"
def get_token():
    url = "https://accounts.google.com/o/oauth2/token?refresh_token=1//04Vp7Cvcx5GllCgYIARAAGAQSNwF-L9IrSfTQo3vrQZMvg903GRXIwTtPNxBmVCYaR8LM1MVgdEwS3MPjCPNNuYbOx1WCUlRUQKg&redirect_uri=https://developers.google.com/oauthplayground&client_id=319825298674-b4jv0vm504ic4fpt7ub9oc1nms7qpofn.apps.googleusercontent.com&client_secret=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&grant_type=refresh_token"
    payload={}
    headers = {
    'Cookie': 'NID=511=Csaq4q6a5RQZoqG-fjKdR1dq9_A-5hLLb61LS9GKOFMJrfs_7hyf5bUviDd8K2AsBF6vhZM65jDRYTNKNI9ZV7F9G35kZgfkcHh9JMO7AY6gsaX1VdtOgKLs9qv3ilTmEW7ouLQI-AwGrTBWMl_SY2bnxPxEIv_RgcNZ82q2K1E; __Host-GAPS=1:BSgSEG-H0z6z7SwFbrjS2sFmzhHbJA:GWcoiIRwPrRR7-XN'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    store =json.loads(response.text)
    access_token = store.get('access_token')
    return access_token

def get_data(get_tokens):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/A2:$W"
    payload={}
    headers = {
    'Authorization': f'Bearer {get_tokens}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    store =json.loads(response.text)['values']
    return store


def update_gsheet(get_tokens,temp,sheet_range):
    url = "https://sheets.googleapis.com/v4/spreadsheets/1H9KPCUPRCwVEzy0S7dsJ9cRqSG9Ot7SwDTdJq_j5tpU/values:batchUpdate"
    payload = json.dumps({
    "data": [
        {
        "values": [
            temp
        ],
        "range":sheet_range
        }
    ],
    "valueInputOption": "USER_ENTERED"
    })
    headers = {
    'Authorization': f'Bearer {get_tokens}',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.status_code


def main():
    get_tokens = get_token()
    get_data(get_tokens)
    count = 5
    temp = []
    input_data = {  
        'venue':"Dolphin Tavern",
        "name":"Josh Test, Josh Test2",
        "email":"josh@leadcapitalagency.com,admin@leadcapitalagency.com",
        "LinkedIn Profile":"linkedin.com,linkedin.com", 
        "Title":"President,President",
        "source":"Outbound Research",
        "campaign" :"reviews",
        "Review Link":"https://search.google.com/local/reviews?placeid=ChIJcwcnPBDGxokRkgvUEr-tXwI",
        "Owner":"Derek Pacque",
        "Rating": "XtraHot",
        "Location Link":"https://www.google.com/maps/place/Dolphin Tavern/@39.930577899999996,-75.168071,14z/data=!4m8!1m2!2m1!1sDolphin Tavern!3m4!1s0x89c6c6103c270773:0x25fadbf12d40b92!8m2!3d39.930577899999996!4d-75.168071",
        "Venue Type" :"Night Club",
        "Review Source": "Review Source",
        "City" :"Philadelphia",
        "State":"Pennsylvania",
        "lat" :"39.9305779",
        "Long" :"-75.168071",
        "Country":"US",
        "Phone":"1 215-278-7950",
        "street":"1539 S Broad St",
        "postal": "19147",
        "venuerating":"4"

        }
    if "," in input_data.get("name") and input_data.get("venue") and input_data.get("email") and input_data.get("LinkedIn Profile") and input_data.get("Title") and input_data.get("source") and input_data.get("campaign") and input_data.get("Review Link") and input_data.get("City") and input_data.get("Owner") and input_data.get("Rating") and input_data.get("Location Link") and input_data.get("Venue Type")and input_data.get("State") and input_data.get("lat") and input_data.get("Long") and input_data.get("Country") and input_data.get("Phone") and input_data.get("street") and input_data.get("postal") and input_data.get("venuerating"):
        for i in zip(input_data.get("name").split(','),
            input_data.get("email").split(','),
            input_data.get("LinkedIn Profile").split(','),
            input_data.get("Title").split(','),
            input_data.get("source").split(','),
            input_data.get("campaign").split(','),
            input_data.get("Review Link").split(','),
            input_data.get("Owner").split(','),
            input_data.get("Rating").split(','),
            input_data.get("Location Link").split(','),
            input_data.get("Venue Type").split(','),
            input_data.get("Review Source").split(','),
            input_data.get("City").split(','),
            input_data.get("State").split(','),
            input_data.get("lat").split(','),
            input_data.get("Long").split(','),
            input_data.get("Country").split(','),
            input_data.get("Phone").split(','),
            input_data.get("street").split(','),
            input_data.get("postal").split(','),
            input_data.get("venuerating").split(','),
            input_data.get("venue").split(',')):
            res = {  
            "venue":i[21],
            "name":i[0],
            "email":i[1],
            "LinkedIn Profile":i[2],
            "Title":i[3],
            "source":i[4],
            "campaign":i[5],
            "Review Link":i[6],
            "Owner":i[7],
            "Rating":i[8],
            "Location Link":i[9],
            "Venue Type":i[10],
            "Review Source":i[11],
            "City":i[12],
            "State":i[13],
            "lat":i[14],
            "Long":i[15],
            "Country":i[16],
            "Phone":i[17],
            "street":i[18],
            "postal":i[19],
            "venuerating":i[20],
            }
            temp.append(res)
        print(temp,"=====")
    # else:
    #     input_data = input_data
    #     print(input_data,"===")
       
    for j in temp:
        venue = j.get('venue')
        name = j.get('name')
        email = j.get('email')
        LinkedIn_Profile = j.get('LinkedIn_Profile')
        Title = j.get('Title')
        source = j.get('source')
        campaign = j.get('campaign')
        Review_Link = j.get('Review Link')
        Owner = j.get('Owner')
        Rating = j.get('Rating')
        Location_Link = j.get('Location Link')
        Venue_Type = j.get('Venue Type')
        Review_Source = j.get('Review Source')
        City = j.get('City')
        State = j.get('State')
        lat = j.get('lat')
        Long = j.get('Long')
        Country = j.get('Country')
        Phone = j.get('Phone')
        street = j.get('street')
        postal = j.get('postal')
        venuerating = j.get('venuerating')
        print(venue,"=====")


        payload = [venue,source,campaign,name,'',email,LinkedIn_Profile,Title,Review_Link,Owner,Rating,Location_Link,Venue_Type,Review_Source,City,State,lat,Long,Country,Phone,street,postal,venuerating]
        range = f"Sheet1!A{count}:W{count}"
        # print("Range[]:",range,"Payload:",payload,"===")
        update_gsheet(get_tokens,payload,range)
        count += 1
        

main()


