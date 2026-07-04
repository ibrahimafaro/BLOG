def suite_sylvester() :
  print("Objectif : Afficher les n premiers termes de la suite \n")
  s0 = 2
  n = int(input("Donnez un entier naturel : "))
  while n < 0 :
    print("L'entier doit être positif ")
    n = int(input("Donnez un entier naturel : "))
  if n == 0 :
    print("Il sagit du premier terme de la suite : s0 =" , s0)
  else :
    d = 1
    s_precedent = s0
    lim = 1/s0
    for k in range(0,n+1) :
      if k == 0 :
        sn = s0
        print(f" s_{k} = {sn}")
      else :
        d *= sn 
        s_precedent = 1 + d
        sn =+ s_precedent
        # Limites
        lim = lim + 1/sn
        print(f" s_{k} = {sn} | la limite l_{k} = {lim}")
    # Approximation
    E = 1.26408
    print("La valeur approchée de s_{k} est : ", E**2**(n+1))
    check = input("Faire la comparaison entre valeurs exacte et approchée (non/oui) ?").strip()
    if check == "non" :
      print("Merci. \n Fin du programme")
    else :
      print(f"valeur exacte : {sn} | valeur approchée : {E**2**(n+1)}")
  return
