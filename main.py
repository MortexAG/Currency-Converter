def main():
       import requests
       url_symbols = 'https://api.exchangerate.host/symbols'
       response_symbols = requests.get(url_symbols)
       data_symbols = response_symbols.json()
       symbols = data_symbols['symbols']
      
       
       print("*Any Unidentified Currency Code Will Restart The Process*")
       print("Type Exit To End The Process")      
       print("Enter The Currency You Want to Convert From")
       
       cur_from = input().upper()
       if cur_from in symbols:
          print()
       elif cur_from == "EXIT":
        exit()
       elif cur_from not in symbols or cur_from != "EXIT":
         print("Incorrect Currnecy Code")
         main()
       print("Enter The Currency You Want to Convert to")
       cur_to = input().upper()
       if cur_to in symbols:
          print()
       elif cur_to == "EXIT":
         exit()
       elif cur_to not in symbols or cur_to != "EXIT":
         print("Incorrect Currnecy Code")
         main()
       print("Enter The Amount of {} You Want to Convert".format(cur_from))


       #def check_user_input(amount):
       #    try:
       #       val = float(amount)
       #    except ValueError:
       #      int(amount)
       #      print("PLease Enter An Amount")
       #      main()
       
       amount = input().upper()
       if amount == "EXIT":
         exit()
       #check_user_input(amount)
      
       url = 'https://api.exchangerate.host/convert?from={}&to={}&amount={}'.format(cur_from, cur_to, amount)
       response = requests.get(url)
       data = response.json()
       data_from = data["query"]["from"]
       data_to = data["query"]["to"]
       data_result = data["result"]
       print(amount , data_from,  "=", data_result, data_to)

       #print(data)
                     
       print('Do You Want To Make Another Conversion ?')
       restart= input().lower()
       if restart == "yes" or restart == "y":
              main()
       else:
              print("GoodBye")
              exit()
main()
