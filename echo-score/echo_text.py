"""Normalize game OCR text before matching Echo UI and scoring templates."""

from functools import lru_cache


# These characters cover the Echo panels when OpenCC is unavailable (for
# example, an older host installation). OpenCC handles full character names.
_ECHO_TRADITIONAL = str.maketrans({
    "聲": "声", "強": "强", "並": "并", "調": "调", "諧": "谐",
    "鳴": "鸣", "裝": "装", "備": "备", "戰": "战", "擊": "击",
    "傷": "伤", "療": "疗", "禦": "御", "護": "护", "體": "体",
    "屬": "属", "導": "导", "電": "电", "氣": "气", "動": "动",
    "滅": "灭", "熱": "热", "釋": "释", "寧": "宁", "婭": "娅",
    "達": "达", "貝": "贝", "霽": "霁", "聖": "圣", "蘿": "萝",
    "麗": "丽", "爾": "尔", "維": "维", "愛": "爱", "彌": "弥",
    "擇": "择", "選": "选", "項": "项", "檔": "档", "滿": "满",
})


@lru_cache(maxsize=1)
def _converter():
    try:
        from opencc import OpenCC
    except ImportError:
        return None
    return OpenCC("t2s")


def simplify_echo_text(text):
    """Convert Traditional Chinese OCR to the Simplified labels used by XWUID."""
    # PaddleOCR sometimes uses the Japanese glyph 撃 for 擊 in Traditional
    # Chinese stat labels (暴撃 / 攻撃). OpenCC does not normalize that glyph.
    text = str(text).replace("撃", "擊")
    converter = _converter()
    return converter.convert(text) if converter is not None else text.translate(_ECHO_TRADITIONAL)
