import customtkinter as ctk
from tkinter import messagebox

# Caesar cipher logic
alphabet = list("abcdefghijklmnopqrstuvwxyz")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter.lower() not in alphabet:
            output_text += letter
        else:
            is_upper = letter.isupper()
            lower_letter = letter.lower()
            shifted_index = (alphabet.index(lower_letter) + shift_amount) % 26
            shifted_letter = alphabet[shifted_index]
            output_text += shifted_letter.upper() if is_upper else shifted_letter
    return output_text

# Run cipher and update output box
def run_cipher():
    text = message_input.get("0.0", "end").strip()
    shift = shift_input.get()
    direction = direction_option.get()

    if not shift.isdigit():
        messagebox.showerror("Invalid Input", "Shift must be a number.")
        return

    result = caesar(text, int(shift), direction)
    result_output.configure(state="normal")
    result_output.delete("0.0", "end")
    result_output.insert("0.0", result)
    result_output.configure(state="disabled")

def clear_fields():
    message_input.delete("0.0", "end")
    shift_input.delete(0, "end")
    result_output.configure(state="normal")
    result_output.delete("0.0", "end")
    result_output.configure(state="disabled")
    direction_option.set("encode")

# ---------- UI Design ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Caesar Cipher - Modern UI")
app.geometry("700x650")

# Title
title_label = ctk.CTkLabel(app, text="🔐 Caesar Cipher", font=("Helvetica Neue", 26, "bold"))
title_label.pack(pady=20)

# Main Frame
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Mode Dropdown
ctk.CTkLabel(frame, text="Select Mode", font=("Segoe UI", 16)).pack(anchor="w", padx=15, pady=(15, 0))
direction_option = ctk.StringVar(value="encode")
ctk.CTkOptionMenu(frame, variable=direction_option, values=["encode", "decode"]).pack(padx=15, pady=5, fill="x")

# Shift Input
ctk.CTkLabel(frame, text="Shift Number", font=("Segoe UI", 16)).pack(anchor="w", padx=15, pady=(10, 0))
shift_input = ctk.CTkEntry(frame, placeholder_text="e.g. 3")
shift_input.pack(padx=15, pady=5, fill="x")

# Message Input
ctk.CTkLabel(frame, text="Enter Your Message", font=("Segoe UI", 16)).pack(anchor="w", padx=15, pady=(10, 0))
message_input = ctk.CTkTextbox(frame, height=100)
message_input.pack(padx=15, pady=5, fill="x")

# Run & Clear Buttons
btn_frame = ctk.CTkFrame(frame, fg_color="transparent")
btn_frame.pack(pady=10)
ctk.CTkButton(btn_frame, text="Run Cipher", command=run_cipher, width=150).grid(row=0, column=0, padx=10)
ctk.CTkButton(btn_frame, text="Clear", command=clear_fields, fg_color="gray", width=100).grid(row=0, column=1, padx=10)

# Output Section
ctk.CTkLabel(frame, text="Result", font=("Segoe UI", 16)).pack(anchor="w", padx=15, pady=(10, 0))
result_output = ctk.CTkTextbox(frame, height=100, state="disabled")
result_output.pack(padx=15, pady=5, fill="x")

# Footer
footer = ctk.CTkLabel(app, text="Made with ❤️ using customtkinter", font=("Segoe UI", 12), text_color="gray")
footer.pack(pady=5)

app.mainloop()
