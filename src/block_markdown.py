from block_type import BlockType
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE_BLOCK
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def heading_to_html_node(block):
    heading_level = len(block) - len(block.lstrip("#"))
    tag = f"h{heading_level}"
    content = block[heading_level + 1:].strip()
    return ParentNode(tag=tag, children=text_to_children(content))

def code_block_to_html_node(block):
    lines = block.split("\n")
    content = TextNode("\n".join(lines[1:-1]), TextType.TEXT)
    wrapped_content = ParentNode(tag="pre", children=[LeafNode("code", content.text)])
    return wrapped_content
    
def blockquote_to_html_node(block):
    lines = block.strip().split("\n")
    quote_lines = []

    for line in lines:
        line = line.lstrip()
        if not line.startswith(">"):
            continue

        # Remove leading '>' and following space if present
        content = line[1:]
        if content.startswith(" "):
            content = content[1:]

        # If it's just a blank '>' line, preserve it as empty paragraph break
        quote_lines.append(content)

    # Rejoin and split into paragraphs on *true* blank lines (now preserved)
    quote_text = "\n".join(quote_lines)
    paragraphs = quote_text.split("\n\n")

    blockquote_children = []
    for para in paragraphs:
        if not para.strip():
            continue
        inline_nodes = text_to_children(para.strip())
        blockquote_children.append(ParentNode(tag="p", children=inline_nodes))

    return ParentNode(tag="blockquote", children=blockquote_children)

# def unordered_list_to_html_node(block):


# def ordered_list_to_html_node(block):


def paragraph_block_to_html_node(block):
    paragraphs = block.strip().split("\n\n")
    nodes = []

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        content = TextNode(para, TextType.TEXT)
        p_node = ParentNode(tag="p", children=text_to_children(content.text))
        nodes.append(p_node)

    return nodes


# def markdown_to_html_node(markdown):
#     blocks = markdown_to_blocks(markdown)
#     block_nodes = []

#     for block in blocks:
#         block_type = block_to_block_type(block)

        
