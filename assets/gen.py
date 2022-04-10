import os
import webbrowser
import pyimgur
import urllib.request
import time
from rich import print
from rich.progress import track
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


CLIENT_ID = "65e4214d4f2cf06"

os.system("cls")

def remove():
    os.remove("char.svg")
    os.remove("char.png")

print("1 - [bold]male[/]")
print("2 - [bold]female[/]")
print("3 - [bold]human[/]")
print("4 - [bold]identicon[/]")
print("5 - [bold]initials[/]")
print("6 - [bold]bottts[/]")
print("7 - [bold]winter-hat[/]")
print("8 - [bold]jdenticon[/]")
print("9 - [bold]gridy[/]")
print("10 - [bold]micah[/]")
print("11 - [bold]big-ears[/]")

sprite = int(input("Qual seu tipo de char?: "))

if(sprite == 1):
    sprite = ("male")
elif(sprite == 2):
    sprite = ("female")
elif(sprite == 3):
    sprite = ("human")
elif(sprite == 4):
    sprite = ("identicon")
elif(sprite == 5):
    sprite = ("initials")
elif(sprite == 6):
    sprite = ("bottts")
elif(sprite == 7):
    sprite = ("avataaars")
elif(sprite == 8):
    sprite = ("jdenticon")
elif(sprite == 9):
    sprite = ("gridy")
elif(sprite == 10):
    sprite = ("micah")
elif(sprite == 11):
    sprite  = ("big-ears")


os.system("cls")

print(":face_with_monocle: Qual o nick do seu char?: ")
seed = input("")

os.system("cls")

print("1 - [purple]Purple[/]")
print("2 - [blue]Blue[/]")
print("3 - [red]Red[/]")
print("4 - [black]Black[/]")
print("5 - [white]White[/]")
print("6 - [blue]Dark Blue[/]")
print("7 - [gray]Gray[/]")
print("8 - [green]Green[/]")

color = int(input("Digite a cor de fundo para seu char: "))

if(color == 1):
    color = ("23a600ff")
elif(color == 2):
    color = ("230062ff")
elif(color == 3):
    color = ("23ff2e2e")
elif(color == 4):
    color = ("230d0d0d")
elif(color == 5):
    color = ("23f0f0f0")
elif(color == 6):
    color = ("23070066")
elif(color == 7):
    color = ("23595959")
elif(color == 8):
    color = ("2340e261")

os.system("cls")

print("1 - SIM")
print("2 - NÃO")


border = int(input("Quer adicionar borda ao seu char?: "))

if(border == 1):
    border = ("&r=23")
elif(border == 2):
    border = ("")

r = ("https://avatars.dicebear.com/api/{0}/{1}.svg?b=%{2}{3}&top[]=winterHat04&skin[]=light".format(sprite, seed, color, border))

def dl(url, file_path, file_name):
    full_path  = file_path + file_name +'.svg'
    urllib.request.urlretrieve(url, full_path)

url = r
file_name = "char"

dl(url, './', file_name)

drawing = svg2rlg('char.svg')
renderPM.drawToFile(drawing, 'char.png', fmt='PNG')

PATH = "char.png"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="Char: "+seed)

os.system("cls")

link = uploaded_image.link
final_link = link.replace(".png","")

print(":white_check_mark: Obrigado por usar o CharMaker :smile: :v:")

for tarefa in track(range(3), 'Gerando char...'):
    time.sleep(0.5)

webbrowser.open(final_link)
remove()






