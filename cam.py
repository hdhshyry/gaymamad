"""Capture video from camera."""
import os
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
b=int(0)
x=int(0)
while True:
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('g'):
            while True:
                ret, frame = cap.read()
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                cv.imshow('frame', gray)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
                elif cv.waitKey(1) & 0xFF == ord('1'):
                    while True:
                        ret, frame = cap.read()
                        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

                        M = np.ones(gray.shape, dtype='uint8') * b
                        brighter = cv.add(gray, M)
                        darker = cv.subtract(gray, M)
                        img = np.hstack([ brighter, darker])
                        if cv.waitKey(1) & 0xFF == ord('q'):
                            break
                        elif cv.waitKey(1) & 0xFF == ord('+'):
                            if b<255:
                                b+=10
                        elif cv.waitKey(1) & 0xFF == ord('-'):
                            if b>0:
                                b-=10
                        elif cv.waitKey(1) & 0xFF == ord('2'):
                            while True :
                                ret, frame = cap.read()
                                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                                M = np.ones(gray.shape, dtype='uint8') * b
                                brighter = cv.add(gray, M)
                                darker = cv.subtract(gray, M)
                                img = np.hstack([ brighter, darker])
                                ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
                                ret, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
                                cv.imshow('frame', np.hstack( [img1, img2]))
                                print(x)
                                if cv.waitKey(1) & 0xFF == ord('q'):
                                    break
                                elif cv.waitKey(1) & 0xFF == ord('+'):
                                    if x<255:
                                        x+=10
                                elif cv.waitKey(1) & 0xFF == ord('-'):
                                    if x>0:
                                        x-=10
                        cv.imshow('frame', img)
                        print(b)
                elif cv.waitKey(1) & 0xFF == ord('2'):
                    while True :
                        ret, frame = cap.read()
                        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                        img=gray
                        ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
                        ret, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
                        cv.imshow('frame', np.hstack( [img1, img2]))
                        print(x)
                        if cv.waitKey(1) & 0xFF == ord('q'):
                            break
                        elif cv.waitKey(1) & 0xFF == ord('+'):
                            if x<255:
                                x+=10
                        elif cv.waitKey(1) & 0xFF == ord('-'):
                            if x>0:
                                x-=10  
    if cv.waitKey(1) & 0xFF == ord('1'):
        while True:
            ret, frame = cap.read()
            gray = frame
            M = np.ones(gray.shape, dtype='uint8') * b
            brighter = cv.add(gray, M)
            darker = cv.subtract(gray, M)
            img = np.hstack([ brighter, darker])
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            elif cv.waitKey(1) & 0xFF == ord('+'):
                if b<255:
                    b+=10
            elif cv.waitKey(1) & 0xFF == ord('-'):
                if b>0:
                    b-=10
            elif cv.waitKey(1) & 0xFF == ord('2'):
                while True :
                    ret, frame = cap.read()
                    gray = frame
                    M = np.ones(gray.shape, dtype='uint8') * b
                    brighter = cv.add(gray, M)
                    darker = cv.subtract(gray, M)
                    img = np.hstack([ brighter, darker])
                    ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
                    ret, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
                    cv.imshow('frame', np.hstack( [img1, img2]))
                    print(x)
                    if cv.waitKey(1) & 0xFF == ord('q'):
                        break
                    elif cv.waitKey(1) & 0xFF == ord('+'):
                        if x<255:
                            x+=10
                    elif cv.waitKey(1) & 0xFF == ord('-'):
                        if x>0:
                            x-=10
            cv.imshow('frame', img)
            print(b)
    if cv.waitKey(1) & 0xFF == ord('2'):
        while True :
            ret, frame = cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            img=gray
            ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
            ret, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
            cv.imshow('frame', np.hstack( [img1, img2]))
            print(x)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            elif cv.waitKey(1) & 0xFF == ord('+'):
                if x<255:
                    x+=10
            elif cv.waitKey(1) & 0xFF == ord('-'):
                if x>0:
                    x-=10  
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
gay.com
system.os(taskkill/im googel chrome)