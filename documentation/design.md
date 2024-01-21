# DISSENY DE L'APLICACIÓ WEB
He decidir fer una aplicació web degut a que és més fàcil d'accedir-hi des de qualsevol dispositiu. També és més fàcil de mantenir, ja que no cal instal·lar-la en cada dispositiu.

## Eines utilitzades
Per fer el disseny de l'aplicació web, he utilitzat el programa [Figma](https://www.figma.com/). Aquest programa és molt intuïtiu i fàcil d'utilitzar. També és molt potent, ja que permet crear prototips interactius. (Imatge del prototip)

## Frameworks utilitzats
Encara no està decidit.

# ESQUEMA DE LA BASE DE DADES
Al ser una aplicació web que consistirà en el desenvolupament de tornejos de futbol, he decidit crear una base de dades que contingui tota la informació necessària per a poder desenvolupar aquesta aplicació web. Aquesta base de dades estarà formada per les següents taules:

## Taules de la base de dades:

 ***Arbitre***: Contindrà informació dels àrbitres que participaran als tornejos. Aquesta informació serà el nom, cognoms i dades de registre per tancar les actes.
 
 ***Equip***: Contindrà informació dels equips que participaran als tornejos. Aquesta informació serà el nom, escut, gols a favor i en contra, punts i resultats.
 
 ***Jugador***: Contindrà informació dels jugadors que participaran als tornejos. Aquesta informació serà el nom, cognoms, dorsal, gols i data de naixement.

 ***Partit***: Contindrà informació dels partits que es disputaran als tornejos. Aquesta informació serà la data, l'hora, l'àrbitre, l'equip local, l'equip visitant, el resultat i el camp on es disputarà el partit.

 ***Camp***: Contindrà informació dels camps on es disputaran els partits. Aquesta informació serà el nom.

 ***Torneig***: Contindrà informació dels tornejos que es disputaran. Aquesta informació serà el nom, la data d'inici, la data de finalització, i la fase del torneig.

 ***Grup***: Contindrà informació dels grups que es disputaran als tornejos. Aquesta informació serà el nom, el torneig al que pertany i els equips que hi participen.

 ***Ubicacions***: Contindrà informació de les ubicacions dels camps. Aquesta informació serà la ciutat, provincia, codi postal i direcció.

 ***Personal***: Contindrà informació del personal que participarà als tornejos. Aquesta informació serà el nom, cognoms i tipus de personal.
 
 ***Administrador***: Contindrà informació dels administradors de l'aplicació web. Aquesta informació serà el nom, cognoms, usuari i contrasenya.

 ***Gol***: Contindrà informació dels gols que es marcaran als partits. Aquesta informació serà el jugador que ha marcat el gol, el partit on s'ha marcat el gol i l'equip que ha marcat el gol.

***Sancions*** (taula intermitja): Contindrà informació de les sancions que es donaran als jugadors. Aquesta informació serà el jugador que ha rebut la sanció, el partit on s'ha rebut la sanció i el tipus de sanció.

***Classificació*** (taula intermitja): Contindrà informació de la classificació dels equips als grups. Aquesta informació serà l'equip, el grup, la posició, victories, empats i derrotes.

## Diagrama de la base de dades:

Aquest és el diagrama de la base de dades que he creat per aquesta aplicació web. Aquest diagrama està creat amb el programa [SqlIDBM](https://app.sqldbm.com/) i es pot trobar a la carpeta **sql**.

![IBB](https://i.ibb.co/sjnTzrN/diagrama-ER-bbdd.png)

Per aixecar la base de dades, he utilitzat la llibreria [SQL alchemy](https://www.sqlalchemy.org/). Aquesta llibreria permet crear la base de dades a partir dels models de les taules. Aquests models es troben a la carpeta **models**.