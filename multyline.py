from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_wrapped_text(c, text, x, y, max_width):
    lines = []
    words = text.split(' ')
    line = ''
    for word in words:
        test_line = line + word + ' '
        if c.stringWidth(test_line) <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word + ' '
    lines.append(line)

    for line in lines:
        c.drawString(x, y, line)
        y -= 15  # Смещение на новую строку

# Создание объекта canvas
c = canvas.Canvas("example_canvas.pdf", pagesize=letter)

# Задание начальной позиции и ширины текста
x, y = 50, 750
max_width = 500

# Текст для вставки
text = """
This text will automatically wrap to a new line if it does not fit on the current line.
You can add long text here to see how auto-wrapping works using canvas in ReportLab.
"""

# Вызов функции для рисования текста с автопереносом строк
draw_wrapped_text(c, text, x, y, max_width)

# Сохранение PDF-документа
c.save()