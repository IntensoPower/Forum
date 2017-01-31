# 3. - Mise en place d'un server web `nginx`:

## 3.1. Démarrer une machine virtuelle sera utilisé comme serveur:

```
cd <forum>/3_webserver
vagrant up
vagrant ssh
```

## 3.2. Installer et configurer `nginx` sur le serveur
### 3.2.1. Installation
  - Utiliser `apt` pour installer `nginx`
   
### 3.2.2. Configuration du site web
  - Télécharger le code sur le serveur dans `/var/www/html` en utilisant `git`
  - Configurer `nginx` pour servir les fichiers HTML contenues dans `/var/www/html`
