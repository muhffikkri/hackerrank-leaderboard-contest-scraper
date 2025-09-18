import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
from dotenv import load_dotenv, set_key
import threading
import main

class ContestScraperGUI(tk.Tk):
    def gui_scrape(self):
        # Ambil data dari input
        email = self.email_var.get()
        password = self.password_var.get()
        contest_link = self.contest_link_var.get()
        # Simpan ke .env agar konsisten
        env_path = os.path.join(os.getcwd(), '.env')
        set_key(env_path, 'HACKERRANK_USERNAME', email)
        set_key(env_path, 'HACKERRANK_PASSWORD', password)
        set_key(env_path, 'CONTEST_LINK', contest_link)

        # Redirect print ke log area
        import sys
        class PrintLogger:
            def __init__(self, append_func):
                self.append_func = append_func
            def write(self, msg):
                if msg.strip():
                    self.append_func(msg + '\n')
            def flush(self):
                pass
        old_stdout = sys.stdout
        sys.stdout = PrintLogger(self.append_log)
        try:
            main.main()
        except Exception as e:
            self.append_log(f"Error: {e}\n")
        finally:
            sys.stdout = old_stdout
    def __init__(self):
        super().__init__()
        self.title("Hackerrank Leaderboard Contest Scraper")
        self.geometry("800x600")
        self.resizable(False, False)
        self.create_tabs()

    def create_tabs(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)

        # Home Tab
        self.home_tab = ttk.Frame(notebook)
        notebook.add(self.home_tab, text='Home')
        self.create_home_tab()

        # Settings Tab
        self.settings_tab = ttk.Frame(notebook)
        notebook.add(self.settings_tab, text='Settings')
        self.create_settings_tab()

        # Results Tab
        self.results_tab = ttk.Frame(notebook)
        notebook.add(self.results_tab, text='Results')
        self.create_results_tab()

        # Help Tab
        self.help_tab = ttk.Frame(notebook)
        notebook.add(self.help_tab, text='Help')
        self.create_help_tab()

    def create_home_tab(self):
        load_dotenv()
        # Contest Link Input
        ttk.Label(self.home_tab, text="Contest Link:").pack(pady=(20,5), padx=20, anchor='w')
        self.contest_link_var = tk.StringVar(value=os.getenv('CONTEST_LINK', ''))
        ttk.Entry(self.home_tab, textvariable=self.contest_link_var, width=80).pack(pady=(0,15), padx=20, anchor='w')
        # Start Button
        ttk.Button(self.home_tab, text="Start Scraping", command=self.start_scraping, style="Start.TButton").pack(pady=(0,20), padx=20, anchor='w')
        # Log Output
        ttk.Label(self.home_tab, text="Log Output:").pack(pady=(0,5), padx=20, anchor='w')
        self.log_text = tk.Text(self.home_tab, height=18, width=90, state='disabled')
        self.log_text.pack(pady=(0,20), padx=20)
        # Custom style for button
        style = ttk.Style()
        style.configure("Start.TButton", padding=8)

    def append_log(self, text):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, text)
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')

    def create_settings_tab(self):
        load_dotenv()
        ttk.Label(self.settings_tab, text="Email:").pack(pady=(20,5), padx=20, anchor='w')
        self.email_var = tk.StringVar(value=os.getenv('HACKERRANK_USERNAME', ''))
        ttk.Entry(self.settings_tab, textvariable=self.email_var, width=50).pack(pady=(0,15), padx=20, anchor='w')
        ttk.Label(self.settings_tab, text="Password:").pack(pady=(0,5), padx=20, anchor='w')
        self.password_var = tk.StringVar(value=os.getenv('HACKERRANK_PASSWORD', ''))
        ttk.Entry(self.settings_tab, textvariable=self.password_var, show='*', width=50).pack(pady=(0,15), padx=20, anchor='w')
        ttk.Label(self.settings_tab, text="Contest Link:").pack(pady=(0,5), padx=20, anchor='w')
        self.settings_contest_link_var = tk.StringVar(value=os.getenv('CONTEST_LINK', ''))
        ttk.Entry(self.settings_tab, textvariable=self.settings_contest_link_var, width=80).pack(pady=(0,15), padx=20, anchor='w')
        ttk.Button(self.settings_tab, text="Save Settings", command=self.save_settings, style="Save.TButton").pack(pady=(0,20), padx=20)
        style = ttk.Style()
        style.configure("Save.TButton", padding=8)

    def save_settings(self):
        env_path = os.path.join(os.getcwd(), '.env')
        set_key(env_path, 'HACKERRANK_USERNAME', self.email_var.get())
        set_key(env_path, 'HACKERRANK_PASSWORD', self.password_var.get())
        set_key(env_path, 'CONTEST_LINK', self.settings_contest_link_var.get())
        # Update contest link in Home tab
        self.contest_link_var.set(self.settings_contest_link_var.get())
        messagebox.showinfo("Settings", "Email, password, dan contest link berhasil disimpan ke .env")

    def create_results_tab(self):
        ttk.Label(self.results_tab, text="Results Files:").pack(pady=(20,5), padx=20, anchor='w')
        self.results_listbox = tk.Listbox(self.results_tab, width=80, height=15)
        self.results_listbox.pack(pady=(0,15), padx=20)
        ttk.Button(self.results_tab, text="Refresh List", command=self.refresh_results_list).pack(pady=(0,10), padx=20, anchor='w')
        ttk.Button(self.results_tab, text="Show File Info", command=self.show_file_info).pack(pady=(0,10), padx=20, anchor='w')
        self.file_info_label = ttk.Label(self.results_tab, text="")
        self.file_info_label.pack(pady=(0,20), padx=20, anchor='w')
        self.refresh_results_list()

    def refresh_results_list(self):
        self.results_listbox.delete(0, tk.END)
        results_dir = os.path.join(os.getcwd(), 'results')
        if not os.path.exists(results_dir):
            self.file_info_label.config(text="No results folder found.")
            return
        files = [f for f in os.listdir(results_dir) if f.endswith('.csv')]
        for f in files:
            self.results_listbox.insert(tk.END, f)
        if not files:
            self.file_info_label.config(text="No result files found.")
        else:
            self.file_info_label.config(text="Select a file and click 'Show File Info'.")

    def show_file_info(self):
        selection = self.results_listbox.curselection()
        if not selection:
            messagebox.showwarning("No file selected", "Please select a file.")
            return
        filename = self.results_listbox.get(selection[0])
        filepath = os.path.join(os.getcwd(), 'results', filename)
        try:
            import pandas as pd
            import time
            start_time = os.path.getctime(filepath)
            end_time = os.path.getmtime(filepath)
            df = pd.read_csv(filepath)
            duration = end_time - start_time
            info = f"File: {filename}\nRows: {len(df)}\nStart: {time.ctime(start_time)}\nEnd: {time.ctime(end_time)}\nDuration: {duration:.2f} seconds"
            self.file_info_label.config(text=info)
        except Exception as e:
            self.file_info_label.config(text=f"Error reading file: {e}")

    def create_help_tab(self):
        help_text = (
            "Aplikasi ini digunakan untuk mengambil data leaderboard kontes Hackerrank secara otomatis.\n\n"
            "Tab Home: Masukkan link kontes dan mulai scraping.\n"
            "Tab Settings: Simpan email dan password ke .env.\n"
            "Tab Results: Lihat file hasil scraping dan info durasi pengambilan data.\n"
            "Tab Help: Petunjuk penggunaan dan deskripsi aplikasi.\n\n"
            "Pastikan sudah mengisi email, password, dan link kontes dengan benar sebelum mulai scraping."
        )
        tk.Label(self.help_tab, text=help_text, justify='left', anchor='nw').pack(padx=20, pady=(20,10), fill='both')

    def start_scraping(self):
        self.log_text.config(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state='disabled')
        self.append_log("Scraping started...\n")
        self.append_log(f"Contest link: {self.contest_link_var.get()}\n")
        # Jalankan scraping di thread terpisah agar GUI tidak freeze
        t = threading.Thread(target=self.gui_scrape)
        t.start()

if __name__ == "__main__":
    app = ContestScraperGUI()
    app.mainloop()
