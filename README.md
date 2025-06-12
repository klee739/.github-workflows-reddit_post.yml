name: Reddit Auto Poster

on:
  schedule:
    - cron: '0 14 * * *'   # 10 AM ET
    - cron: '0 18 * * *'   # 2 PM ET
    - cron: '0 22 * * *'   # 6 PM ET
  workflow_dispatch:       # Also allows manual trigger

jobs:
  post:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install praw

      - name: Run Reddit post script
        env:
          REDDIT_CLIENT_ID: ${{ secrets.REDDIT_CLIENT_ID }}
          REDDIT_CLIENT_SECRET: ${{ secrets.REDDIT_CLIENT_SECRET }}
          REDDIT_USERNAME: ${{ secrets.REDDIT_USERNAME }}
          REDDIT_PASSWORD: ${{ secrets.REDDIT_PASSWORD }}
        run: python reddit_post.py
