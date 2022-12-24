ffmpeg -i %2 -vn -acodec copy temp.aac
ffmpeg -i %1 -i temp.aac -vcodec copy -acodec copy tempoutput.mp4
del temp.aac
ffmpeg -i tempoutput.mp4 -c:v libx264 output.mp4
del tempoutput.mp4