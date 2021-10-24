import phonenumbers 

# service provider of required phone number 
from phonenumbers import carrier 
# country location to that phone number 
from phonenumbers import geocoder 
#Country timezone
from phonenumbers import timezone


ph_no = input("Enter phone no. with country code:  ")
c_code = phonenumbers.parse(ph_no) 
tt_zone = phonenumbers.parse(ph_no, "en") 
service_provider = phonenumbers.parse(ph_no) 

 


print("\nService Provider: ", end="")
print(carrier.name_for_number(service_provider, 'en'))

print("\nCountry: ", end="")
print(geocoder.description_for_number(c_code,  'en'))

print("\nTimeZone: ", end="")  
print(timezone.time_zones_for_number(tt_zone))


