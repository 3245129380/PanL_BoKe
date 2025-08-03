import markdown as md
import re

def convert_markdown_to_html(markdown_text: str) -> str:
    """
    Convert markdown text to HTML
    """
    # Convert markdown to HTML
    html = md.markdown(markdown_text, extensions=['fenced_code', 'codehilite'])
    return html

def extract_code_blocks(markdown_text: str) -> list:
    """
    Extract code blocks from markdown text
    """
    # Regular expression to match code blocks
    code_block_pattern = r"```(\w*)\n([\s\S]*?)```"
    code_blocks = re.findall(code_block_pattern, markdown_text)
    return code_blocks

def sanitize_html(html: str) -> str:
    """
    Sanitize HTML to prevent XSS attacks
    """
    # Remove script tags
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Remove on* attributes
    html = re.sub(r'\s*on\w+\s*=\s*"[^"]*"', '', html, flags=re.IGNORECASE)
    html = re.sub(r"\s*on\w+\s*=\s*'[^']*'", '', html, flags=re.IGNORECASE)
    return html