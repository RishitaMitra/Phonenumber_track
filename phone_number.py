#Phone number tracking with time area and sim company
import phonenumbers

from phonenumbers import timezone, geocoder, carrier

number= input("Enter a valid phone number with country code+__: ")   #in terminal we have to write +91....
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")    #en has written to denote that the output of this should be in english
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(reg)
print(car)
