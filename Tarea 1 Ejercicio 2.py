#Fernando Donis 20210415

def nota(cali): 
  if cali >= 90: return "A"
  elif cali >= 80: return "B"
  elif cali >= 70: return "C"
  elif cali >= 65: return "D"
  elif cali <= 64: return "F"
  else: return "Problemita"

def main(): 
  cali = int(input("Ingrese su calificacion: "))     
  print("Su nota es:", nota(cali))

main()