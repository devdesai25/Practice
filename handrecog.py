import cv2
import mediapipe as mp
import time

"""mp_hand = mp.solutions.hand
hands = mp_hand.Hands()
"""

mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5

)
mp_drawing_utils = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)
prev_time = 0
while True:

    success, img = cap.read( )

    if not success:
        break


    "result = hands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))  "  
    result = holistic_model.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

    #print(result.multi_hand_landmarks)
    "if result.left_hand_landmakrs:"
        
    """if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks :
            mp_drawing_utils.draw_landmarks(img,hand_landmark,mp_hand.HAND_CONNECTIONS)
    """
    mp_drawing_utils.draw_landmarks(
        img,
        result.face_landmarks,
        mp_holistic.FACEMESH_CONTOURS,
        mp_drawing_utils.DrawingSpec(color=(255,0,255),thickness=1,circle_radius=1),
        mp_drawing_utils.DrawingSpec(color=(0,255,255),thickness=1,circle_radius=1)
    )

    mp_drawing_utils.draw_landmarks(
        img,
        result.right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS
    )

    mp_drawing_utils.draw_landmarks(
        img,
        result.left_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS
    )

    cur_time = time.time()
    FPS = int(1/(cur_time-prev_time))
    prev_time = cur_time

    cv2.putText(img,f"FPS : {str(FPS)}",(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(200,0,250),3)


    cv2.imshow("Image",img)
    cv2.waitKey(1)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()  