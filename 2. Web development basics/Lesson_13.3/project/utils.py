def has_r(word):
    """Проверяет существование р в строке"""
    if type(word) != str:
        raise TypeError(f"Str expected got {type(word)} instead!")    
    return "р" in word.lower()
