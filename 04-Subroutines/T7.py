facebook = input("Do you have a Facebook account? (True/False): ").lower() == 'true'
twitter = input("Do you have a Twitter account? (True/False): ").lower() == 'true'
instagram = input("Do you have an Instagram account? (True/False): ").lower() == 'true'
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("The person can be an influencer")
else:
    print("The person is a bad influencer")