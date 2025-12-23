# Get available playback devices
$available = Get-AudioDevice -List |
    Where-Object { 
        $_.Type -eq 'Playback' -and
        $_.ID -ne '{0.0.0.00000000}.{7bd35607-8a87-40b5-9246-892e008b0ad3}' # remove laptop speakers from cycle
    }

# Safety check
if ($available.Count -lt 2) {
    exit
}

# Determine current output
$curOutputID = Get-AudioDevice -Playback |
    Select-Object -ExpandProperty ID

# Cycle forward
$currentIndex = ($available | Select-Object -ExpandProperty ID).IndexOf($curOutputID)

# Fallback if current device is not part of the cycle
if ($currentIndex -lt 0) {
    $nextIndex = 0
} else {
    $nextIndex = ($currentIndex + 1) % $available.Count
}

# Set new Audio Output
Set-AudioDevice -Index $available[$nextIndex].Index
