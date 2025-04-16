import cv2
import mediapipe as mp
import pyautogui
import math
import time

screen_width, screen_height = pyautogui.size()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_y = 0
scroll_mode = False
last_click_time = 0  # ← click delay timer

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            index_x, index_y = int(lm[8].x * w), int(lm[8].y * h)
            thumb_x, thumb_y = int(lm[4].x * w), int(lm[4].y * h)
            middle_x, middle_y = int(lm[12].x * w), int(lm[12].y * h)

            cv2.circle(frame, (index_x, index_y), 8, (255, 0, 0), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 8, (0, 255, 0), -1)
            cv2.circle(frame, (middle_x, middle_y), 8, (255, 255, 0), -1)

            screen_x = int(lm[8].x * screen_width)
            screen_y = int(lm[8].y * screen_height)
            pyautogui.moveTo(screen_x, screen_y)

            # ----- CLICK -----
            dist_click = math.hypot(index_x - thumb_x, index_y - thumb_y)
            current_time = time.time()
            if dist_click < 25 and (current_time - last_click_time) > 3:
                pyautogui.click()
                last_click_time = current_time
                cv2.putText(frame, "Click!", (index_x + 20, index_y - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # ----- SCROLL -----
            dist_scroll = math.hypot(index_x - middle_x, index_y - middle_y)
            if dist_scroll < 40:
                cv2.putText(frame, "Scroll Mode", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if not scroll_mode:
                    prev_y = index_y
                    scroll_mode = True
                else:
                    delta_y = index_y - prev_y
                    if abs(delta_y) > 5:
                        pyautogui.scroll(-int(delta_y * 5))
                        prev_y = index_y
            else:
                scroll_mode = False

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Mouse with Scroll & Click Delay", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
