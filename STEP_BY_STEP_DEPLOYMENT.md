# Step-by-Step IBM Cloud Code Engine Deployment

Follow these exact steps to deploy your Country Mapping App to IBM Cloud Code Engine.

---

## 📋 STEP 1: Install IBM Cloud CLI

### Windows (Your System):

1. **Download the installer:**
   - Go to: https://github.com/IBM-Cloud/ibm-cloud-cli-release/releases/
   - Download: `IBM_Cloud_CLI_2.x.x_windows_amd64.exe` (latest version)

2. **Run the installer:**
   - Double-click the downloaded `.exe` file
   - Follow the installation wizard
   - Click "Next" → "Next" → "Install" → "Finish"

3. **Verify installation:**
   - Open **PowerShell** (or Command Prompt)
   - Type: `ibmcloud --version`
   - You should see version information

**Expected output:**
```
ibmcloud version 2.x.x
```

---

## 📋 STEP 2: Login to IBM Cloud

1. **Open PowerShell** in your project directory:
   - Right-click on your `country-mapping-app` folder
   - Select "Open in Terminal" or "Open PowerShell window here"

2. **Login with SSO (Single Sign-On):**
   ```powershell
   ibmcloud login --sso
   ```

3. **Follow the prompts:**
   - You'll see: "Get a one-time code from https://identity-x.x.x.x to proceed"
   - Press **Enter**
   - A browser window will open
   - Login with your **IBM w3id credentials**
   - Copy the **one-time passcode** shown
   - Paste it back in PowerShell and press **Enter**

4. **Select your account:**
   - If you have multiple accounts, select your IBM account
   - Type the number and press **Enter**

**Expected output:**
```
Targeted account Your IBM Account (xxxxx)
API endpoint:      https://cloud.ibm.com
Region:            us-south
User:              your.email@ibm.com
Account:           Your IBM Account (xxxxx)
```

---

## 📋 STEP 3: Install Code Engine Plugin

1. **In the same PowerShell window, run:**
   ```powershell
   ibmcloud plugin install code-engine
   ```

2. **Confirm installation:**
   - Type `y` when asked "Do you want to install the plugin?"
   - Wait for installation to complete (30-60 seconds)

3. **Verify installation:**
   ```powershell
   ibmcloud plugin list
   ```

**Expected output:**
```
Plugin Name          Version
code-engine          1.x.x
```

---

## 📋 STEP 4: Target Your Resource Group

1. **List available resource groups:**
   ```powershell
   ibmcloud resource groups
   ```

2. **Target the Default resource group:**
   ```powershell
   ibmcloud target -g Default
   ```

**Expected output:**
```
Targeted resource group Default
```

---

## 📋 STEP 5: Create Code Engine Project

1. **Create a new project:**
   ```powershell
   ibmcloud ce project create --name country-mapping-app
   ```

2. **Wait for creation** (30-60 seconds)

**Expected output:**
```
Creating project 'country-mapping-app'...
OK
```

3. **Select the project:**
   ```powershell
   ibmcloud ce project select --name country-mapping-app
   ```

**Expected output:**
```
Selecting project 'country-mapping-app'...
OK
```

---

## 📋 STEP 6: Deploy Your Application

1. **Make sure you're in your project directory:**
   ```powershell
   cd c:\Users\VitorManuelBarbosaFe\Desktop\country-mapping-app
   ```

2. **Verify files are present:**
   ```powershell
   dir
   ```
   
   You should see:
   - ✅ app.py
   - ✅ data_processor.py
   - ✅ Dockerfile
   - ✅ requirements.txt
   - ✅ Country Mapping File 28April2026 vs1.xlsx

3. **Deploy the application:**
   ```powershell
   ibmcloud ce application create --name country-mapping-app --build-source . --strategy dockerfile --port 8501 --min-scale 0 --max-scale 1 --cpu 0.25 --memory 0.5G
   ```

4. **Wait for deployment** (3-5 minutes)
   - You'll see: "Creating application..."
   - Then: "Building from source..."
   - Finally: "OK"

**Expected output:**
```
Creating application 'country-mapping-app'...
Packaging files to upload from source path '.'...
Submitting build run 'country-mapping-app-run-xxxxx'...
Creating image 'private.us.icr.io/ce--xxxxx/app-country-mapping-app:xxxxx'...
Waiting for build run to complete...
Build run status: 'Running'
Build run completed successfully.
Run 'ibmcloud ce buildrun get -n country-mapping-app-run-xxxxx' to check the build run status.
Configuration 'country-mapping-app' is waiting for a Revision to become ready.
Ingress has been successfully assigned.
Run 'ibmcloud ce application get -n country-mapping-app' to check the application status.
OK
https://country-mapping-app.xxxxx.us-south.codeengine.appdomain.cloud
```

---

## 📋 STEP 7: Get Your Application URL

1. **Get application details:**
   ```powershell
   ibmcloud ce application get --name country-mapping-app
   ```

2. **Look for the URL in the output:**
   ```
   URL: https://country-mapping-app.xxxxx.us-south.codeengine.appdomain.cloud
   ```

3. **Copy the URL and open it in your browser**

---

## 📋 STEP 8: Test Your Application

1. **Open the URL in your browser**
2. **You should see your Country Mapping App**
3. **Test the dropdowns:**
   - Select a Geo
   - Select a Market
   - Select a Country
   - Verify data displays correctly

---

## 🎉 SUCCESS! Your App is Live!

Your application is now hosted on IBM Cloud Code Engine and accessible via the URL.

---

## 📊 Monitor Your Application

### View Application Status:
```powershell
ibmcloud ce application get --name country-mapping-app
```

### View Logs:
```powershell
ibmcloud ce application logs --name country-mapping-app
```

### View Real-time Logs:
```powershell
ibmcloud ce application logs --name country-mapping-app --follow
```

---

## 🔄 Update Your Application

When you make changes to your code:

1. **Save your changes**
2. **Run the update command:**
   ```powershell
   ibmcloud ce application update --name country-mapping-app --build-source .
   ```
3. **Wait for rebuild** (2-3 minutes)
4. **Refresh your browser**

---

## 🛑 Troubleshooting

### Problem: "ibmcloud: command not found"
**Solution:** Restart PowerShell after installing IBM Cloud CLI

### Problem: "Login failed"
**Solution:** 
- Make sure you're using `--sso` flag
- Use your IBM w3id credentials
- Check your internet connection

### Problem: "Project already exists"
**Solution:** 
- Select existing project: `ibmcloud ce project select --name country-mapping-app`
- Or use a different name

### Problem: "Build failed"
**Solution:**
- Check logs: `ibmcloud ce buildrun logs --name country-mapping-app-run-xxxxx`
- Verify all files are present in directory
- Check Dockerfile syntax

### Problem: "Application not responding"
**Solution:**
- Check logs: `ibmcloud ce application logs --name country-mapping-app`
- Verify port 8501 is correct
- Check if Excel file is included

### Problem: "Out of memory"
**Solution:**
- Increase memory: `ibmcloud ce application update --name country-mapping-app --memory 1G`

---

## 💰 Cost Tracking

### Check Your Usage:
1. Go to: https://cloud.ibm.com/billing/usage
2. Look for "Code Engine" in the services list
3. Monitor your free tier usage

### Free Tier Limits:
- ✅ 100,000 vCPU-seconds/month
- ✅ 200,000 GB-seconds/month
- ✅ ~222 hours of runtime/month

**Your app configuration:**
- 0.25 vCPU × 0.5GB = 0.125 vCPU-GB
- 1 hour = 450 vCPU-seconds
- Well within free tier for internal use

---

## 🗑️ Delete Application (if needed)

### Delete the application:
```powershell
ibmcloud ce application delete --name country-mapping-app
```

### Delete the project:
```powershell
ibmcloud ce project delete --name country-mapping-app
```

---

## 📞 Need Help?

- **IBM Cloud Docs:** https://cloud.ibm.com/docs/codeengine
- **IBM Cloud Support:** Open ticket via IBM Cloud console
- **Internal IBM Slack:** #ibm-cloud-code-engine

---

## ✅ Quick Reference Commands

```powershell
# Login
ibmcloud login --sso

# Select project
ibmcloud ce project select --name country-mapping-app

# Deploy/Update
ibmcloud ce application update --name country-mapping-app --build-source .

# Get URL
ibmcloud ce application get --name country-mapping-app

# View logs
ibmcloud ce application logs --name country-mapping-app --follow

# Delete
ibmcloud ce application delete --name country-mapping-app
```

---

**You're all set! Follow these steps and your app will be live in ~10 minutes.**