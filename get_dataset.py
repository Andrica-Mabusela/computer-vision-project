import pandas as pd
import subprocess
import os

# Load annotations CSV (download just this file first - it's tiny)
df = pd.read_csv('./kinetics400/train.csv')  
# Columns: label, youtube_id, time_start, time_end, split, is_cc

# Define household chore classes
chore_classes = [
    'washing dishes', 'doing laundry', 'vacuuming floor',
    'mopping floor', 'ironing clothes', 'folding clothes',
    'cooking chicken', 'baking cookies', 'making bed',
    'cleaning toilet', 'sweeping floor', 'washing hands'
]

# Filter to only chore-related videos
chores_df = df[df['label'].isin(chore_classes)]
print(f"Found {len(chores_df)} chore clips across {chores_df['label'].nunique()} classes")

chores_df.to_csv('kinetics_chores_annotations.csv', index=False)



def download_clip(row, output_dir='chores_videos'):
    os.makedirs(output_dir, exist_ok=True)
    url = f"https://www.youtube.com/watch?v={row['youtube_id']}"
    output_path = f"{output_dir}/{row['youtube_id']}_{row['time_start']}.mp4"
    
    cmd = [
        'yt-dlp',
        '--download-sections', f"*{row['time_start']}-{row['time_end']}",
        '-o', output_path,
        url
    ]
    subprocess.run(cmd, capture_output=True)

# Download only chore clips
for _, row in chores_df.iterrows():
    download_clip(row)