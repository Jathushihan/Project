import tkinter as tk
from tkinter import simpledialog

class EventManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Manager")

        self.events = []  # List to store events and their counts

        # Frame for event input and buttons
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.event_input = tk.Entry(self.input_frame, width=25)
        self.event_input.grid(row=0, column=0, padx=5)

        self.add_event_btn = tk.Button(self.input_frame, text="Add Event", command=self.add_event)
        self.add_event_btn.grid(row=0, column=1, padx=5)

        # Frame for event list
        self.event_list_frame = tk.Frame(self.root)
        self.event_list_frame.pack(pady=10)

    def add_event(self):
        event_name = self.event_input.get().strip()
        if event_name:  # Ensure input is not empty
            event = {"name": event_name, "count": 0}
            self.events.append(event)
            self.refresh_events()
            self.event_input.delete(0, tk.END)

    def refresh_events(self):
        # Clear the frame
        for widget in self.event_list_frame.winfo_children():
            widget.destroy()

        for i, event in enumerate(self.events):
            # Event name
            name_label = tk.Label(self.event_list_frame, text=event["name"], width=20, anchor="w")
            name_label.grid(row=i, column=0, padx=5, pady=2)

            # Rename button
            rename_btn = tk.Button(self.event_list_frame, text="Rename", command=lambda idx=i: self.rename_event(idx))
            rename_btn.grid(row=i, column=1, padx=5)

            # Minus button
            minus_btn = tk.Button(self.event_list_frame, text="-", command=lambda idx=i: self.update_count(idx, -1))
            minus_btn.grid(row=i, column=2, padx=5)

            # Counter label
            count_label = tk.Label(self.event_list_frame, text=event["count"], width=5, anchor="center")
            count_label.grid(row=i, column=3, padx=5)

            # Plus button
            plus_btn = tk.Button(self.event_list_frame, text="+", command=lambda idx=i: self.update_count(idx, 1))
            plus_btn.grid(row=i, column=4, padx=5)

            # Move Up button
            move_up_btn = tk.Button(self.event_list_frame, text="↑", command=lambda idx=i: self.move_event(idx, -1))
            move_up_btn.grid(row=i, column=5, padx=5)

            # Move Down button
            move_down_btn = tk.Button(self.event_list_frame, text="↓", command=lambda idx=i: self.move_event(idx, 1))
            move_down_btn.grid(row=i, column=6, padx=5)

            # Delete button
            delete_btn = tk.Button(self.event_list_frame, text="Delete", command=lambda idx=i: self.delete_event(idx))
            delete_btn.grid(row=i, column=7, padx=5)

    def update_count(self, idx, delta):
        self.events[idx]["count"] += delta
        self.refresh_events()

    def rename_event(self, idx):
        new_name = simpledialog.askstring("Rename Event", "Enter new name:")
        if new_name:
            self.events[idx]["name"] = new_name
            self.refresh_events()

    def move_event(self, idx, direction):
        new_idx = idx + direction
        if 0 <= new_idx < len(self.events):
            self.events[idx], self.events[new_idx] = self.events[new_idx], self.events[idx]
            self.refresh_events()

    def delete_event(self, idx):
        del self.events[idx]
        self.refresh_events()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagerApp(root)
    root.mainloop()
