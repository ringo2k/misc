#!/usr/bin/python
# Import everything needed to edit video clips
from moviepy.editor import *


introImageTime = 5 # time the intro image is shown in seconds
thingiverseNr = 000
machineType="Mendel i2"
# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip("test.mpg")

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0)
clip = vfx.freeze(clip, 0, introImageTime)
intro = vfx.blackwhite(clip)
intro = vfx.freeze(intro, 0, introImageTime)
intro = intro.set_duration(introImageTime)
intro = vfx.colorx(intro, 0.2)

#introImage = ImageClip("mendeli2.png")

# print infos
w,h = clip.size
duration = clip.duration
print "Video size W: " + str(w) + ", H " + str(h)
print "Duration " + str(duration) + "s"
print TextClip.list("font")
#introImage = introImage.resize((h,w))



# Generate a text clip. You can customize the font, color, etc.
if machineType != "":
    machineTypeTxt = TextClip("Machine:\n"+str(machineType),font="DejaVu-Serif",fontsize=20,color='red', stroke_color="white")
else:
    machineTypeTxt = TextClip("",font="DejaVu-Serif",fontsize=20,color='red', stroke_color="white")


# prepare thingiverse hint in video
thingiverseTxt= TextClip("Printing thingiverse thing:\n"+str(thingiverseNr),font="DejaVu-Serif",fontsize=25,color='blue', stroke_color="white")
thingiverseTxt = thingiverseTxt.set_pos("top")
thingiverseTxt = thingiverseTxt.set_duration(introImageTime)


# Say that you want it to appear 10s at the center of the screen
machinetypeTxt = machineTypeTxt.set_pos('center').set_duration(introImageTime)
#introImage = introImage.set_pos("center").set_duration(introImageTime)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip,intro, machinetypeTxt, thingiverseTxt])

# Write the result to a file (many options available !)
video.write_videofile("test_edited.mp4")
