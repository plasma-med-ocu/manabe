import cv2
import numpy as np
camera=cv2.VideoCapture(1)
# 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
while True:
    ret, frame = camera.read()# フレームを取得 480*640*3 RGB
    if ret:
        #cv2.imshow('camera', frame)# フレームを画面に表示
        lower = np.array([100,0,120])
        upper = np.array([160,50,255])
        frame_mask = cv2.inRange(frame, lower, upper)
        dst = cv2.bitwise_and(frame, frame, mask=frame_mask)
        cv2.imshow('camera', dst)
        if np.min(dst)<50:
            print("\007")
    else:
        camera=cv2.VideoCapture(1)
 
    # キー操作があればwhileループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 
# 撮影用オブジェクトとウィンドウの解放
camera.release()
cv2.destroyAllWindows()