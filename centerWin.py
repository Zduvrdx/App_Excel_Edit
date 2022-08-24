def centerWindow(window):
    winHeight = window.winfo_height()
    WinWidht = window.winfo_width()
    # para criar a janela centralizada na tela
    janelaY = (window.winfo_screenheight() / 2) - (winHeight/2)
    janelaX = (window.winfo_screenwidth() / 2) - (WinWidht /2)
    window.geometry(f"{WinWidht}x{winHeight}+{int(janelaX)}+{int(janelaY)}")
    window.wm_maxsize(height=winHeight, width=WinWidht)