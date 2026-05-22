# How to Update Your Hugging Face Space

Quick guide to update your Hugging Face Space with the new multi-country comparison feature.

---

## 🚀 Method 1: Web Interface (Easiest)

### **Step 1: Go to Your Space**
1. Open: https://huggingface.co/spaces/YOUR-USERNAME/country-mapping-app
2. Click the **"Files"** tab

### **Step 2: Update app.py**
1. Click on **"app.py"**
2. Click the **pencil icon** (Edit) in the top-right
3. **Select all** (Ctrl+A) and **delete**
4. **Copy the entire content** from your local `app.py` file
5. **Paste** into the editor
6. Scroll down and click **"Commit changes to main"**
7. Add commit message: "Add multi-country comparison feature"
8. Click **"Commit"**

### **Step 3: Wait for Rebuild**
1. Click the **"App"** tab
2. You'll see **"Building..."** status
3. Wait **2-3 minutes** for rebuild
4. Status will change to **"Running"**
5. **Done!** Your app is updated

---

## 🔄 Method 2: Upload File (Alternative)

### **Step 1: Go to Files Tab**
1. Open your Space
2. Click **"Files"** tab

### **Step 2: Upload Updated File**
1. Click **"Add file"** → **"Upload files"**
2. **Drag and drop** your updated `app.py`
3. Or click **"Choose files"** and select `app.py`
4. Add commit message: "Update app.py with comparison feature"
5. Click **"Commit changes to main"**

### **Step 3: Wait for Rebuild**
- Same as Method 1, Step 3

---

## 💻 Method 3: Git Push (Advanced)

If you set up Git access:

### **Step 1: Navigate to Your Project**
```powershell
cd C:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app
```

### **Step 2: Add Hugging Face Remote (First Time Only)**
```powershell
git remote add hf https://huggingface.co/spaces/YOUR-USERNAME/country-mapping-app
```

### **Step 3: Commit Your Changes**
```powershell
git add app.py
git commit -m "Add multi-country comparison feature"
```

### **Step 4: Push to Hugging Face**
```powershell
git push hf main
```

### **Step 5: Enter Credentials**
- **Username:** Your Hugging Face username
- **Password:** Your Hugging Face access token
  - Get token at: https://huggingface.co/settings/tokens

---

## ✅ Verify the Update

### **After Rebuild Completes:**

1. **Open your Space URL**
2. **Test single country selection:**
   - Select 1 country
   - Verify detailed view works

3. **Test multi-country comparison:**
   - Select 2+ countries
   - Check tables have **light backgrounds**
   - Check text is **dark and readable**
   - Verify **no scrolling** inside tables
   - Confirm **"Yes"/"No"** values display

4. **Check metric labels:**
   - Verify "systems enabled" text is readable
   - Should be dark text, not green-on-green

---

## 🐛 Troubleshooting

### **Problem: Build Fails**
**Solution:**
1. Click **"Logs"** tab to see error
2. Check if app.py was uploaded correctly
3. Verify no syntax errors
4. Try restarting: Settings → Restart Space

### **Problem: Tables Still Dark**
**Solution:**
1. **Hard refresh** your browser: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. **Clear browser cache**
3. Try in **incognito/private window**
4. CSS changes may take a moment to apply

### **Problem: Old Version Still Showing**
**Solution:**
1. Check **"Files"** tab - verify app.py was updated
2. Look at file timestamp
3. Check **"Logs"** tab for build completion
4. Hard refresh browser

---

## 📝 What's New in This Update

### **Features Added:**
- ✅ Multi-country selection (multiselect dropdown)
- ✅ Systems comparison table
- ✅ Additional information comparison table
- ✅ Light backgrounds with dark text
- ✅ No scrolling inside tables
- ✅ Readable metric labels

### **Files Changed:**
- ✅ `app.py` - Enhanced with comparison feature

### **Files Unchanged:**
- ✅ `data_processor.py` - No changes needed
- ✅ `requirements.txt` - No new dependencies
- ✅ Excel file - No changes needed

---

## 🎯 Quick Update Checklist

- [ ] Go to Hugging Face Space
- [ ] Click "Files" tab
- [ ] Edit or upload app.py
- [ ] Commit changes
- [ ] Wait for rebuild (2-3 minutes)
- [ ] Test the app
- [ ] Verify multi-country comparison works
- [ ] Check tables have light backgrounds
- [ ] Confirm no scrolling needed

---

## 💡 Tips

### **Best Practice:**
- Update during **low-usage times**
- Test locally first: `streamlit run app.py`
- Keep a backup of working version
- Use descriptive commit messages

### **Commit Message Examples:**
- "Add multi-country comparison feature"
- "Fix table styling - light backgrounds"
- "Update app.py - improve readability"

---

## 📞 Need Help?

### **If Update Fails:**
1. Check Hugging Face status: https://status.huggingface.co/
2. Review build logs in "Logs" tab
3. Verify file uploaded correctly
4. Try Method 1 (web interface) if Git fails

### **If App Doesn't Work:**
1. Check browser console for errors (F12)
2. Review Space logs
3. Test with single country first
4. Clear browser cache

---

## 🎉 Success!

Once updated, your Hugging Face Space will have:
- ✅ Multi-country comparison
- ✅ Beautiful light-themed tables
- ✅ Easy-to-read text
- ✅ No scrolling issues
- ✅ Professional appearance

**Your IBM colleagues will love the new comparison feature!** 🌍