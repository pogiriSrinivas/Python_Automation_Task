import requests


# endpoint_url = 'https://back.app.match2one.com/admin/v1/companies/report-lite?paymentScheduleApproximate=true&paymentScheduleEndDate=2024-05-13&withBalances=true&withCampaignBalances=true&companyId=CO-KTSW8ZJ4&status=active&limit=100&from=7'
endpoint_url = 'https://api.app.match2one.com/v2/reports/public'

def btoken():
    url = "https://back.app.match2one.com/v1/login"

    data = {
        "email": "sambasiva.gangumolu@mediamint.com",
        "password": "@Shiva@11216@"
    }

    response = requests.post(url, json=data)

    print("Status Code:", response.status_code)
    print("JSON Response:", response.json())

    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        # Extract the bearer token from the JSON response
        response_data = response.json()
        bearer_token = response_data.get("token").split(" ")[1]  # Extract the token value after 'Bearer '
        return "Bearer " + bearer_token


def finixio_name_extractor():
    bt = btoken()
    names = []
    # Print the bearer token
    print("Bearer Token:", bt)

    try:
        # Send a GET request to the endpoint with the Authorization header
        response = requests.get(endpoint_url, headers={'Authorization': bt})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract and print the response headers
            print("Response Headers:")
            for header, value in response.headers.items():
                print(f"{header}: {value}")

            # Extract and print the response data
            data = response.json()
            print("\nResponse Data:")
            print(data)

            for item in data.get('data', []):
                name = item.get('name')
                if name:
                    names.append(name)
                    print(name)


        else:
            print(f'Failed to fetch data. Status code: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred while making the request: {e}')

    return names

finixio_name_extractor()

