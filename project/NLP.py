import praw
import csv
import time
from tqdm import tqdm

# 初始化 Reddit API
reddit = praw.Reddit(
    client_id='ZSSUtry-qVqVCVd8oUrRHg',
    client_secret='3j_ZTDHr5mjE5FFBaTTmMFWlNO70zQ',  # 👈 換成你的 secret
    user_agent='my_app by /u/Alarming_Fan_4866'
)

# 搜尋關鍵字
keywords = ['POPMART', 'Disney', 'Pokemon']
output_file = 'reddit_comments.csv'

# 建立並寫入表頭一次
with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['keyword', 'post_title', 'post_url', 'comment'])
    writer.writeheader()

# 開始寫入資料（追加模式）
with open(output_file, mode='a', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['keyword', 'post_title', 'post_url', 'comment'])

    for keyword in keywords:
        print(f"\n🔍 正在搜尋關鍵字: {keyword}")
        submissions = reddit.subreddit('all').search(keyword, sort='top', limit=100)

        for submission in tqdm(submissions, desc=f"處理 {keyword}", unit="post"):
            try:
                submission.comments.replace_more(limit=0)
                comments = submission.comments[:5]

                for comment in comments:
                    writer.writerow({
                        'keyword': keyword,
                        'post_title': submission.title,
                        'post_url': f'https://reddit.com{submission.permalink}',
                        'comment': comment.body.replace('\n', ' ').strip()
                    })

                time.sleep(1)

            except Exception as e:
                print(f"⚠️ 錯誤跳過：{e}")
                continue

print(f"\n✅ 抓取完成，資料即時寫入 CSV：{output_file}")