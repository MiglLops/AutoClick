import pyautogui as pa, keyboard

pa.PAUSE = 0

print("Pressione 'z' para iniciar ou 'x' para parar")

keyboard.wait("z")
print("Autocliker iniciado...")

cliques = 0
while not keyboard.is_pressed("x"):
    pa.click()
    cliques += 1

input(cliques)

