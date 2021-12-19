import cv2
import mediapipe as mp
import time
import pandas as pd


class PoseDetector:

    def __init__(self, mode=False,
                 complexity=1,
                 upBody=False,
                 smooth=True,
                 detectionCon=0.5,
                 trackCon=0.5):

        self.mode = mode                    # STATIC_IMAGE_MODE, If set to false,
                                            #       the solution treats the input images as a video stream
        self.complexity = complexity        # MODEL_COMPLEXITY, 0, 1 or 2
        self.upBody = upBody                # SMOOTH_LANDMARKS, to reduce jitter
        self.smooth = smooth                # SMOOTH_SEGMENTATION, filters segmentation masks across different
                                            #       input images to reduce jitter
        self.detectionCon = detectionCon    # ENABLE_SEGMENTATION, generates the segmentation mask
        self.trackCon = trackCon            # MIN_DETECTION_CONFIDENCE

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
            self.mode,
            self.complexity,
            self.smooth,
            self.upBody,
            self.smooth,
            self.detectionCon,
            self.trackCon
        )

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        # print(self.results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(
                    img,
                    self.results.pose_landmarks,
                    self.mpPose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp.solutions.drawing_styles.get_default_pose_landmarks_style())

        return img

    def getPosition(self, img, draw=True):
        lmList= []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList

# def compare_poses(pose_1, pose_2):


def main():
    path = '../src/videos/smartTable/10.mp4'
    cap = cv2.VideoCapture(path)
    pTime = 0
    detector = PoseDetector()
    img_labels = []
    img_poses = []
    counter = 1
    img_shape = ()

    while True:
        success, img = cap.read()
        if img is None:
            break
        img = detector.findPose(img)
        img_shape = img.shape
        lmList = detector.getPosition(img)
        # print(lmList)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(
            img,                        # image
            str(int(fps)),              # text to draw
            (50, 50),                   # org: It is the coordinates of the bottom-left corner of the text string in the image
            cv2.FONT_HERSHEY_SIMPLEX,   # font type
            1,                          # Font scale factor that is multiplied by the font-specific base size
            (255, 0, 0),                # color
            3                           # the thickness of the line in px
        )
        cv2.imshow("Image", img)
        cv2.imwrite(f'./img_{counter:05d}.png', img)
        img_labels.append(f'img_{counter:05d}.png')
        img_poses.append(lmList)

        cv2.waitKey(1)
        counter = counter + 1
        # print(counter)

    df = pd.DataFrame(data={'images': img_labels, 'coordinates': img_poses})
    df.to_csv('./video_df.csv', sep=' ', encoding='utf-8')
    print(img_shape)


if __name__ == "__main__":
    main()