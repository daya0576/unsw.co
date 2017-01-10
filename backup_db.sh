#!/bin/sh

d='/home/daya0576/unsw-it-8543-courses/'

echo $d

python3 $d'scheduled_bd_backup.py' $d'db.sqlite3' $d'DB_backups'

