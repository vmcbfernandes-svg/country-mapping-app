# Streamlit Cloud Private Deployment - Step by Step

Complete guide to deploy your Country Mapping App to Streamlit Cloud as a **PRIVATE** app for IBM internal use only.

---

## 📋 PART 1: Prerequisites (5 minutes)

### STEP 1: Create GitHub Account (if you don't have one)

1. **Go to:** https://github.com/signup
2. **Enter your email** (use your IBM email: vitor.fernandes@bg.ibm.com)
3. **Create password**
4. **Choose username**
5. **Verify email**
6. **Complete setup**

### STEP 2: Install Git (if not installed)

1. **Download Git for Windows:**
   - Go to: https://git-scm.com/download/win
   - Download "64-bit Git for Windows Setup"
   - Run the installer
   - Click "Next" through all options (defaults are fine)
   - Click "Install"

2. **Verify installation:**
   - Open PowerShell
   - Type: `git --version`
   - You should see: `git version 2.x.x`

3. **Configure Git:**
   ```powershell
   git config --global user.name "Your Name"
   git config --global user.email "vitor.fernandes@bg.ibm.com"
   ```

---

## 📋 PART 2: Prepare Your Code (5 minutes)

### STEP 3: Create .gitignore File

1. **In PowerShell, navigate to your project:**
   ```powershell
   cd C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app
   ```

2. **Create .gitignore file:**
   ```powershell
   notepad .gitignore
   ```

3. **Paste this content:**
   ```
   __pycache__/
   *.py[cod]
   *$py.class
   .vscode/
   .idea/
   *.swp
   .DS_Store
   Thumbs.db
   .streamlit/secrets.toml
   ```

4. **Save and close** (File → Save, then close Notepad)

### STEP 4: Verify All Required Files

Run this command to see your files:
```powershell
dir
```

**You should have:**
- ✅ app.py
- ✅ data_processor.py
- ✅ requirements.txt
- ✅ Country Mapping File 28April2026 vs1.xlsx
- ✅ .gitignore (just created)

---

## 📋 PART 3: Push Code to GitHub (10 minutes)

### STEP 5: Create GitHub Repository

1. **Go to:** https://github.com/new

2. **Fill in the form:**
   - **Repository name:** `country-mapping-app`
   - **Description:** "IBM Country Mapping Application - Internal Use Only"
   - **Visibility:** Select **"Private"** ⚠️ IMPORTANT!
   - **DO NOT** check "Add a README file"
   - **DO NOT** add .gitignore (we already have one)
   - **DO NOT** choose a license

3. **Click "Create repository"**

4. **Keep this page open** - you'll need the commands shown

### STEP 6: Push Your Code to GitHub

1. **In PowerShell (in your project directory):**

   ```powershell
   # Initialize Git repository
   git init
   ```

2. **Add all files:**
   ```powershell
   git add .
   ```

3. **Commit files:**
   ```powershell
   git commit -m "Initial commit - Country Mapping App"
   ```

4. **Rename branch to main:**
   ```powershell
   git branch -M main
   ```

5. **Add remote repository:**
   ```powershell
   git remote add origin https://github.com/YOUR-USERNAME/country-mapping-app.git
   ```
   
   ⚠️ **Replace `YOUR-USERNAME`** with your actual GitHub username!

6. **Push to GitHub:**
   ```powershell
   git push -u origin main
   ```

7. **Enter credentials when prompted:**
   - **Username:** Your GitHub username
   - **Password:** Use a **Personal Access Token** (not your password)
   
   **To create a token:**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Give it a name: "Streamlit Deploy"
   - Check "repo" scope
   - Click "Generate token"
   - **Copy the token** (you won't see it again!)
   - Paste it as the password

8. **Verify upload:**
   - Go to: https://github.com/YOUR-USERNAME/country-mapping-app
   - You should see all your files
   - Verify it says **"Private"** next to the repo name

---

## 📋 PART 4: Deploy to Streamlit Cloud (5 minutes)

### STEP 7: Sign Up for Streamlit Cloud

1. **Go to:** https://share.streamlit.io/signup

2. **Click "Continue with GitHub"**

3. **Authorize Streamlit Cloud:**
   - Click "Authorize streamlit"
   - Enter your GitHub password if prompted

4. **You'll be redirected to Streamlit Cloud dashboard**

### STEP 8: Deploy Your App

1. **Click "New app"** (big button in the center or top-right)

2. **Fill in the deployment form:**

   - **Repository:** Select `YOUR-USERNAME/country-mapping-app`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL (optional):** Leave default or customize
     - Example: `country-mapping-app` → `country-mapping-app.streamlit.app`

3. **Click "Deploy!"**

4. **Wait for deployment** (2-3 minutes)
   - You'll see build logs
   - Status will change from "Building" → "Running"

5. **Your app is now live!**
   - You'll get a URL like: `https://country-mapping-app.streamlit.app`

---

## 📋 PART 5: Make App Private (CRITICAL!)

### STEP 9: Set App to Private

1. **In Streamlit Cloud, click on your app**

2. **Click the "⚙️ Settings" button** (top-right)

3. **Go to "Sharing" tab**

4. **Under "App visibility":**
   - Select **"Private"**
   - This ensures only invited users can access

5. **Click "Save"**

### STEP 10: Invite IBM Colleagues

1. **Still in Settings → Sharing tab**

2. **Under "Viewers":**
   - Click "Add viewer"
   - Enter IBM colleague's email
   - They'll receive an invitation
   - They must sign in with GitHub to access

3. **Repeat for each colleague**

---

## 📋 PART 6: Test Your App

### STEP 11: Access Your Private App

1. **Click on your app URL** (or go to the URL from Step 8)

2. **You should see your Country Mapping App**

3. **Test functionality:**
   - ✅ Select Geo dropdown
   - ✅ Select Market dropdown
   - ✅ Select Country dropdown
   - ✅ Verify data displays correctly
   - ✅ Check systems/offerings show up

4. **Share URL with invited colleagues**
   - They'll need to sign in with GitHub
   - Then they can access the app

---

## 🔄 PART 7: Update Your App (Future Changes)

### When You Make Changes to Your Code:

1. **Save your changes in VS Code**

2. **In PowerShell:**
   ```powershell
   cd C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app
   
   # Add changes
   git add .
   
   # Commit changes
   git commit -m "Description of changes"
   
   # Push to GitHub
   git push
   ```

3. **Streamlit Cloud auto-deploys:**
   - Changes appear in 1-2 minutes
   - No need to manually redeploy
   - Just refresh your browser

---

## 📊 Monitoring & Management

### View App Logs:

1. **In Streamlit Cloud dashboard**
2. **Click on your app**
3. **Click "Manage app" (bottom-right)**
4. **View logs, metrics, and status**

### Restart App:

1. **Manage app → "Reboot app"**
2. **Useful if app is stuck or not responding**

### Delete App:

1. **Manage app → "Delete app"**
2. **Confirm deletion**
3. **App and URL will be removed**

---

## 🔒 Security Best Practices

### ✅ DO:
- Keep GitHub repo **Private**
- Set Streamlit app to **Private**
- Only invite trusted IBM colleagues
- Use strong GitHub password
- Enable 2FA on GitHub account

### ❌ DON'T:
- Make repo public
- Share app URL publicly
- Commit sensitive credentials
- Use weak passwords

---

## 💰 Cost & Limits

### Streamlit Cloud Free Tier:

- ✅ **1 private app** (FREE)
- ✅ **Unlimited public apps** (FREE)
- ✅ **1 GB RAM** per app
- ✅ **1 CPU core** per app
- ✅ **Auto-sleep** after inactivity (wakes on access)

**Your app is well within these limits!**

---

## 🛑 Troubleshooting

### Problem: "Repository not found"
**Solution:** 
- Verify repo is on GitHub
- Check repo name spelling
- Ensure Streamlit has access to private repos

### Problem: "Module not found"
**Solution:**
- Check `requirements.txt` has all dependencies
- Verify file is in root directory
- Push updated requirements.txt to GitHub

### Problem: "File not found: Country Mapping File..."
**Solution:**
- Verify Excel file is in GitHub repo
- Check file name matches exactly (including spaces)
- Ensure file wasn't in .gitignore

### Problem: "App won't start"
**Solution:**
- Check logs in Streamlit Cloud
- Verify app.py has no syntax errors
- Test locally first: `streamlit run app.py`

### Problem: "Can't access private app"
**Solution:**
- Ensure user is invited in Settings → Sharing
- User must sign in with GitHub
- Check app visibility is set to "Private"

---

## 📞 Support

- **Streamlit Docs:** https://docs.streamlit.io/streamlit-community-cloud
- **Streamlit Forum:** https://discuss.streamlit.io/
- **GitHub Help:** https://docs.github.com/

---

## ✅ Quick Reference Commands

### Git Commands:
```powershell
# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your message"

# Push to GitHub
git push

# Pull latest changes
git pull
```

### Local Testing:
```powershell
# Run app locally
streamlit run app.py

# Stop app
Ctrl+C
```

---

## 🎉 Summary

**You now have:**
- ✅ Private GitHub repository
- ✅ Private Streamlit Cloud app
- ✅ Free hosting for IBM internal use
- ✅ Auto-deployment from GitHub
- ✅ Access control for IBM colleagues
- ✅ Professional URL for sharing

**Total time: ~25 minutes**

**Your app is live and secure for IBM internal use!**