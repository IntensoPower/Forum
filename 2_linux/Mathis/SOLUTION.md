* Vérifier la taille du disque dur: 
```
$ df -h
```
        
* Se déplacer dans le dossier `/opt/videogames`:    
```
$ cd /opt/videogames
```

* Créer les dossiers `/opt/videogames/ps4`  et `/opt/videogames/nintendo`:
```
$ mkdir nintendo
$ mkdir ps4
```
  
* Utiliser un éditeur de texte pour créer le fichier `/opt/videogames/ps4/sonic.info` et écrire les informations suivantes:
```
### A écrire dans le fichier:
Sonic possède un éventail de mouvements spéciaux sans cesse renouvelés et améliorés au fil des jeux. Des simples Rolling Spin Attack et Jumping Spin Attack (Rouler Tourbillon Attaque et Sauter Tourbillon Attaque) en boule, il développe le Spin Dash (Course tourbillon) qui permet de prendre de l'élan, le Super Peel Out qui est une alternative du Spin Dash et le Drop Dash (Turbo jeté).
############################
```

```
$ touch sonic.info
$ cat > sonic.info
Sonic possède un éventail de mouvements spéciaux sans cesse renouvelés et améliorés au fil des jeux. Des simples Rolling Spin Attack et Jumping Spin Attack (Rouler Tourbillon Attaque et Sauter Tourbillon Attaque) en boule, il développe le Spin Dash (Course tourbillon) qui permet de prendre de l'élan, le Super Peel Out qui est une alternative du Spin Dash et le Drop Dash (Turbo jeté).
^C
```

* Utiliser un éditeur de texte pour créer le fichier `/opt/videogames/nintendo/mario.info` et écrire les informations suivantes:

```
### A écrire dans le fichier:
Les sources divergent quant à l'origine du patronyme. Le nom de Mario aurait été choisi en l'honneur du propriétaire des locaux de la société Nintendo of America de l'époque, Mario Segali6. Mais, selon Eiji Aonuma, proche collaborateur de Shigeru Miyamoto, Mario serait l'abréviation de marionnette, choisi par Miyamoto à cause de son amour des automates et du bunraku, le théâtre de marionnettes japonais7. Shigeru Miyamoto, quant à lui, a déclaré lors d'une interview que c'est un employé de Nintendo of America qui lui avait suggéré le nom de Mario3. Lors des vidéos précédant la sortie de Super Mario Maker, Miyamoto confirme que le nom vient bel et bien de Mario Segali.
############################
```

```
$ cd ..
$ cd nintendo
$ touch mario.info
$ cat > mario.info
Les sources divergent quant à l'origine du patronyme. Le nom de Mario aurait été choisi en l'honneur du propriétaire des locaux de la société Nintendo of America de l'époque, Mario Segali6. Mais, selon Eiji Aonuma, proche collaborateur de Shigeru Miyamoto, Mario serait l'abréviation de marionnette, choisi par Miyamoto à cause de son amour des automates et du bunraku, le théâtre de marionnettes japonais7. Shigeru Miyamoto, quant à lui, a déclaré lors d'une interview que c'est un employé de Nintendo of America qui lui avait suggéré le nom de Mario3. Lors des vidéos précédant la sortie de Super Mario Maker, Miyamoto confirme que le nom vient bel et bien de Mario Segali. 
^C
```

> Le système contient 4 utilisateurs:
> 
> ![Utilisateurs](/2_linux/pictures/users.png?raw=true)
> 
> `mario` et `luigi` font parti du groupe `nintendo`
> `sonic` et `tails` font parti du groupe `ps4`

* Comment changer d'utilisateur pour devenir `luigi`
```
$ sudo su luigi
```
  
* Seul `mario` peut écrire dans le fichier `/opt/videogames/nintendo/mario.info`. Tous les autres peuvent le lire:
```
$ chmod 644 mario.info
```

* `sonic` autorise `tails` à lire le fichier `/opt/videogames/ps4/sonic.info`. Par contre les autres ne peuvent que voir le contenu du dossier `/opt/videogames/ps4/` (ils ne peuvent ni les lire, ni les écrire).
```
$ chmod 640
```

* Donner une commande équivalente à:
```
cd /home/vagrant
```
```
$ cd vagrant
```
  
* Combien de lignes contient le fichier `/home/vagrant/videogames.txt
```
$ wc -l videogames.txt
```
  
* Rechercher combien de fois le mot `Mario` apparait dans le fichir `/home/vagrant/videogames.txt
```
$ grep -c Mario videogames.txt
```

* A quelle(s) ligne(s) le jeu `Secret of Mana` apparait dans le fichir `/home/vagrant/videogames.txt
```
$ grep -n "Secret of Mana" videogames.txt
```

* A quelle(s) ligne(s) le jeu `Secret of Mana` apparait dans le fichir `/home/vagrant/videogames.txt
```
$ grep -n "Secret of Mana" videogames.txt
```
