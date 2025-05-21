
# 🖱️ Chrome Tab Switcher & Activity Simulator

This Python script simulates user activity by:
- Switching between Chrome tabs
- Moving the mouse
- Pressing Page Down keys to simulate scrolling

Useful for keeping sessions alive, preventing screen locking, or faking activity.

---

## 🚀 Features

- Switches Chrome tabs every few seconds
- Moves mouse to random screen positions
- Scrolls down and resets to top after a few steps
- Shutdown popup with countdown on Ctrl+Alt
---

## ⚙️ Configuration

Edit these values at the top of the script to adjust behavior:

```python
SWITCH_INTERVAL = 240  # Change this to 30 for tab switching every 30 seconds
ENABLE_MOUSE_MOVEMENT = True
ENABLE_SCROLLING = True
SCROLL_STEPS = 10
STOP_KEY_COMBO = 'ctrl+alt'
COUNTDOWN_TIME = 10
```

---

## ✅ Requirements

- Python 3.13.3 or newer installed
- Required libraries:
  ```bash
  pip install pyautogui keyboard
  ```
- For GUI popup: `tkinter` (comes pre-installed with most Python distributions)

---

## 📦 How to Use

1. Open Chrome with multiple tabs.
2. Run the script:
   ```bash
   python your_script_name.py
   ```
3. Let it simulate tab switching and scrolling.
4. To stop the script:
   - Press `Ctrl+Alt`, or
   - Move your mouse to the top-left corner

---

## 📚 Examples

- Want to switch tabs every **30 seconds** instead of 240?

  Change:
  ```python
  SWITCH_INTERVAL = 30
  ```

- Want to **disable scrolling**?

  Change:
  ```python
  ENABLE_SCROLLING = False
  ```

---

## ❓ FAQ

### Does this work with browsers other than Chrome?
It is optimized for Chrome but may work with other browsers if Ctrl+Tab is the tab switch shortcut.

### Can this run in the background?
It must stay focused on Chrome for the actions to work.

### Why does nothing happen when I run it?
Make sure Chrome is active and in focus when you launch the script.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## ✒️ Author & Credits

Made with ❤️ by **Billy Wellington**

- [LinkedIn](https://www.linkedin.com/in/billywellington/)
- Feel free to fork, contribute, or star ⭐ the repo!

