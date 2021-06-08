import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
	while cap.isOpened():
		ret, frame = cap.read()

		# 🌈 Changing color code for processing
		image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		
		# 🚩 Set Flag
		image.flags.writeable = False
		
		# 🤚 Detection
		result = hands.process(image)

		# 🔙 Revert Flag and color
		image.flags.writeable = False
		image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

		#Value of all hand value added
		total = 0
		if result.multi_hand_landmarks:
			for count, hand in enumerate(result.multi_hand_landmarks):
				
				# ✌ Raised Fingers (True -> Raised | False -> Not raised)
				# https://google.github.io/mediapipe/solutions/hands.html#hand-landmark-model
				thumb = hand.landmark[4].y < hand.landmark[5].y 
				index = hand.landmark[8].y < hand.landmark[7].y 
				middle = hand.landmark[12].y < hand.landmark[11].y 
				ring = hand.landmark[16].y < hand.landmark[15].y 
				pinky = hand.landmark[20].y < hand.landmark[19].y 
				
				# ➕ Binary operation
				num = 1 * thumb + 2 * index + 4 * middle + 8 * ring + 16 * pinky
				total += num
				# 🗺 Coords of actual hand 
				coords = int(hand.landmark[0].x*image.shape[1] - 50), int(hand.landmark[0].y*image.shape[0] + 20)

				# ✏ Drawing
				mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
				text = 'Hand '+str(count+1)+": "+str(num)
				cv2.putText(image,text, coords, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255, 2))

		# ✏ Draw total
		cv2.putText(image,str(total), (50,50), cv2.FONT_ITALIC, 0.5, (255,0,0), 2)


		# 💻 Display on screen!
		cv2.imshow("Hand Binary Counter", image)

		# ⌨ Keyboard exit
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break

cap.release()
cv2.destroyAllWindows()
