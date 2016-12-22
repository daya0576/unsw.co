#!/bin/sh

d='/home/henry/repo/unswco_develope/'

echo $d

python3 $d'scheduled_bd_backup.py' $d'db.sqlite3' $d'DB_backups'

