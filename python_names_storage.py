from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "electric-icon-382122",
  "private_key_id": "12d898464a0ee6449b20bc0a732fb751f86637ae",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDCUvDGH1W1oV0N\nSf2dwZZhLtfl81wGwrzWrRdVm8nCcLiiwUE8MWZAOZyNUKRZe9JAFefDaxnw/pSG\n8Rc38eg10LEcrW5Y5UDd0aJJdkpzjztf5Q9LMPYWx0ph97NoTllMGL2DzX1hcpJK\n7xwdvPlH+TXqjW4sc/WM9NTVV8vtqzPMEfegMw2W4BItM2rgdKUafI7E7VQ3rgFO\n9BGu6jJxi3awTmiFlfRHlljWJkSFtJz4MkeVrZOIJVEmlFGxIPN7yCMvVJTkHAfA\nF1YDzI1z/prka47cFtOSGRC1nCTQENBMyOB8DO8oNmHazY031tGOzukXYVAhHuRT\n0FnZYnqbAgMBAAECggEARjXvdrYVorV1yHpmXxx1+BETwqrGIk80KaCKoMzT/iP6\nIhwPNO9oUWY/cTOk3gwF8E+52HqW+eMRyRvM1tLZorAPfhwPlaDnaf33U/GgftZO\njpxVhUZgc+R3tKPpt5MvYnZB6yBQ3+ekgdyY3QnNS7r4RxHor7kKDG7dg2Pgc7NZ\nBOjxJWTUHs9ICKM88fXb5vFWn7K94CfsNYw4PT+Fd3zvlImTFzuhyzE//zInHNZn\nfbMAcbcwSSI5nh3HiDTgGq8y2Fz4n84iTFLEyE3NmS1trnpZsm7yxBSaF05JRwTs\nduy2aHIMGVjd483DAFFKtQBp5CqvSNJABaUXSKQ1sQKBgQD0CR7f+KAhQhfUAtHK\nn67NB3GX6RflLNaI7fDVy9rv5vz0UXf0GQ00qbQUA/LY0OiveX9agsFqSU5o2egQ\nmVOKz3KIy0o9mQbK9m/JgiRINOpCs8Hzn6wqjy7ynXxktKO1TWccxPEideB4cW+b\n4CTd1ikS9EjmcFkJ6pWzS/APowKBgQDL2eQ57vjIB+YgeotA/ifqHttgtiGBpk9U\nr5WT2mnGYnFJIWgLF4RyASnLTDGOz36tevPxh/2qH4ODEeYFzdwWVBmxL4g0teEX\n9afW8Pa6mlkP+46m6h1Cm1PqLfVtxqnnHa8YCpwiXySsuH+W6pAiVhdKg5y0mKhv\n+aqaH1m4qQKBgQCdiC24I0UrcwDyyYcoKACtNfrsN3pHZLRw3Di1qs0ARLpR9S1c\nE7fkoRAwQ4RG1kT+0Y2WngXBWOUW5mPaI0A8wUGMcL7SGLC74G21RR+qxQ3cVTIE\n1LRNHPUPhP5B/CIZ7Yd8mN2Yg0OOPJvxobXqxk7pf2x35Vp0/kv43DJxxQKBgQCi\nQtA9pRB1+IOfOqv5kdSnsOQieRb2ojDnUdQYGnSzqsxNz7+HhLKyJGbmIcIY0OUe\npY3jpcGuVuNRwz97Qz96rnq85P7gJh4D+lAc8TUTl6Ro6m3EQvoDeKw07Vw8gzPe\neWxUEK3zVhRVP46fzBnqmuhzMYvc3N7GMs8vWuEJ8QKBgCkFELDrn5IO4FfR/bCF\nX+HRGRNRidLMA7Iz6KKrR87iwF3nFRgM2zUFzMYaUHRqnpTZ6Z1vpMGNu3wk1gFo\nnTfz8vf6Hs+jnz+Xrkh4EflSTZ2jD4DB6l4GXWGtichb8YOIr4sRxqqXLqrkkvCa\nmjq2Yme/eKPC1sJg+yUuXIzE\n-----END PRIVATE KEY-----\n",
  "client_email": "conta-atividade@electric-icon-382122.iam.gserviceaccount.com",
  "client_id": "103688183534295594761",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/conta-atividade%40electric-icon-382122.iam.gserviceaccount.com"
}

try:

  """Uploads a file to the bucket."""
  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials)
  bucket = storage_client.get_bucket('electric-icon-382122') 
  blob = bucket.blob('artist-names.csv')

  pages = []
  names = "Name \n"

  for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

  for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
      names = names + artist_name.contents[0] + "\n"

    blob.upload_from_string(names, content_type="text/csv")

except Exception as ex:
  print(ex) 