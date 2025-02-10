from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_wrapped_text(c, text, x, y, max_width):
    """
    Draws text on the canvas, wrapping it to a new line if it exceeds the maximum width.

    Parameters:
    c (canvas.Canvas): The canvas object to draw on.
    text (str): The text to be drawn.
    x (int): The x-coordinate of the starting position.
    y (int): The y-coordinate of the starting position.
    max_width (int): The maximum width of the text before wrapping to a new line.
    """
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

    for wrapped_line in lines:
        c.drawString(x, y, wrapped_line)
        y -= 15  # Move to a new line

# Создание объекта canvas
c = canvas.Canvas("example_canvas.pdf", pagesize=letter)

# Задание начальной позиции и ширины текста
x, y = 50, 750
max_width = 500

# Текст для вставки
text = """This text will automatically wrap to a new line if it does not fit on the current line.
You can add long text here to see how auto-wrapping works using canvas in ReportLab."""

# Вызов функции для рисования текста с автопереносом строк
draw_wrapped_text(c, text, x, y, max_width)

# Сохранение PDF-документа
c.save()
