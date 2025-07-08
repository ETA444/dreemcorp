# DREEMCORP Social Media Archive

## Folder Structure
This repository serves as an organized archive for social media content and related analytics `Python scripts`, `.csv files` and `graphs`.

It is primarily used to track posts, scripts, and assets across various platforms for easy backup, reference, and analysis.

---

## Folder Structure Overview
The general folder structure is as follows:

```
.
├── .git/
├── .gitignore
├── .obsidian/
├── LICENSE
├── README.md
├── <Account_Name>/
│   └── {series-name}_{title}_{date}/ 
│     ├── articles/
│     │   ├── {series-name}_{title}_{date}_full.md
│     │   ├── {series-name}_{title}_{date}_substack.md
│     │   └── {series-name}_{title}_{date}_medium.md
│     ├── posts/
│     │   ├── x-posts/
│     │   │   ├── {title}_tweet_1.md
│     │   │   ├── {title}_tweet_2.md
│     │   │   └── ...
│     │   │
│     │   └── linkedin-posts/
│     │       ├── {title}_linkedin_post.md
│     │       └── ...
│     │
│     ├── code/
│     │   ├── analysis-scripts/
│     │   │   └── ...
│     │   └── visualization-scripts/
│     │       └── ...
│     │
│     └── visuals/
│         ├── charts/
│         │   └── ...
│         └── ...
│             └── ...
│
└── <YT_Account_Name>/ (for YouTube accounts)
        └── community-posts/
            └── <Community_Post_ID>/
                └── (Content files: .txt, .png, etc.)
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
