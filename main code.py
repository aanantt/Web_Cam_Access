{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "error",
     "evalue": "OpenCV(3.4.2) C:\\projects\\opencv-python\\opencv\\modules\\highgui\\src\\window.cpp:356: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31merror\u001b[0m                                     Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-d9f20dd0adc2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[0mret\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mframe\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcap\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m     \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mimshow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'frame'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mframe\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwaitKey\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m&\u001b[0m \u001b[1;36m0xFF\u001b[0m\u001b[1;33m==\u001b[0m \u001b[0mord\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'q'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m         \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31merror\u001b[0m: OpenCV(3.4.2) C:\\projects\\opencv-python\\opencv\\modules\\highgui\\src\\window.cpp:356: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "cap=cv2.VideoCapture(0)\n",
    "width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))\n",
    "height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))\n",
    "while True:\n",
    "    ret,frame=cap.read()\n",
    "    \n",
    "    cv2.imshow('frame',frame)\n",
    "    if cv2.waitKey(1)& 0xFF== ord('q'):\n",
    "        break\n",
    "        \n",
    "cap.release\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
