# unsw.co — Archived

> ⚠️ This project is archived. The website is no longer actively maintained.

**unsw.co** was a community-driven course review platform for UNSW students, primarily serving Chinese-speaking postgraduate and undergraduate students in the CSE faculty.

## Course Reviews

All course comments have been migrated to GitHub Issues for preservation:

👉 **[Browse all course reviews](https://github.com/daya0576/unsw.co/issues)**

| Label | Description |
|---|---|
| `CSE-Postgrad` | CSE Postgraduate Coursework courses |
| `CSE-Undergraduate-Courses` | CSE Undergraduate courses |
| `UEEC` | University English Entry Course |

- **65 courses** with at least one review
- **129 comments** migrated, preserved with original author, date, and likes

---

## Original Setup (for reference)

### Step 1
Add `keys.py` to the `rango/` directory:
```python
BING_API_KEY = ""
G_EMAIL_KEY = ""
ME_EMAIL_KEY = ""
```

### Step 2
Install dependencies from the root directory:
```bash
pip install -r requirements.txt
```

### Step 3
```bash
cd rango
python manage.py runserver 8001
```

Open [http://127.0.0.1:8001/](http://127.0.0.1:8001/) in your browser.
