; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
AppName=Gazette Notifications
AppPublisher=Lucas Watkins
AppPublisherURL=https://github.com/lucas-watkins/gazette-notifications
BackColor=clGreen
BackColor2=clWhite
AppVerName=Gazette Notifications 1.0.1
AppVersion=1.0.1
DefaultDirName={autopf}\Lucas Softworks\Gazette Notifications
LicenseFile=license.txt
AlwaysRestart=yes
DisableDirPage=yes
DisableProgramGroupPage=yes

[Files]
Source: "Gazette Notifications\*"; DestDir: "{app}\Lucas Softworks\Gazette Notifications"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{userstartup}\Gazette Notifications"; Filename: "{app}\Lucas Softworks\Gazette Notifications\notify.exe"; WorkingDir: "{app}"