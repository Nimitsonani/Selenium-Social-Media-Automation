# Selenium Social Media Automation

This is a Selenium-based automation script built to practice browser automation on Instagram.

The script logs into an account, navigates to a target profile, opens the followers list, and follows users from that list.

The focus of this project was learning how to handle dynamic content and interactive elements in a real web application.

---

## What This Script Does

After launching the browser:

1. Logs into Instagram using provided credentials.
2. Navigates to a specified target account.
3. Opens the followers modal.
4. Scrolls through the dynamically loaded follower list.
5. Clicks the follow button for users in that list.

---

## What It Demonstrates

This script was built to practice:

- Automated login flows
- Handling popups and modals
- Working with dynamically loaded elements
- Scrolling inside scrollable containers
- Clicking elements that load asynchronously
- Basic environment variable handling for credentials

Instagram loads followers dynamically while scrolling, so the script includes logic to repeatedly scroll the modal to load more users before interacting with elements.

---

## Environment Variables

Create a `.env` file in the root directory:

```env
USERNAME_INSTA="your_instagram_username"
PASSWORD_INSTA="your_instagram_password"
ACCOUNT_TO_FOLLOW="target_account"
CURRENT_FOLLOWER_COUNT="target_account_current_follower_count"
```

- `USERNAME_INSTA` → Your Instagram login username  
- `PASSWORD_INSTA` → Your Instagram login password  
- `ACCOUNT_TO_FOLLOW` → Target profile to open  
- `CURRENT_FOLLOWER_COUNT` → Used to control scroll logic  

---

## Run

```
python main.py
```

---

## Notes

- This script is intended for learning purposes.
- Instagram’s UI changes frequently, so selectors may need updates.
- Credentials should never be hardcoded in the script.
