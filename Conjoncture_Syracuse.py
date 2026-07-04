n = int(input("Donnez un entier n : "))
while n <0 :
  print(" n doit être positif !")
  n = int(input("Donnez la nouvelle valeur de n : "))
if n>0 : print(f" La valeur de n = {n}")
while n !=1 :
  print(n)
  if n%2 ==0 :
    n = n/2
  else :
    n = 3*n +1
  n=+n
print(n)
