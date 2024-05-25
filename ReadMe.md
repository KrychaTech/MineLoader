# MineLoader

This is a really short script (10 lines!) that downloads and runs Minecraft.

The play_minecraft.exe file is created from the minecraft_runner.py file with nuitka, which just utilizes [this](https://github.com/mindstorm38/portablemc/) to run the game. Huge thanks to mindstorm38 for making this project possible.

## Powershell
To download and run minecraft you only need to open Powershell and paste this command:

### Newest Release
```powershell
curl "https://github.com/KrychaTech/MineLoader/raw/main/play_minecraft.exe" -o "minecraft.exe"; "If you are running this script for the first time or downloading a new version this might take a while."; Start-Process -FilePath "minecraft.exe" -NoNewWindow -Wait; Remove-Item "minecraft.exe"
```

### Specified Release
Change the release argument (-r flag) to the version you want to run. In this example the version selected is 1.12.2.
```powershell
curl "https://github.com/KrychaTech/MineLoader/raw/main/play_minecraft.exe" -o "minecraft.exe"; "If you are running this script for the first time or downloading a new version this might take a while."; Start-Process -FilePath "minecraft.exe" -NoNewWindow -ArgumentList "-r 1.12.2" -Wait; Remove-Item "minecraft.exe"

