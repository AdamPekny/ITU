Spustenie webovej aplikácie:
Webovú aplikáciu nájdete na adrese:
http://167.99.142.225:3000/

Pre prístup k užívateľským účtom slúžia účty vytvorené v databáze:
email: john.doe@johndoe.com
heslo: pwd
email: arthur.dent@arthurdent.com
heslo: password
email: fort.prefect@fortprefect.com
heslo: password
email: root@root.com
heslo: root
Registrácia nie je implementovaná nakoľko bolo v zadaní že jej implementácia by nemala byť implementovaná.


Spustenie na lokáli (v prípade potreby):
Backend:
    vytvorte mysql databázu
    importujte do nej súbor db_dump.sql z koreňovej zložky adresára
    nainštalujte python 3.8 alebo vyššie
    nastavte si python venv
    nainštalujte závislosti pomocou pip install -r requirements.txt
    server spustíte pomocou python manage.py runserver v zložke api/api/
Frontend:
    nainštalujte npm, nodejs a dependencies zo súboru dependencies
    frontend spustíte pomocou npm start

