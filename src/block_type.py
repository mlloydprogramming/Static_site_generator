from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE_BLOCK = "code_block"
    QUOTE = "quote" 
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    