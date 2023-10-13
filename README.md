# Python-Celery
Celery 練習

# 步驟

## 設定任務

```Python
# src/tasks.py
# 設定任務 範例
@celery.task
def print_time():
    msg = f'現在時間: {datetime.now()}'
    logger.info(msg)
    res = {'data': msg}
    return res # 回傳結果會顯示在flower網站


@celery.task
def add_num(x, y):
    ans = x + y
    logger.info(ans)
    res = {'data': ans}
    return res
```

## 設定排程

```Python
# src/schedule.py
# 設定排程
task_name = 'add_num-1' # 設定任務名稱
if task_name in TASKS.keys():
    if TASKS[task_name]['execute']:
        CELERYBEAT_SCHEDULE[task_name] = {
            'task': 'src.tasks.add_num',
            'schedule': crontab(hour=12, minute=0),  # 每天中午 12:00 執行
            'args': tuple(TASKS[task_name]['args'])  # 帶入參數 將串列轉成元組
        }

        if TASKS[task_name]['queue']:
            # 將任務發送到 queue
            CELERYBEAT_SCHEDULE[task_name]['options'] = {'queue': TASKS[task_name]['queue']}
```

## 設定開關

```json
// conf/tasks.json
// 設定開關
{
  "print_time-1": { // 任務名稱
    "execute": true, // 是否執行
    "queue": null, // 指定使用哪個worker
	"send_messag": false // 是否開啟發送結果到 tg (須設置 TELEGRAM_API_KEY TELEGRAM_CHAT_ID)
  },
  "add_num-1": {
    "execute": false,
    "args": [1, 2], // 帶入函式參數
    "queue": "queue2",
	"send_messag": false
  }
}
```

# config.ini 說明

```ini
[BASIC]
; celery溝通 預設  redis://redis:6379/0
; Celery 代理（消息中間件）的 URL。
; 這告訴 Celery 在哪裡查找和儲存任務。
CELERY_BROKER=

; 結果存入位置 預設 mongodb://mongo:27017/celery.result
CELERY_BACKEND=

; 時區設置 預設 Asia/Taipei
; https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
CELERY_TIMEZONE=

; 輸出log等級 預設為 WARNING
LOG_LEVEL=

; 關閉log功能 輸入選項 (true, True, 1) 預設 不關閉
LOG_DISABLE=

; logs路徑 預設 logs
LOG_PATH=

; 關閉紀錄log檔案 輸入選項 (true, True, 1)  預設 關閉
LOG_FILE_DISABLE=

; (用於開關任務)tasks json設定檔位置 預設為 conf/tasks.json
TASKS_JSON_PATH=

[TELEGRAM]
; Telegram Bot 的 API 金鑰
TELEGRAM_API_KEY=

; Telegram 使用者的 Chat ID
TELEGRAM_CHAT_ID=
```