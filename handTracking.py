import cv2
import mediapipe as mp
import pyautogui
import math

# Get screen resolution
screen_width, screen_height = pyautogui.size()

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror image
    frame_height, frame_width, _ = frame.shape

    # Convert BGR to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    # Process hand landmarks
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm_list = hand_landmarks.landmark

            # Get index finger tip (landmark 8)
            index_x = int(lm_list[8].x * frame_width)
            index_y = int(lm_list[8].y * frame_height)

            # Get thumb tip (landmark 4)
            thumb_x = int(lm_list[4].x * frame_width)
            thumb_y = int(lm_list[4].y * frame_height)

            # Draw fingertip circles
            cv2.circle(frame, (index_x, index_y), 10, (255, 0, 0), -1)  # Blue: Index
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), -1)  # Green: Thumb

            # Draw a line between thumb and index
            cv2.line(frame, (index_x, index_y), (thumb_x, thumb_y), (0, 255, 255), 2)

            # Calculate screen coords for index tip
            screen_x = int(lm_list[8].x * screen_width)
            screen_y = int(lm_list[8].y * screen_height)

            # Move the mouse
            pyautogui.moveTo(screen_x, screen_y)q

            # Check distance between index and thumb tips
            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

            if distance < 40:
                pyautogui.click()
                cv2.putText(frame, "Click!", (index_x + 20, index_y - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Draw hand landmarks and connections
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show the frame in a window
    cv2.imshow("Virtual Mouse", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
cv2.destroyAllWindows()
