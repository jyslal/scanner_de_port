# Port Scanner TCP

Petit scanner de ports TCP simple écrit en Python.

Il permet de vérifier quels ports sont ouverts sur une adresse IP cible.

## Fonctionnalités

- Scan d'une adresse IP (IPv4)
- Scan de ports spécifiques ou d'une plage par défaut (1 → 999)
- Affichage du nom de service quand il est connu
- Timeout court pour un scan relativement rapide
- Arguments en ligne de commande via `argparse`

## Prérequis

- Python 3.6 ou supérieur
- Modules utilisés (tous inclus dans la bibliothèque standard) :
  - `socket`
  - `ipaddress`
  - `argparse`

Aucune installation de package externe n'est nécessaire.

## Utilisation

```bash
python port_scanner.py [options]
```

### Options disponibles

| Option          | Description                                      | Exemple              |
|-----------------|--------------------------------------------------|----------------------|
| `-c`, `--cible` | Adresse IP à scanner (défaut : `127.0.0.1`)      | `-c 192.168.1.10`    |
| `-p`, `--port`  | Liste de ports à scanner                         | `-p 22 80 443`       |
| `-pi`, `--ping` | Lance un ping                                    | `-pi`                |
