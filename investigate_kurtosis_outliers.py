# Investigate the features where SYNTHETIC has surprisingly high kurtosis
# (ellipsis_count and first_person_count are the standouts)

for feat in ['ellipsis_count', 'first_person_count', 'word_count', 'type_token_ratio']:
    top5 = synthetic_df.nlargest(5, feat)[['output', feat]]
    print(f"\n=== Top 5 synthetic outliers for {feat} ===")
    for idx, row in top5.iterrows():
        preview = row['output'][:100].replace('\n', ' ')
        print(f"  {feat}={row[feat]}  |  {preview}...")
