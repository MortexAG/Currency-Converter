import requests
def currency_converter(cur_from, cur_to, amount_to):
    """
    The First Input is The Currency You Want to Convert From.
    The Second Input is The Currency You Want to Convert To.
    The Third Input is The Amount You Want to Convert.
    *All Currencies Must Be With Codes As "usd" and "eur" And The Amount Must Always Be A Number*
    """
    currency_from = cur_from
    currency_to = cur_to
    amountof = amount_to
    url = 'https://api.exchangerate.host/convert?from={}&to={}&amount={}'.format(currency_from , currency_to, amountof)
    response = requests.get(url)
    data = response.json()
    data_from = data["query"]["from"]
    data_to = data["query"]["to"]
    data_result = data["result"]
    print(amountof , data_from,  "=", data_result, data_to)
