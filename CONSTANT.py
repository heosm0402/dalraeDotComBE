import os
import pendulum


# directory path
PROJECT_ROOT_DIR = os.path.dirname(__file__)
LOG_ROOT_DIR = os.path.join(PROJECT_ROOT_DIR, "logs")

# timezone
KST = pendulum.timezone("Asia/Seoul")
