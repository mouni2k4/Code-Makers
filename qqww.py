import requests
import requests



# Replace 'your_api_key' with your actual Hunter API key
API_KEY = '9cf2304ba984cd374e30f19fbce5c3457b2007a3'

# Function to search for social media profiles associated with an email address
def find_social_media_profiles(email, first_name, last_name, company, domain):
    url = f"https://api.hunter.io/v2/email-finder?email={email}&first_name={first_name}&last_name={last_name}&company={company}&domain={domain}&api_key={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            social_profiles = data.get('data', {}).get('profiles', [])
            return social_profiles
        else:
            error_message = data.get('errors', [{}])[0].get('details', 'Unknown error')
            return [f"Error: {error_message}"]
    except Exception as e:
        return [f"Error: {str(e)}"]

# User input
user_email = input("Enter an email address: ")
user_first_name = input("Enter the first name associated with the email address: ")
user_last_name = input("Enter the last name associated with the email address: ")
user_company = input("Enter the associated company: ")
user_domain = input("Enter the associated domain: ")

# Search for social media profiles
social_media_profiles = find_social_media_profiles(user_email, user_first_name, user_last_name, user_company, user_domain)

if social_media_profiles:
    print("Social Media Profiles:")
    for profile in social_media_profiles:
        print(profile)
else:
    print("No social media profiles found for the provided email address.")
