def divide_text(texto: str, max_s: int) -> list[str]:
    words = texto.split()
    chunks = []
    chunk_current = ""
    for word in words:
        if len(chunk_current) + len(word) <= max_s:
            chunk_current += word + " "
        else:
            chunks.append(chunk_current.strip())
            chunk_current = word + " "
    
    chunks.append(chunk_current.strip())
    
    return chunks