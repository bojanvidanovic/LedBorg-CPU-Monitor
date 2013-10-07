LedBorg CPU Monitor on RasperryPi
===================
<h3>Description:</h3>
Simple script for free use on your RaspberryPi with LedBorg, it's a handy tool for monitoring your CPU usage in a simple way.
I have implemented gradient of 10 colors, from blue-green-red, red is above 90% CPU usage.


<h3>Requirements:</h3>
<li>
<ul>Raspberry Pi</ul>
<ul><a href="http://www.piborg.com/ledborg">LedBorg from PiBorg</a></ul>
<ul>Python 2.7</ul>
<ul><a href="https://code.google.com/p/psutil/">psutil module</a></ul>
<ul>Some linux knowledge</ul>
</li>


<h3>Installation:</h3>
1. Copy ledborg-cpu-monitor.py in /usr/local/bin/ledborg #You can change the path<br>
   sudo cp ledborg-cpu-monitor.py /usr/local/bin/ledborg/

2. Make sure the script is executable<br>
   sudo chmod +x /usr/local/bin/ledborg/ledborg-cpu-monitor.py

3. Copy ledborg-cpu-monitor.sh in /etc/init.d #If you have changed default path of py script, you need to this file adding the correct path
   sudo cp ledborg-cpu-monitor.sh /etc/init.d

4. Make sure the script is executable<br>
   sudo chmod +x /etc/init.d/ledborg-cpu-monitor.sh

5. Auto start at boot<br>
   sudo update-rc.d ledborg-cpu-monitor.sh defaults

<h3>Usage:</h3>
To start: sudo /etc/init.d/ledborg-cpu-monitor.sh start<br>
To stop: sudo /etc/init.d/ledborg-cpu-monitor.sh stop
