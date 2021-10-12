print("Je word wakker door het geluid van geklop, je doet de deur open. Het is de politie, wat doe je ?")
print("typ: meegaan, of rennen")
choice = input()
if choice == 'meegaan':
    print("De politie neemt je mee naar het bureau en stelt je vragen over je kat, Panter")
elif choice == 'rennen':
    print("Je rent weg, de politie vangt je en neemt je mee naar het bureau, hij stelt je vragen over je kat, Panter")
else:
    print(choice, "Dat is geen keuze")