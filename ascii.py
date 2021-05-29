


#  Though I can easily make an interface to help you decide if the video should be captured from laptop camera or any video you wish to provide,
#  But I chose to boast the code I wrote, Thnx


from tkinter import *
import cv2
import os

cap=cv2.VideoCapture(0)

max_string_len=50


def play_ascii():
    os.system('cls')

    _,frame=cap.read()
    cv2.flip(frame,0)
    
    frame_height,frame_width=frame.shape[:2]
    refrence_dim=max(frame_height,frame_width)
    # x_step_len=int( ( frame_width / max_string_len ) * ( frame_width / refrence_dim ) )
    x_step=int(max_string_len * frame_width/refrence_dim)
    # y_step_len=int( ( frame_height / max_string_len ) * ( frame_height / refrence_dim ) )
    y_step=int(max_string_len * frame_height/refrence_dim)

    grey_frame=cv2.flip(cv2.resize(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),(x_step,y_step)),1)

    final=[['.']*x_step for i in range(y_step)]

    asciis = " .:-=+*#%@"[::-1]
    
    for i in range(y_step):
        for j in range(x_step):
            
            # final[i][j]=asciis[int( grey_frame[i*y_step_len][j*x_step_len]/(255/10))]
            final[i][j]=asciis[int( grey_frame[i][j]/(255/10))]

    # cv2.imshow("Frame", grey_frame)

    for row in final:
        print(*row)

# root=Tk()
# root.title('ASCII Video')
# root.columnconfigure(0,weight=1)
# root.columnconfigure(1,weight=1)

# Button(root,text='Camera',command=None)
# Button(root,text='Select',command=None)

# root.mainloop()

run=True
while run:
    try:
        play_ascii()

        key = cv2.waitKey(1)


    except KeyboardInterrupt:
        break

    
    # if key == 27:
    #     run=False
    #     break