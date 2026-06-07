import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

print("DeepSORT Installed Successfully")

# Load YOLO Model
model = YOLO("yolov8n.pt")

# Initialize DeepSORT
tracker = DeepSort(max_age=30)

# Store Unique Vehicle IDs
unique_vehicle_ids = set()

# Video Path
video_path = "data/videos/south.mp4"

# Open Video
import os

print("Current Working Directory:", os.getcwd())
print("Video Exists:", os.path.exists(video_path))
print("Video Path:", video_path)
cap = cv2.VideoCapture(video_path)

print("Video Opened:", cap.isOpened())

ret, test_frame = cap.read()

print("First Frame Read:", ret)

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Video Finished")
        break

    # YOLO Detection
    results = model(
        frame,
        conf=0.4
    )

    detections = []

    for r in results:

        for box in r.boxes:

            x1, y1, x2, y2 = box.xyxy[0]

            conf = float(box.conf[0])

            cls = int(box.cls[0])

            class_name = model.names[cls]

            if class_name in [
                "car",
                "truck",
                "bus",
                "motorcycle"
            ]:

                detections.append(
                    (
                        [
                            float(x1),
                            float(y1),
                            float(x2 - x1),
                            float(y2 - y1)
                        ],
                        conf,
                        class_name
                    )
                )

    print("Detections:", len(detections))

    # DeepSORT Tracking
    tracks = tracker.update_tracks(
        detections,
        frame=frame
    )

    print("Tracks:", len(tracks))

    # Draw Tracks
    for track in tracks:

        if not track.is_confirmed():
            continue

        track_id = track.track_id

        unique_vehicle_ids.add(track_id)

        ltrb = track.to_ltrb()

        x1, y1, x2, y2 = map(
            int,
            ltrb
        )

        # Bounding Box
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # Vehicle ID
        cv2.putText(
            frame,
            f"ID {track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    # Total Unique Vehicles
    cv2.putText(
        frame,
        f"Unique Vehicles: {len(unique_vehicle_ids)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Show Video
    cv2.imshow(
        "Vehicle Tracking",
        frame
    )

    # Exit Key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()

print(
    "\nTotal Unique Vehicles:",
    len(unique_vehicle_ids)
)