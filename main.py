import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
import fitz

def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_document = fitz.open(file_path)
        num_pages = pdf_document.page_count
        
        

        root = tk.Tk()
        root.title("PDF Viewer")
        
        

        notebook = ttk.Notebook(root )
        notebook.pack(fill='both', expand=True)

        for page_num in range(num_pages):
            page = pdf_document[page_num]
            text = page.get_text()

            text_widget = tk.Text(notebook)
            text_widget.insert('1.0', text)
            text_widget.config(state='disabled')

            notebook.add(text_widget, text=f'Page {page_num + 1}')

        root.mainloop()

if __name__ == "__main__":
    open_pdf()

