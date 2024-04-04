@echo off
powershell -Command "Start-Process 'python' -ArgumentList 'Service.py install' -Verb runAs"
powershell -Command "Start-Process 'python' -ArgumentList 'Service.py start' -Verb runAs"
