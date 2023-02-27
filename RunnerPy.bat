@echo off
py src/main.py
for /d /r src %%d in (__pycache__) do (
    rd /s /q "%%d"
)
