# 📦 Step-by-Step Guide: Push Your App to GitHub

Complete guide to push your country-mapping-app to GitHub (with screenshots descriptions).

---

## 🎯 **Overview**

You'll learn to:
1. ✅ Create a GitHub account (if needed)
2. ✅ Create a private repository
3. ✅ Push your code from your computer
4. ✅ Verify everything is uploaded

**Time needed: 10-15 minutes**

---

## 📋 **Prerequisites**

### **Check if Git is installed:**

Open PowerShell and run:
```powershell
git --version
```

**If you see a version number** (e.g., `git version 2.40.0`):
- ✅ Git is installed, skip to Step 1

**If you see an error**:
- ❌ Git not installed, follow installation steps below

### **Install Git (if needed):**

1. **Download Git:**
   - Go to: https://git-scm.com/download/win
   - Click "64-bit Git for Windows Setup"
   - Download will start automatically

2. **Install Git:**
   - Run the downloaded `.exe` file
   - Click "Next" through all options (defaults are fine)
   - Click "Install"
   - Click "Finish"

3. **Verify installation:**
   - Open **new** PowerShell window
   - Run: `git --version`
   - Should show version number ✅

---

## 🚀 **STEP 1: Create GitHub Account (If You Don't Have One)**

### **1.1 Sign Up:**
1. Go to: https://github.com
2. Click **"Sign up"** (top right)
3. Enter your email address
4. Click **"Continue"**
5. Create a password
6. Choose a username (e.g., `vitor-ibm`)
7. Complete verification puzzle
8. Click **"Create account"**

### **1.2 Verify Email:**
1. Check your email inbox
2. Find email from GitHub
3. Click verification link
4. ✅ Account created!

---

## 📁 **STEP 2: Create a Private Repository on GitHub**

### **2.1 Create New Repository:**
1. **Log in to GitHub**: https://github.com
2. Click **"+"** icon (top right corner)
3. Select **"New repository"**

### **2.2 Configure Repository:**

Fill in the form:

**Repository name:**
```
country-mapping-app
```

**Description (optional):**
```
IBM Country Mapping Application - Streamlit Dashboard
```

**Visibility:**
- ⚫ Select **"Private"** (Important for IBM internal use)

**Initialize repository:**
- ❌ **DO NOT** check "Add a README file"
- ❌ **DO NOT** add .gitignore
- ❌ **DO NOT** choose a license

**Why?** Your local folder already has these files.

### **2.3 Create Repository:**
1. Click **"Create repository"** (green button at bottom)
2. ✅ Repository created!
3. **Keep this page open** - you'll need the URL

### **2.4 Find the "Push Existing Repository" Section:**

After creating the repository, GitHub shows you a page with setup instructions.

**Look for this section (scroll down if needed):**
```
…or push an existing repository from the command line
```

**You'll see 3 commands like this:**
```bash
git remote add origin https://github.ibm.com/Vitor-Fernandes/country-mapping-app.git
git branch -M main
git push -u origin main
```

**IMPORTANT:**
- ✅ Keep this page open in your browser
- ✅ You'll copy these exact commands in Step 3
- ✅ The URL will be specific to YOUR repository

**Your URL will look like:**
- IBM GitHub: `https://github.ibm.com/YOUR-USERNAME/country-mapping-app.git`
- Public GitHub: `https://github.com/YOUR-USERNAME/country-mapping-app.git`

---

## 💻 **STEP 3: Push Your Code from Your Computer**

### **3.1 Open PowerShell in Your Project Folder:**

**Method 1 - From File Explorer:**
1. Open File Explorer
2. Navigate to: `C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app`
3. Click in the address bar (top)
4. Type: `powershell`
5. Press **Enter**
6. PowerShell opens in your project folder ✅

**Method 2 - From PowerShell:**
1. Open PowerShell
2. Run:
   ```powershell
   cd C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app
   ```

### **3.2 Verify You're in the Right Folder:**

Run:
```powershell
ls
```

You should see your files:
- ✅ `app.py`
- ✅ `data_processor.py`
- ✅ `requirements.txt`
- ✅ `Dockerfile`
- ✅ `Country Mapping File 28April2026 vs1.xlsx`
- ✅ Other `.md` files

If you see these files, you're in the right place! ✅

### **3.3 Configure Git (First Time Only):**

**⚠️ IMPORTANT: Enter these commands ONE LINE AT A TIME**

**First command - Set your name:**
```powershell
git config --global user.name "Your Name"
```
Press **Enter** and wait for it to complete (no output is normal).

**Second command - Set your email:**
```powershell
git config --global user.email "your.email@ibm.com"
```
Press **Enter** and wait for it to complete (no output is normal).

**Example (replace with YOUR actual name and email):**

**Command 1:**
```powershell
git config --global user.name "Vitor Barbosa"
```
Press **Enter** ✅

**Command 2:**
```powershell
git config --global user.email "vitor.barbosa@ibm.com"
```
Press **Enter** ✅

---

**Verify configuration (also one line at a time):**

**Check name:**
```powershell
git config --global user.name
```
Should display: `Vitor Barbosa` (or your name)

**Check email:**
```powershell
git config --global user.email
```
Should display: `vitor.barbosa@ibm.com` (or your email)

✅ Git configured successfully!

### **3.4 Initialize Git Repository:**

Run:
```powershell
git init
```

**Expected output:**
```
Initialized empty Git repository in C:/Users/VitorManuelBarbosaFe/Desktop/country-mapping-app/.git/
```

✅ Git repository initialized!

### **3.5 Add All Files to Git:**

Run:
```powershell
git add .
```

**What this does:**
- Stages all files for commit
- The `.` means "all files in current directory"

**No output is normal** - it means success! ✅

### **3.6 Verify Files Are Staged:**

Run:
```powershell
git status
```

**Expected output:**
```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .dockerignore
        new file:   .gitignore
        new file:   app.py
        new file:   data_processor.py
        new file:   requirements.txt
        ... (more files)
```

✅ All files are staged!

### **3.7 Create First Commit:**

Run:
```powershell
git commit -m "Initial commit - Country Mapping App"
```

**Expected output:**
```
[master (root-commit) abc1234] Initial commit - Country Mapping App
 15 files changed, 1234 insertions(+)
 create mode 100644 app.py
 create mode 100644 data_processor.py
 ... (more files)
```

✅ First commit created!

### **3.8 Use the Commands from GitHub Page:**

**🔴 IMPORTANT: Go back to your GitHub repository page in your browser.**

After creating the repository, scroll down to find this section:

```
…or push an existing repository from the command line
```

**You'll see 3 commands that look like this:**

```bash
git remote add origin https://github.ibm.com/Vitor-Fernandes/country-mapping-app.git
git branch -M main
git push -u origin main
```

**📋 These are YOUR specific commands with YOUR repository URL.**

---

### **3.9 Run Command 1: Connect to GitHub**

**Copy the FIRST command from the GitHub page and run it in PowerShell:**

```powershell
git remote add origin https://github.ibm.com/YOUR-USERNAME/country-mapping-app.git
```

**Example (use YOUR actual URL from GitHub):**
```powershell
git remote add origin https://github.ibm.com/Vitor-Fernandes/country-mapping-app.git
```

**Verify connection:**
```powershell
git remote -v
```

**Expected output:**
```
origin  https://github.ibm.com/YOUR-USERNAME/country-mapping-app.git (fetch)
origin  https://github.ibm.com/YOUR-USERNAME/country-mapping-app.git (push)
```

✅ Connected to GitHub!

---

### **3.10 Run Command 2: Rename Branch**

**Copy the SECOND command from the GitHub page and run it:**

```powershell
git branch -M main
```

**What this does:**
- Renames default branch from `master` to `main`
- GitHub uses `main` as default

**No output is normal** - it means success! ✅

---

### **3.11 Run Command 3: Push to GitHub**

**Copy the THIRD command from the GitHub page and run it:**

```powershell
git push -u origin main
```

**What happens:**
1. Git will ask for GitHub credentials
2. **Username**: Enter your IBM GitHub username
3. **Password**: **DO NOT use your GitHub password!**

**IMPORTANT: Use Personal Access Token (PAT) - See Step 4 below**

---

## 🔑 **STEP 4: Create GitHub Personal Access Token (PAT)**

### **Why?**
GitHub no longer accepts passwords for command-line operations. You need a PAT.

### **4.1 Create PAT:**

1. **Go to GitHub Settings:**
   - Click your profile picture (top right)
   - Click **"Settings"**

2. **Navigate to Developer Settings:**
   - Scroll down to bottom of left sidebar
   - Click **"Developer settings"**

3. **Create Personal Access Token:**
   - Click **"Personal access tokens"**
   - Click **"Tokens (classic)"**
   - Click **"Generate new token"**
   - Click **"Generate new token (classic)"**

4. **Configure Token:**
   - **Note**: `Country Mapping App - Deployment`
   - **Expiration**: `90 days` (or your preference)
   - **Select scopes**: Check **"repo"** (this checks all sub-items)
   - Scroll down
   - Click **"Generate token"** (green button)

5. **Copy Token:**
   - ⚠️ **IMPORTANT**: Copy the token NOW
   - It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - You won't see it again!
   - Save it in a secure location (password manager)

### **4.2 Use PAT to Push:**

Go back to PowerShell and run:
```powershell
git push -u origin main
```

**When prompted:**
- **Username**: Your GitHub username
- **Password**: **Paste your PAT** (not your GitHub password!)

**Expected output:**
```
Enumerating objects: 20, done.
Counting objects: 100% (20/20), done.
Delta compression using up to 8 threads
Compressing objects: 100% (18/18), done.
Writing objects: 100% (20/20), 15.23 KiB | 1.52 MiB/s, done.
Total 20 (delta 2), reused 0 (delta 0), pack-reused 0
To https://github.com/YOUR-USERNAME/country-mapping-app.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

✅ **Code pushed to GitHub successfully!**

---

## ✅ **STEP 5: Verify Upload on GitHub**

### **5.1 Check GitHub Repository:**

1. Go to: `https://github.com/YOUR-USERNAME/country-mapping-app`
2. You should see all your files:
   - ✅ `app.py`
   - ✅ `data_processor.py`
   - ✅ `requirements.txt`
   - ✅ `Dockerfile`
   - ✅ `.gitignore`
   - ✅ All `.md` files
   - ✅ Excel file

### **5.2 Verify Privacy:**

Look for **"Private"** badge next to repository name:
- ✅ Should say **"Private"** (not "Public")

### **5.3 Check File Contents:**

1. Click on `app.py`
2. Verify code is correct
3. Click "Back" button
4. Check other files

✅ **Everything uploaded successfully!**

---

## 🔄 **Future Updates: How to Push Changes**

After making changes to your code:

### **Quick Update Commands:**

```powershell
# 1. Navigate to project folder
cd C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app

# 2. Check what changed
git status

# 3. Add all changes
git add .

# 4. Commit with message
git commit -m "Description of changes"

# 5. Push to GitHub
git push
```

**Example workflow:**
```powershell
# After editing app.py
git add .
git commit -m "Updated color scheme for better visibility"
git push
```

✅ Changes pushed to GitHub!

---

## 🆘 **Troubleshooting**

### **Problem: "git: command not found"**
**Solution:**
- Git not installed
- Follow installation steps in Prerequisites section
- Restart PowerShell after installation

### **Problem: "Permission denied (publickey)"**
**Solution:**
- Use HTTPS URL (not SSH)
- URL should start with `https://` not `git@`
- Use Personal Access Token (PAT) as password

### **Problem: "Authentication failed"**
**Solution:**
- Don't use GitHub password
- Use Personal Access Token (PAT)
- Create new PAT if lost (Step 4)

### **Problem: "Repository not found"**
**Solution:**
- Check repository URL is correct
- Verify repository exists on GitHub
- Check you're logged in to correct GitHub account

### **Problem: Excel file not uploading**
**Solution:**
- File might be too large
- Check `.gitignore` doesn't exclude `.xlsx` files
- Run: `git add "Country Mapping File 28April2026 vs1.xlsx" -f`

### **Problem: "fatal: not a git repository"**
**Solution:**
- You're not in the project folder
- Run: `cd C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app`
- Then run `git init`

---

## 📝 **Complete Command Reference**

### **First Time Setup:**
```powershell
# Navigate to project
cd C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app

# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@ibm.com"

# Initialize repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit - Country Mapping App"

# Rename branch to main
git branch -M main

# Connect to GitHub (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/country-mapping-app.git

# Push to GitHub
git push -u origin main
```

### **Future Updates:**
```powershell
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push
```

---

## ✅ **Success Checklist**

- [ ] Git installed and working
- [ ] GitHub account created
- [ ] Private repository created on GitHub
- [ ] Git configured with name and email
- [ ] Repository initialized locally
- [ ] All files added and committed
- [ ] Connected to GitHub remote
- [ ] Personal Access Token (PAT) created
- [ ] Code pushed to GitHub successfully
- [ ] Verified files on GitHub website
- [ ] Repository is private

---

## 🎉 **Next Steps**

Now that your code is on GitHub:

1. **Deploy to Streamlit Cloud:**
   - See **DEPLOYMENT_ALTERNATIVES.md**
   - Go to: https://share.streamlit.io
   - Connect GitHub and deploy

2. **Or Deploy to Render:**
   - See **DEPLOYMENT_ALTERNATIVES.md**
   - Go to: https://render.com
   - Connect GitHub and deploy

3. **Or Deploy to Railway:**
   - See **DEPLOYMENT_ALTERNATIVES.md**
   - Go to: https://railway.app
   - Connect GitHub and deploy

**Your app will be live in 2-3 minutes!** 🚀

---

## 💡 **Pro Tips**

### **Commit Messages:**
Write clear commit messages:
- ✅ Good: `"Fixed color scheme for better visibility"`
- ✅ Good: `"Added multi-country comparison feature"`
- ❌ Bad: `"Update"`
- ❌ Bad: `"Changes"`

### **Commit Frequency:**
- Commit after each logical change
- Don't wait until end of day
- Small, frequent commits are better

### **Check Before Pushing:**
```powershell
# Always check what you're pushing
git status
git diff
```

### **Save Your PAT:**
- Store in password manager
- Don't share with anyone
- Create new one if lost

---

**You're now ready to push to GitHub and deploy!** 🎉

**Made with Bob** 💻