# BackgroundMusicRemover
<p>This tool is designed to remove the background music of a video, and then return a VIDEO with the bg audio removed.</p>
<p>This should make life a bit easier when you have to isolate the vocals from a batch of videos</p>
<strong><h3>Warning!</h3></strong>
<hr>
<p> Yo, I made this script in 2 hours whilst sleep deprived, so if it has bugs, please keep that in mind</p>
<h3>Pre-prerequisates</h3>
<hr>
<ol>
  <li>Make sure you have a version of Python that supports pytorch. As of 08/03/2023, this is python 3.10</li>
  <li>Install pytorch <a href = "https://pytorch.org/">here</a>, using their handy installer.</li>
  <li>Finally, make sure you have FFMpeg installed. If you're on Windows, check out this installation guide from <a href="https://www.wikihow.com/Install-FFmpeg-on-Windows">WikiHow.</a></li>
 </li>
</ol>

<h3>Required Packages</h3>
<hr>
<ul>
  <li><a href="https://github.com/deezer/spleeter">spleeter</a></li>
</ul>

<h3>How to use</h3>
<hr>
<ol>
  <li>Place your video files in the Input Folder</li>
  <li>Run the command: $python BackgroundMusicRemover.py</li>
  <li>After the script executes, you should find the videos in the Output folder</li>
 </ol>
 <h3>Acknowledgements</h3>
 <hr>
 <p>In random order, I would like to thank</p>
 <ul>
  <li>Deezer for making Spleeter</li>
  <li>That mosquito that kept me awake all night which lead me to making this script out of boredom</li>
 </ul>
