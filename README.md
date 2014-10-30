LedBorg CPU Monitor on RaspberryPi
===================

Simple script written in Python for free use on your RaspberryPi with LedBorg, handy tool for monitoring your CPU usage in a simple way.
I have implemented gradient of 10 colors, from blue(<10%)-green(<50%)-red(<90%) CPU usage.



<h2><a name="requirements" class="anchor" href="#requirements"><span class="octicon octicon-link"></span></a>Requirements</h2>
<li>
<ul>Raspberry Pi</ul>
<ul><a href="http://www.piborg.com/ledborg">LedBorg from PiBorg</a></ul>
<ul>WiringPi2 Python module, installation instructions <a href="https://www.piborg.org/ledborg-new/install">available here</a></ul>
<ul>Python 2.7</ul>
<ul><a href="https://code.google.com/p/psutil/">psutil module</a></ul>
<ul>Some linux knowledge</ul>
</li>


<h2><a name="test" class="anchor" href="#test"><span class="octicon octicon-link"></span></a>Test</h2>

    sudo python ledborg-cpu-monitor.py

<h2><a name="installation" class="anchor" href="#installation"><span class="octicon octicon-link"></span></a>Installation</h2>

1. Copy ledborg-cpu-monitor.py in /usr/local/bin/ledborg #You can change the path<br>

   ```
   sudo cp ledborg-cpu-monitor.py /usr/local/bin/ledborg/
   ```

2. Make sure the script is executable<br>

    ```
    sudo chmod +x /usr/local/bin/ledborg/ledborg-cpu-monitor.py
    ```
    
3. Copy ledborg-cpu-monitor.sh in /etc/init.d #If you have changed default path of py script, you need to this file adding the correct path
   
    ```
    sudo cp ledborg-cpu-monitor.sh /etc/init.d
    ```

4. Make sure the script is executable<br>

    ```
    sudo chmod +x /etc/init.d/ledborg-cpu-monitor.sh
    ```

5. Auto start at boot<br>

   ```
   sudo update-rc.d ledborg-cpu-monitor.sh defaults
   ```

<h2><a name="usage" class="anchor" href="#usage"><span class="octicon octicon-link"></span></a>Usage</h2>
To start: `sudo /etc/init.d/ledborg-cpu-monitor.sh start`<br>
To stop: `sudo /etc/init.d/ledborg-cpu-monitor.sh stop`

<h2><a name="author" class="anchor" href="#author"><span class="octicon octicon-link"></span></a>Author</h2>

Bojan Vidanovic - Web Application Developer, in free time like to play with Raspberry Pi :) Follow me on:<br>
[Twitter](https://twitter.com/Bojan_Vidanovic)<br>
[Google+](https://plus.google.com/110220689355297296347)<br>

