import cv2
from ultralytics import YOLO
import csv
import os

# Load YOLO Model
model = YOLO("yolov8n.pt")

# Base Directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Results Folder
results_dir = os.path.join(
    BASE_DIR,
    "results"
)

os.makedirs(
    results_dir,
    exist_ok=True
)

csv_file = os.path.join(
    results_dir,
    "traffic_data.csv"
)

# Four Direction Videos
videos = {
    "North": "data/videos/north.mp4",
    "South": "data/videos/south.mp4",
    "East": "data/videos/east.mp4",
    "West": "data/videos/west.mp4"
}

# Create CSV Header
with open(
    csv_file,
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Direction",
        "Cars",
        "Bikes",
        "Buses",
        "Trucks",
        "Total",
        "Density"
    ])

# Process All Videos
for direction, video_path in videos.items():

    print(f"\nProcessing {direction}")

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():

        print(f"Cannot Open {video_path}")

        continue

    frame_count = 0
    MAX_FRAMES = 500

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        if frame_count > MAX_FRAMES:

            print(
                f"{direction}: {MAX_FRAMES} frames processed"
            )

            break

        # YOLO Detection
        results = model(
            frame,
            conf=0.25
        )

        car_count = 0
        bike_count = 0
        bus_count = 0
        truck_count = 0

        for r in results:

            for box in r.boxes:

                cls = int(box.cls[0])

                class_name = model.names[cls]

                if class_name == "car":
                    car_count += 1

                elif class_name == "motorcycle":
                    bike_count += 1

                elif class_name == "bus":
                    bus_count += 1

                elif class_name == "truck":
                    truck_count += 1

        total = (
            car_count
            + bike_count
            + bus_count
            + truck_count
        )

        # Density
        if total < 15:

            density = "LOW"

        elif total < 30:

            density = "MEDIUM"

        else:

            density = "HIGH"

        # Save CSV
        with open(
            csv_file,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                direction,
                car_count,
                bike_count,
                bus_count,
                truck_count,
                total,
                density
            ])

        # Draw Detections
        annotated_frame = results[0].plot()

        cv2.putText(
            annotated_frame,
            f"Direction: {direction}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        cv2.putText(
            annotated_frame,
            f"Total: {total}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            annotated_frame,
            f"Density: {density}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.imshow(
            f"{direction} Traffic",
            annotated_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):

            cap.release()

            cv2.destroyAllWindows()

            exit()

    print(
        f"Finished Processing {direction}"
    )

    cap.release()

cv2.destroyAllWindows()

print(
    "\nAll Four Directions Processed Successfully"
)