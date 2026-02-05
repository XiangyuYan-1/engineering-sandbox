import tkinter as tk
from tkinter import ttk


interface = 0


def change_interface(n):
    global interface
    interface = n


def main():
    root = tk.Tk()
    root.title("Vote for your favorite food")
    root.geometry("900x520")
    root.minsize(820, 480)
    root.configure(bg="#03163D")

    # header
    header = tk.Frame(root, bg="#111827", padx=18, pady=14)
    header.pack(fill="x")

    if interface == 0:
        vote_button = ttk.Button(root, text="Vote", command=change_interface(1))
        result_button = ttk.Button(root, text="Results", command=change_interface(2))
        winner_button = ttk.Button(root, text="Winner", command=change_interface(3))

        vote_button.pack(ipadx=5, ipady=5, expand=True)
        result_button.pack(ipadx=5, ipady=5, expand=True)
        winner_button.pack(ipadx=5, ipady=5, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
