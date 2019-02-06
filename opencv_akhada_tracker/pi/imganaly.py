# color analysis hunxa ya
# r g b color ko contour patta lagauni
# ani contour area calculate garni
# jasto ki blue ra green ko contour 1000 vanda badi xa vane back off
# ani red ko kam xa vane forward jani
# sidhai dabdini ho

# flag use garnu parxa jata tatai


#red matrai xutana paro ni hoina? 
# green ra blue ni xa 2k


def segment_colour(frame):
    hsv_roi =  cv2.cvtColor(frame, cv2.cv.CV_BGR2HSV)
    mask_1 = cv2.inRange(hsv_roi, np.array([160, 160,10]), np.array([190,255,255]))
    ycr_roi=cv2.cvtColor(frame,cv2.cv.CV_BGR2YCrCb)
    mask_2=cv2.inRange(ycr_roi, np.array((0.,165.,0.)), np.array((255.,255.,255.)))
    mask = mask_1 | mask_2
    kern_dilate = np.ones((8,8),np.uint8)
    kern_erode  = np.ones((3,3),np.uint8)
    mask= cv2.erode(mask,kern_erode)      #Eroding lminima
    mask=cv2.dilate(mask,kern_dilate)     #Dilating
    cv2.imshow('mask',mask)
    return mask

