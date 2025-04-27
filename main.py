def main():
    from ui.main_window import MainWindow
    import customtkinter as ctk

    app = ctk.CTk()
    MainWindow(app)
    app.mainloop()


if __name__ == "__main__":
    main()