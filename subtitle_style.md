ffmpeg -i input.srt -vf "ass=fontsdir=/path/to/fonts:fontname=Arial:fontsize=20:borderw=3:shadowx=2:shadowy=2" output.ass
ffmpeg -i input.mp4 -vf "ass=output.ass" output.mp4
