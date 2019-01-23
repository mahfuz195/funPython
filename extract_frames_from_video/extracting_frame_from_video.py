import cv2
import sys
import glob

print (cv2.__version__)

def show_progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


video_dir = 'video.mp4'#'darkflow-master/video_2.AVI'
output_dir = 'frames/'
print ('Video  input  file from : ', video_dir)
print ('Frame  output file from : ', output_dir)

vidcap = cv2.VideoCapture(video_dir)
length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
total = length 

print ('Total frames in video : ' , total)

success,image = vidcap.read()
count = 0
frame_rate = 0
while success:
    success,image = vidcap.read()
    frame_rate +=1
       
    if(count%10==0):
        image = cv2.resize(image,(640,384))
        cv2.imwrite(output_dir + "frame_%d.jpg" % count, image)     # save frame as JPEG file      
       

    #print('Read a new frame: ', success)
    count += 1
    show_progress(count, total)

vidcap.release()
print ('OK')




