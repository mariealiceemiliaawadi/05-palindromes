t = str.maketrans("àâäéèêëîïôöùûüç?!',-:", "aaaeeeeiioouuuc      ")

#### Fonction secondaire


def ispalindrome(p):

    # votre code ici
    """module de verifiction"""

     # Vérifie si une chaîne est un palindrome en ignorant la casse, les espaces, la ponctuation et les accents.

    p = p.lower()
    # print(p)
    p = p.translate(t)
    # print(p)
    p = p.replace(" ", "")
    # print(p)
    # print(p)
    # p=p.replace(" "," ").replace(".","").replace("ô", "o").replace("?"," ")
    # p=p.replace("ê", "e").replace("!"," ").replace ("-"," ").replace("'"," ")
    # p=p.replace(","," "). replace("é", "e").replace("è", "e").replace("ù", "u")
    # p=p. replace("ë", "e").replace("ç", "c").replace("à", "a").replace(":"," ")
    return p == p[::-1]

        


    
  

#### Fonction principale
    

def main():
    """module de definition"""
    # vos appels à la fonction secondaire ici

    # for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
    #     print(s, ispalindrome(s))

    s = "Tu l'as trop écrasé, César, ce Port-Salut"
    print(s, ispalindrome(s))




if __name__ == "__main__":
    main()