# Selenium Social Media Automation

Selenium automation Simple Script built to practice login flows, dynamic scrolling, modal handling, and element interaction on instagram.

This script performs automated login, profile navigation, and follower list interaction.

This script login and navigates to a target account, opens its follower list, and follow all user from that list.

---

## Setup

Create a `.env` file with the following variables:

```env
USERNAME_INSTA="your_instagram_username"
PASSWORD_INSTA="your_instagram_password"
ACCOUNT_TO_FOLLOW="target_account"
CURRENT_FOLLOWER_COUNT="target_account_current_follower_count"
```

---

## Run

```bash
python main.py
```

