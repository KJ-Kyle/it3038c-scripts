
function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}

function getVersion{
 (Get-Host).version | Select-String "5*"
}

function host{
 (Get-ComputerInfo).CsDNSHostName
}

function date{
 Get-Date
}

$User = $env:USERNAME
$Ver = getVersion
$IP = getIP
$Host1 = host
$Date = date

$Body = write-output("This machine's IP is $IP. User is $User. Host name is $Host1. Powershell Version $Ver. Today's Date is $Date") | out-file -filepath C:\Body.txt

$Body
notepad C:\Body.txt
