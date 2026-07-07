def suite_sylvester() :
  print("Objectif :  Afficher les n premiers termes de la suite \n")
  n = int(input("Donnez un entier naturel : "))
  s0 = 2
  while n < 0  :
    print("Erreur : n doit être positif")
    n = int(input("Donnez un entier naturel : "))
  if n == 0 :
    print("C'est le premier terme de la suite :", s0)
  else :
    print("Voici les n premiers termes de la suite")
    d = 1
    s_precedent = s0
    lim = 1/s0
    for k in range(0,n+1) :
      if k == 0 :
        sn = s0
      else :
         d *=sn
         s_precedent = 1+d
         print(f"s_{k-1} = {sn}")
         sn =+ s_precedent
         # Limites
         lim = lim 
         print(f"La limite de s_{k-1} est : l_{k-1} =", round(lim,3))
         lim = lim + 1/sn
    # Approximation
    E = 1.26408
    print(f"La prédiction du terme suivant est : s_{k} : {E**2**(n+1)}")
    check = input("Voulez-vous comparer la valeur exacte à celle approximative (oui/non) ?").strip()
    if check in ["non","Non","NON","No"] :
      print("D'accord. \n Merci")
    else :
      print(f"Valeur exacte : {sn} | Valeur approximative : {E**2**(n+1)}")
  return
