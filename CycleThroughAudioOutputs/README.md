# Audio Output Cycler

A small PowerShell script that switches the system’s audio output to the next available playback device.
The script is intended to be triggered by a hotkey or mouse gesture and runs silently without any UI.

## What it does

- Get currently available playback devices
- Filters out unwanted devices
- Detects the current output
- Switches to the next device in the list (wraps around)

If fewer than two valid devices are available, the script exits without doing anything.

## Requirements

- Windows
- PowerShell 5.1 or newer
- PowerShell module `AudioDeviceCmdlets`
```powershell 
Install-Module -Name AudioDeviceCmdlets
```

## Setup

Allow local PowerShell scripts for the current user:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Optionally compile to executable file if required by the caller of the script. Can be done using PowerShell module `PS2EXE`. 

```powershell
Install-Module -Name ps2exe
Invoke-PS2EXE .\cycle-next-output.ps1 .\cycle-next-output.exe
