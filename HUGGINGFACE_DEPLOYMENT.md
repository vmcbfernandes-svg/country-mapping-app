# Hugging Face Spaces Deployment - Step by Step

Complete guide to deploy your Country Mapping App to Hugging Face Spaces as a **PRIVATE** app for IBM internal use only.

**Why Hugging Face?** Unlimited private apps for FREE! 🎉

---

## 📋 PART 1: Create Hugging Face Account (3 minutes)

### STEP 1: Sign Up for Hugging Face

1. **Go to:** https://huggingface.co/join

2. **Fill in the form:**
   - **Email:** Use your IBM email (vitor.fernandes@bg.ibm.com)
   - **Username:** Choose a username (e.g., vitor-fernandes-ibm)
   - **Password:** Create a strong password
   - **Full name:** Your name

3. **Click "Sign Up"**

4. **Verify your email:**
   - Check your IBM email inbox
   - Click the verification link
   - You'll be redirected to Hugging Face

5. **Complete profile (optional):**
   - Add profile picture
   - Add bio
   - Or skip for now

---

## 📋 PART 2: Create Your Space (5 minutes)

### STEP 2: Create a New Space

1. **Go to:** https://huggingface.co/new-space

   Or click your profile picture → "New Space"

2. **Fill in the Space creation form:**

   **Owner:** Your username (auto-selected)
   
   **Space name:** `country-mapping-app`
   
   **License:** Select "Apache 2.0" (or any open license)
   
   **Select the SDK:** Click **"Streamlit"** ⚠️ IMPORTANT!
   
   **Space hardware:** Select **"CPU basic - Free"**
   
   **Space visibility:** Select **"Private"** 🔒 CRITICAL!
   
   **Space secrets:** Leave empty for now

3. **Click "Create Space"**

4. **Wait 10-20 seconds** - Your space is being created

---

## 📋 PART 3: Upload Your Files (10 minutes)

### STEP 3: Prepare Files for Upload

You need to upload these files:
- ✅ app.py
- ✅ data_processor.py
- ✅ requirements.txt
- ✅ Country Mapping File 28April2026 vs1.xlsx

### STEP 4: Upload Files via Web Interface

**Method 1: Drag and Drop (Easiest)**

1. **In your Space page, click "Files" tab**

2. **Click "Add file" → "Upload files"**

3. **Drag and drop all 4 files:**
   - app.py
   - data_processor.py
   - requirements.txt
   - Country Mapping File 28April2026 vs1.xlsx

4. **Or click "Choose files" and select them**

5. **Add commit message:** "Initial upload - Country Mapping App"

6. **Click "Commit changes to main"**

7. **Wait for upload** (30-60 seconds)

**Method 2: Upload One by One**

If drag-and-drop doesn't work:

1. **Click "Add file" → "Create a new file"**

2. **For app.py:**
   - Name: `app.py`
   - Copy-paste content from your local app.py
   - Click "Commit new file to main"

3. **Repeat for data_processor.py**

4. **Repeat for requirements.txt**

5. **For Excel file:**
   - Click "Add file" → "Upload files"
   - Select the Excel file
   - Click "Commit changes to main"

---

## 📋 PART 4: Configure Your Space (2 minutes)

### STEP 5: Verify Files Are Uploaded

1. **Click "Files" tab**

2. **You should see:**
   ```
   📄 app.py
   📄 data_processor.py
   📄 requirements.txt
   📄 Country Mapping File 28April2026 vs1.xlsx
   📄 README.md (auto-created by Hugging Face)
   ```

3. **If any file is missing, upload it now**

### STEP 6: Wait for Build

1. **Click "App" tab** (next to Files)

2. **You'll see "Building..." status**

3. **Wait 2-3 minutes** for the build to complete

4. **Status will change to "Running"**

5. **Your app will appear in the iframe!**

---

## 📋 PART 5: Test Your App (3 minutes)

### STEP 7: Test Functionality

1. **In the "App" tab, you should see your Country Mapping App**

2. **Test all features:**
   - ✅ Select Geo dropdown
   - ✅ Select Sub-Region dropdown
   - ✅ Select Market dropdown
   - ✅ Select Country dropdown
   - ✅ Verify country details display
   - ✅ Check systems/offerings show correctly

3. **If something doesn't work:**
   - Click "Logs" tab to see errors
   - Check if all files uploaded correctly
   - Verify requirements.txt has all dependencies

---

## 📋 PART 6: Share with IBM Colleagues (5 minutes)

### STEP 8: Invite Team Members

1. **Click "Settings" tab** (in your Space)

2. **Scroll to "Collaborators" section**

3. **Click "Add collaborator"**

4. **Enter IBM colleague's Hugging Face username or email**

5. **Select role:**
   - **"Read"** - Can only view the app
   - **"Write"** - Can view and edit
   - Choose **"Read"** for most colleagues

6. **Click "Add"**

7. **Repeat for each colleague**

### STEP 9: Share the URL

1. **Your Space URL is:**
   ```
   https://huggingface.co/spaces/YOUR-USERNAME/country-mapping-app
   ```

2. **Share this URL with invited colleagues**

3. **They must:**
   - Have a Hugging Face account
   - Be logged in
   - Be added as collaborators

4. **They'll see the app immediately after logging in**

---

## 📋 PART 7: Alternative - Git Method (Advanced)

### STEP 10: Clone and Push via Git (Optional)

If you prefer using Git (like GitHub):

1. **Install Git LFS (Large File Storage):**
   ```powershell
   git lfs install
   ```

2. **Clone your Space:**
   ```powershell
   git clone https://huggingface.co/spaces/YOUR-USERNAME/country-mapping-app
   cd country-mapping-app
   ```

3. **Copy your files:**
   ```powershell
   copy C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app\*.py .
   copy C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app\*.txt .
   copy "C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app\Country Mapping File 28April2026 vs1.xlsx" .
   ```

4. **Commit and push:**
   ```powershell
   git add .
   git commit -m "Add Country Mapping App"
   git push
   ```

5. **Enter credentials:**
   - Username: Your Hugging Face username
   - Password: Your Hugging Face password or token

---

## 🔄 PART 8: Update Your App (Future Changes)

### When You Make Changes:

**Method 1: Web Interface (Easiest)**

1. **Go to your Space**
2. **Click "Files" tab**
3. **Click on the file you want to edit** (e.g., app.py)
4. **Click the pencil icon (Edit)**
5. **Make your changes**
6. **Click "Commit changes to main"**
7. **App auto-rebuilds in 1-2 minutes**

**Method 2: Re-upload File**

1. **Click "Files" tab**
2. **Click "Add file" → "Upload files"**
3. **Upload the updated file** (it will overwrite)
4. **Commit changes**

**Method 3: Git Push (if using Git)**

1. **Make changes locally**
2. **Commit and push:**
   ```powershell
   git add .
   git commit -m "Update description"
   git push
   ```

---

## 📊 PART 9: Monitor Your Space

### View Logs:

1. **Click "Logs" tab**
2. **See real-time application logs**
3. **Useful for debugging errors**

### View Settings:

1. **Click "Settings" tab**
2. **Manage:**
   - Visibility (Private/Public)
   - Collaborators
   - Hardware (upgrade if needed)
   - Delete Space

### Check Status:

1. **App tab shows current status:**
   - 🟢 Running
   - 🟡 Building
   - 🔴 Error
   - 😴 Sleeping (wakes on access)

---

## 🔒 Security & Privacy

### Your Space is Private:

- ✅ Only you and invited collaborators can access
- ✅ Not listed in public Spaces
- ✅ Not indexed by search engines
- ✅ Requires login to view

### Best Practices:

1. **Keep Space visibility "Private"**
2. **Only invite trusted IBM colleagues**
3. **Don't commit sensitive credentials**
4. **Use strong password for Hugging Face account**
5. **Enable 2FA (Two-Factor Authentication):**
   - Go to: https://huggingface.co/settings/account
   - Enable 2FA for extra security

---

## 💰 Cost & Limits

### Hugging Face Spaces Free Tier:

- ✅ **Unlimited private Spaces** (not just 1!)
- ✅ **50GB storage** per Space
- ✅ **2 vCPU** (CPU basic)
- ✅ **16GB RAM** (CPU basic)
- ✅ **Auto-sleep** after 48 hours inactivity
- ✅ **Instant wake** on access

**Your app is well within these limits!**

### Upgrade Options (if needed):

- **CPU upgrade** - $0.03/hour (~$22/month)
- **GPU** - For ML models (not needed for your app)
- **Persistent storage** - Keep app always running

**For your use case, FREE tier is perfect!**

---

## 🛑 Troubleshooting

### Problem: "Space is building forever"

**Solution:**
- Check "Logs" tab for errors
- Verify requirements.txt is correct
- Ensure all files uploaded
- Try restarting: Settings → Restart Space

### Problem: "Module not found"

**Solution:**
- Check requirements.txt has all dependencies:
  ```
  streamlit==1.32.0
  pandas==2.2.1
  openpyxl==3.1.2
  ```
- Re-upload requirements.txt
- Restart Space

### Problem: "File not found: Country Mapping File..."

**Solution:**
- Verify Excel file uploaded correctly
- Check file name matches exactly (including spaces)
- Re-upload the Excel file

### Problem: "App shows error"

**Solution:**
- Click "Logs" tab to see detailed error
- Test app locally first: `streamlit run app.py`
- Check if data_processor.py uploaded correctly

### Problem: "Colleague can't access"

**Solution:**
- Verify they're added as collaborators
- Ensure they're logged into Hugging Face
- Check Space visibility is "Private"
- Share correct URL

### Problem: "App is sleeping"

**Solution:**
- This is normal after 48 hours inactivity
- App wakes automatically when accessed
- Takes 10-20 seconds to wake
- Or upgrade to persistent storage

---

## 🆚 Comparison with Other Platforms

| Feature | Hugging Face | Streamlit Cloud | IBM Code Engine |
|---------|--------------|-----------------|-----------------|
| **Private Apps** | ✅ Unlimited | ❌ Only 1 | ✅ Unlimited |
| **Cost** | ✅ FREE | ✅ FREE | ❌ Paid |
| **Storage** | ✅ 50GB | ⚠️ 1GB | ✅ Flexible |
| **Setup Time** | ⭐⭐⭐⭐ 15 min | ⭐⭐⭐⭐⭐ 10 min | ⭐⭐ 30 min |
| **Best For** | **Multiple private apps** | Single demo | Enterprise |

---

## 📞 Support & Resources

- **Hugging Face Docs:** https://huggingface.co/docs/hub/spaces
- **Streamlit on Spaces:** https://huggingface.co/docs/hub/spaces-sdks-streamlit
- **Community Forum:** https://discuss.huggingface.co/
- **Discord:** https://discord.gg/hugging-face

---

## ✅ Quick Reference

### Your Space URL:
```
https://huggingface.co/spaces/YOUR-USERNAME/country-mapping-app
```

### Update via Web:
1. Files tab → Click file → Edit → Commit

### Update via Git:
```powershell
git add .
git commit -m "Update"
git push
```

### Restart Space:
Settings → Restart Space

### Add Collaborator:
Settings → Collaborators → Add

### View Logs:
Logs tab

---

## 🎉 Summary

**You now have:**
- ✅ **FREE** Hugging Face Space
- ✅ **PRIVATE** access (only invited users)
- ✅ **Unlimited** private Spaces (not just 1!)
- ✅ **50GB** storage
- ✅ **Professional** URL
- ✅ **Easy updates** via web or Git
- ✅ **Perfect for IBM internal use**

**Total setup time: ~20 minutes**

**Your app is live, private, and ready for IBM internal use!**

---

## 🚀 Next Steps

1. **Create Hugging Face account** (if you haven't)
2. **Create new Space** (select Streamlit, Private)
3. **Upload your 4 files**
4. **Wait for build** (2-3 minutes)
5. **Test your app**
6. **Invite IBM colleagues**
7. **Share the URL**

**Start with Part 1, Step 1 above!**