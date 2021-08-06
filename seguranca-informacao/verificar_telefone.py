import phonenumbers
from phonenumbers import geocoder

if __name__ == '__main__':
   phone = input('Digite o telefone no formato +55114444444: ')
   phone_number = phonenumbers.parse(phone)
    
   print(geocoder.description_for_number(phone_number, 'pt'))
