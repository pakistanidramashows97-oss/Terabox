import re

TERABOX_PATTERN = r"(https?://(?:www\.)?(terabox|1024terabox|teraboxapp|nephobox|freeterabox)\.com/\S+)"

DISKWALA_PATTERN = r"(https?://(?:www\.)?diskwala\.com/\S+)"

def detect_link(text):

    if re.search(TERABOX_PATTERN, text):
        return "terabox"

    if re.search(DISKWALA_PATTERN, text):
        return "diskwala"

    return None
