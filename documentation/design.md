# DISSENY DE L'APLICACIÓ WEB
He decidir fer una aplicació web degut a que és més fàcil d'accedir-hi des de qualsevol dispositiu. També és més fàcil de mantenir, ja que no cal instal·lar-la en cada dispositiu.

## Eines utilitzades
Per fer el disseny de l'aplicació web, he utilitzat el programa [Figma](https://www.figma.com/). Aquest programa és molt intuïtiu i fàcil d'utilitzar. També és molt potent, ja que permet crear prototips interactius. (Imatge del prototip)

## Frameworks utilitzats
Encara no està decidit.

# ESQUEMA DE LA BASE DE DADES
Al ser una aplicació web que consistirà en el desenvolupament de tornejos de futbol, he decidit crear una base de dades que contingui tota la informació necessària per a poder desenvolupar aquesta aplicació web. Les taules que formen la base de dades són les següents:
    
- **Jugador**: Aquesta taula conté la informació dels jugadors que participen en els tornejos. Aquesta taula conté els següents camps:
    - **id**: Aquest camp conté l'identificador del jugador. Aquest camp és de tipus enter i és la clau primària de la taula.
    - **nom**: Aquest camp conté el nom del jugador. Aquest camp és de tipus cadena de caràcters.
    - **cognom**: Aquest camp conté el cognom del jugador. Aquest camp és de tipus cadena de caràcters.
    - **equip**: Aquest camp conté l'equip del jugador. Aquest camp és de tipus cadena de caràcters.
    - **posicio**: Aquest camp conté la posició del jugador. Aquest camp és de tipus cadena de caràcters.
    - **gols**: Aquest camp conté el nombre de gols que ha marcat el jugador. Aquest camp és de tipus enter.
    - **targetes_grogues**: Aquest camp conté el nombre de targetes grogues que ha rebut el jugador. Aquest camp és de tipus enter.
    - **targetes_vermelles**: Aquest camp conté el nombre de targetes vermelles que ha rebut el jugador. Aquest camp és de tipus enter.
    - **id_equip**: Aquest camp conté l'identificador de l'equip al qual pertany el jugador. Aquest camp és de tipus enter i és una clau forana.

- **Equip**: Aquesta taula conté la informació dels equips que participen en els tornejos. Aquesta taula conté els següents camps:
    - **id**: Aquest camp conté l'identificador de l'equip. Aquest camp és de tipus enter i és la clau primària de la taula.
    - **nom**: Aquest camp conté el nom de l'equip. Aquest camp és de tipus cadena de caràcters.
    - **punts**: Aquest camp conté el nombre de punts que té l'equip. Aquest camp és de tipus enter.
    - **gols_favor**: Aquest camp conté el nombre de gols a favor que té l'equip. Aquest camp és de tipus enter.
    - **gols_contra**: Aquest camp conté el nombre de gols en contra que té l'equip. Aquest camp és de tipus enter.
    - **id_torneig**: Aquest camp conté l'identificador del torneig al qual pertany l'equip. Aquest camp és de tipus enter i és una clau forana.

- **Torneig**: Aquesta taula conté la informació dels tornejos que es disputen. Aquesta taula conté els següents camps:
    - **id**: Aquest camp conté l'identificador del torneig. Aquest camp és de tipus enter i és la clau primària de la taula.
    - **nom**: Aquest camp conté el nom del torneig. Aquest camp és de tipus cadena de caràcters.
    - **data_inici**: Aquest camp conté la data d'inici del torneig. Aquest camp és de tipus data.
    - **data_final**: Aquest camp conté la data de finalització del torneig. Aquest camp és de tipus data.
    - **id_camp**: Aquest camp conté l'identificador del camp on es disputa el torneig. Aquest camp és de tipus enter i és una clau forana.

- **Camp**: Aquesta taula conté la informació dels camps on es disputen els tornejos. Aquesta taula conté els següents camps:
    - **id**: Aquest camp conté l'identificador del camp. Aquest camp és de tipus enter i és la clau primària de la taula.
    - **nom**: Aquest camp conté el nom del camp. Aquest camp és de tipus cadena de caràcters.
    - **adreça**: Aquest camp conté l'adreça del camp. Aquest camp és de tipus cadena de caràcters.
    - **ciutat**: Aquest camp conté la ciutat on es troba el camp. Aquest camp és de tipus cadena de caràcters.
    - **provincia**: Aquest camp conté la província on es troba el camp. Aquest camp és de tipus cadena de caràcters.
    - **codi_postal**: Aquest camp conté el codi postal del camp. Aquest camp és de tipus enter.
    - **id_administrador**: Aquest camp conté l'identificador de l'administrador del camp. Aquest camp és de tipus enter i és una clau forana.

- **Administrador**: Aquesta taula conté la informació dels administradors dels camps. Aquesta taula conté els següents camps:
    - **id**: Aquest camp conté l'identificador de l'administrador. Aquest camp és de tipus enter i és la clau primària de la taula.
    - **nom**: Aquest camp conté el nom de l'administrador. Aquest camp és de tipus cadena de caràcters.
    - **cognom**: Aquest camp conté el cognom de l'administrador. Aquest camp és de tipus cadena de caràcters.
    - **correu_electronic**: Aquest camp conté el correu electrònic de l'administrador. Aquest camp és de tipus cadena de caràcters.
    - **contrasenya**: Aquest camp conté la contrasenya de l'administrador. Aquest camp és de tipus cadena de caràcters.
    - **id_camp**: Aquest camp conté l'identificador del camp on treballa l'administrador. Aquest camp és de tipus enter i és una clau forana.

- **Partit**: Aquesta taula conté la informació dels partits que es disputen en els tornejos. Aquesta taula conté els següents camps:
    - **id**: Aquest camp conté l'identificador del partit. Aquest camp és de tipus enter i és la clau primària de la taula.
    - **data**: Aquest camp conté la data del partit. Aquest camp és de tipus data.
    - **hora**: Aquest camp conté l'hora del partit. Aquest camp és de tipus hora.
    - **id_equip_local**: Aquest camp conté l'identificador de l'equip local. Aquest camp és de tipus enter i és una clau forana.
    - **gols_equip_local**: Aquest camp conté el nombre de gols que ha marcat l'equip local. Aquest camp és de tipus enter.
    - **id_equip_visitant**: Aquest camp conté l'identificador de l'equip visitant. Aquest camp és de tipus enter i és una clau forana.
    - **gols_equip_visitant**: Aquest camp conté el nombre de gols que ha marcat l'equip visitant. Aquest camp és de tipus enter.
    - **id_camp**: Aquest camp conté l'identificador del camp on es disputa el partit. Aquest camp és de tipus enter i és una clau forana.
    - **id_torneig**: Aquest camp conté l'identificador del torneig al qual pertany el partit. Aquest camp és de tipus enter i és una clau forana.

## Diagrama de la base de dades:


Per aixecar la base de dades, he utilitzat la llibreria [SQL alchemy](https://www.sqlalchemy.org/). Aquesta llibreria permet crear la base de dades a partir dels models de les taules. Aquests models es troben a la carpeta **models**.