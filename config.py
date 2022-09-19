import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCzrVBzcdIRtPShiKLf-RkWv8Oq4REUIifZp1Cj5EgS4DHwHcRcv9nQX1w0i80v1un9vTx4Ko0PB2xO3WsxyRDc_KYDztnWn-lSIH0GZSKv94tg7emXPR3-seh4ecXZ_dsaOt5wviX99YElFDUzxGySgbrPji-Jf5xPm0ZNe52fw0IdNxhQ1g8KDFhfYYjBMa95e294kN34Tq-U8Ro-rs3IWf9xRWqgJTBrkcwQCoPwoIgxgrObd65WR13Zkb-WwqCwS0wMohSfvUi4ze0nMF3-G1hNIz-ynWydysQRUG6hk_bwQj1k1oUrXxcDxoA3ls4wdWhtFBOK0xQKYQjL6bHuAAAAAS2x9lYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5609488881:AAHQ3dPYCnBFwEL4GO8BqTGEOMrsJqv2Mn4")
BOT_NAME = getenv("BOT_NAME", "Mahsoom Music X")
API_ID = int(getenv("API_ID", "10285297"))
API_HASH = getenv("API_HASH", "61bb4a53f4597d71245270a00100f736")
OWNER_NAME = getenv("OWNER_NAME", "Call_me_futurepilot")
ALIVE_NAME = getenv("ALIVE_NAME", "Mahsoom Music X")
BOT_USERNAME = getenv("BOT_USERNAME", "Mahsoom_MusicX_RoBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Mahsoom_MusicX")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Noob_Editor_Tutoriyal")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mahsoombotupdate")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5061604950 5176081390").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/28be3d5d723b1e6c4b2b3.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "6000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ghostfathigang/music-video-streamer")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/28be3d5d723b1e6c4b2b3.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/28be3d5d723b1e6c4b2b3.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/28be3d5d723b1e6c4b2b3.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/28be3d5d723b1e6c4b2b3.jpg")
