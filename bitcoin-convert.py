import requests

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')


def btc_eu():
    a = int(input("Merci d'entrer un montant de bitcoins à transformer en euros. "))
    print("La valeur de {} bitcoin est {} €".format(a, float(r.json()['bpi']['EUR']['rate'].replace(",", "")) * a))


def btc_usd():
    a = int(input("Merci d'entrer un montant de bitcoins à transformer en usd. "))
    print("La valeur de {} bitcoin est {} $".format(a, float(r.json()['bpi']['USD']['rate'].replace(",", ""))* a))


def usd_btc():
    a = int(input("Merci d'entrer un montant en USD à transformer en bitcoins. "))
    print("La valeur de {} USD est {} bitcoin".format(a, 1 / float(r.json()['bpi']['USD']['rate'].replace(",", "")) *a))


def eu_btc():
    a = int(input("Merci d'entrer un montant en EU à transformer en bitcoins. "))
    print("La valeur de {} € est {} bitcoins.".format(a, 1 / float(r.json()['bpi']['EUR']['rate'].replace(",", "")) *a))

def demande():
    print("Méthode 1 = 1 Bitcoin en EU // Méthode 2 = 1 Bitcoin en USD")
    print("Méthode 3 = USD vers Bitcoin // Méthode 4 = EU vers Bitcoin")
    methode = input("Merci d'entrer votre méthode. ")
    if methode == "1":
        btc_eu()
    elif methode == "2":
        btc_usd()
    elif methode == "3":
        usd_btc()
    elif methode == "4":
        eu_btc()
        
demande()

while methode != "1" and methode != "2" and methode != "3" and methode != "4":
    print("Erreur !")
    demande()
    
input("Mettez un caractère pour fermer ")
