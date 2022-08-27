import os
import pendulum


# directory path
PROJECT_ROOT_DIR = os.path.dirname(__file__)
LOG_ROOT_DIR = os.path.join(PROJECT_ROOT_DIR, "logs")
IMAGE_FILE_ROOT_DIR = os.path.join("/home/smheo/MinjiDotComDataDir/image")
IMAGE_FILE_DIR_FOR_TASTING_NOTE = os.path.join("/home/smheo/MinjiDotComDataDir/image/TastingNote")

# timezone
KST = pendulum.timezone("Asia/Seoul")
