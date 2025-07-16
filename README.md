# DREEMCORP Social Media Archive

## Folder Structure

This repository serves as an archive for various forms of content created for DREEMCORP-managed social accounts. Here you will find `Python scripts`, `.csv files` and `graphs` from analytics accounts such as **@cryptopandemic** and **@datasafari**.

The repository is primarily used to track posts, scripts, and assets across various platforms for easy backup, reference, and analysis.

**COPYRIGHT NOTICE:** The repository includes copyrighted branding elements that are to be used only with the express permission of DREEMCORP.

---

## Folder Structure Overview

The general folder structure is as follows:

```text
.
├── .git/
├── .gitignore
├── .obsidian/
├── LICENSE
├── README.md
├── <Account_Name>/
│       ├── content/
│       │   └── {series-name}_{title}_{date}/ 
│       │      ├── articles/
│       │      │   ├── {series-name}_{title}_{date}_full.md
│       │      │   ├── {series-name}_{title}_{date}_substack.md
│       │      │   └── {series-name}_{title}_{date}_medium.md
│       │      ├── posts/
│       │      │   ├── x-posts/
│       │      │   │   ├── {title}_tweet_1.md
│       │      │   │   ├── {title}_tweet_2.md
│       │      │   │   └── ...
│       │      │   │
│       │      │   └── linkedin-posts/
│       │      │       ├── {title}_linkedin_post.md
│       │      │       └── ...
│       │      │
│       │      ├── code/
│       │      │   ├── analysis-scripts/
│       │      │   │   └── ...
│       │      │   └── visualization-scripts/
│       │      │       └── ...
│       │      │
│       │      └── visuals/
│       │          ├── charts/
│       │          │   └── ...
│       │          └── ...
│       │              └── ...
│       │       
│       └── branding/
│           │── cover/
│           │    └── ...
│           │── logo/
│           │    └── ...
│           │── pfps/
│           │    └── ...
│           └── .../
│            └── ...
│
└── <YT_Account_Name>/ (for YouTube accounts)
        │── community-posts/
        │    └── <Community_Post_ID>/
        │        └── (Content files: .txt, .png, etc.)
        │
        └── branding/
             │── cover/
             │    └── ...
             │── logo/
             │    └── ...
             │── pfps/
             │    └── ...
             └── watermark/
                 └── ...
```

---

## License

This project is licensed under the MIT License, excluding copyrighted branding content and any graphic assets. See [LICENSE](LICENSE) for details.
