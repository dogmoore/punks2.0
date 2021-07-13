@echo off
title Punks 2.0 creation
cd ..
cd ..
cd ..
cls
Ping www.google.com -n 1 -w 1000
if errorlevel 0 (
  cls
  echo Connected to internet
) else (
  exit
)
echo now downloading git repository for Punks 2.0
echo now creating config file
  (
    echo prefix: '&'
    echo token: 'ODA5MjA0MjgxNjA0ODMzMzAx.YCRsNw.HJo6TfbRIwyxy-iWIAWdgA_EqPA'
    echo version: '69.42.0'
    echo UNUSED: 'UNUSED'
  ) >> "c:\github\punks2.0\config.yml"

  echo done
)
pause
