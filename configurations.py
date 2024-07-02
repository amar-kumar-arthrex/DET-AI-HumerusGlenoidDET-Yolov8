from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
RTSP = 'RTSP'
WEBCAM = 'Webcam'



SOURCES_LIST = [IMAGE, VIDEO, RTSP,WEBCAM]

# ML Model config

MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'

# Webcam
WEBCAM_PATH = 0