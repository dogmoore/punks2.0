@echo off
title Punks 2.0 Console
echo Checking internet connection
Ping www.google.com -n 1 -w 1000
if errorlevel 0 (
  cls
  echo Verifying connection to Discord...
  ping -n 1 -w 1000 162.159.128.233
  if errorlevel 0 (
    cls
    echo Connected to internet
    echo Connected to Discord
    echo Fetching files from github, please wait a moment...
    git fetch https://github.com/dogmoore/Punks2.0
    echo files fetched, now starting up bot
    echo Now adding files to bot
    python index.py
  ) else (
    echo Can not connect to Discord, ending script
  )
) else (
  echo Can not connect to internet, ending script
)
pause
