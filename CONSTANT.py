import os
import pendulum


# directory path
PROJECT_ROOT_DIR = os.path.dirname(__file__)
LOG_ROOT_DIR = os.path.join(PROJECT_ROOT_DIR, "logs")
IMAGE_FILE_ROOT_DIR = os.path.join("/home/smheo/MinjiDotComDataDir/image")
# timezone
KST = pendulum.timezone("Asia/Seoul")
