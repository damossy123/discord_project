# discord_project
# 🚀 Discord Logger & Web Project

פרויקט Full-stack המשלב צד שרת ב-Python עם יכולות תיעוד והתראות בזמן אמת. המערכת מאפשרת למשתמשים לשלוח הודעות דרך ממשק רשת, שומרת את ההיסטוריה במסד נתונים מקומי, ומפיצה עדכונים אוטומטיים לערוץ Discord נבחר.

## ✨ תכונות עיקריות (Features)
* **Web Interface:** ממשק משתמש נקי להזנת נתונים.
* **Database Integration:** שמירה וניהול של היסטוריית שיחות בטבלת SQLite.
* **Discord Automation:** שליחה אוטומטית של הודעות ל-Discord באמצעות Webhooks.
* **Smart Retrieval:** פונקציות לשליפת נתונים מבוססת זמן (למשל: "הודעות מהחצי שעה האחרונה").

## 🛠️ טכנולוגיות (Tech Stack)
* **Backend:** Python 3.x, Flask
* **Database:** SQLite3
* **Integrations:** Discord Webhook API
* **IDE:** PyCharm

## 📋 דרישות מוקדמות (Prerequisites)
לפני הרצת הפרויקט, יש לוודא שמותקנות הספריות הבאות:
```bash
pip install Flask discord-webhook
