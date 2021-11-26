# Uppgift: Samarbete Te19
## Idag ska ni alla klona denna repo och spara i en helt ny mapp på er dator lokalt ni ska sedan välja en av uppgifterna nedan och lösa de i en egen bransch lokalt. När du löst din uppgift så ska du pusha din bransch till repot. På nästa lektion kommer jag godkänna allas push och se om ni lyckats skapa en hemsida tillsammans.
## I Repot finns en grundhemsida av django. Jag har tagit bort vissa rader som ni ska fylla i. Välj nedan vad du ska fixa. Alla väljer 1 person, men ni kan självklart samarbeta om ni fastnar, roligast om alla lyckas och blir klara så att vi får en bra färdig hemsida.

### Kommentarer där ni ska ändra finns i respektive filer.
### Är ni fler personer än det finns uppgifter kan man samarbeta i par, men båda gör samma uppgift.

### Person 1 (Lätt) - (Ditt namn här)
#### Ändringar att leta efter: 
#### Samarbete/Samarbete/settings.py  (Lägg till apparna)
#### Samarbete/Samarbete/urls.py (Koppla till de andra urls)

### Person 2 (Lätt) - (Ditt namn här) 
#### Ändringar att leta efter:
#### register/urls.py (Koppla till view)
#### register/templates/register.html (Lägg till att filen extendar 'mainsite.html')
#### register/templates/register.html (Lägg till så den laddar static files)
#### register/templates/register.html (Ändra titeln i head till Register)

### Person 3 (Lätt) - (Ditt namn här) 
#### Ändringar att leta efter:
#### register/urls.py (Importera views från mappen)
#### shop/views.py (Koppla till 'shop.html')
#### homsite/views.py (Koppla till 'mainsite.html')

### Person 4 (Medel) - (Ditt namn här)
#### Ändringar att leta efter:
#### mainsite/urls.py (Koppla till view)
#### mainsite/templates/mainsite.html (Lägg till en blockcontent tagg)
#### mainsite/templates/mainsite.html (Lägg till så den laddar static files)
#### mainsite/templates/mainsite.html (Lägg till så den länkar till register och shop)

### Person 5 (Medel) - (Ditt namn här)
#### Ändringar att leta efter:
#### shop/urls.py (Koppla till view)
#### shop/templates/shop.html (Extenda mainsite.html)
#### shop/templates/shop.html (Lägg till en blockcontent tagg)
#### shop/templates/shop.html (Lägg till så den laddar static files)

### Person 6 (Medel) - (Ditt namn här)
#### shop/templates/shop.html (Lägg till så den laddar in images rätt)
#### shop/templates/shop.html (Kopiera card diven och skapa så det finns 6 stycken)
#### shop/static/shop/style.css (Få de 6 cardsen att vara 3 per rad, på 2 rader, med mellanrum mellan varandra)

### Person 7 (Medel) - (Ditt namn här)
#### Ändringar att leta efter:
#### mainsite/templates/mainsite.html (Ändra så att den kopplar till style.css)
#### mainsite/static/mainsite/style.css (Stylea navbaren så att den är lite snyggare)
#### mainsite/templates/mainsite.html (Ändra så att knappen i <header> kopplar till shop)

### Person 8 (Svår) - (Ditt namn här)
#### Ändringar att leta efter:
#### register/views.py (Fixa funktionalitet för att kunna registrera en användare, ta hjälp från föregående uppgift)
#### Migrera allt när du är klar så att det går att komma till admin-sidan.
