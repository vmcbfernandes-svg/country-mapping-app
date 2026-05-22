# Quick Deploy to IBM Cloud Code Engine

## TL;DR - Deploy in 3 Commands

```bash
# 1. Login to IBM Cloud
ibmcloud login --sso

# 2. Install Code Engine plugin (if not installed)
ibmcloud plugin install code-engine

# 3. Deploy your app
ibmcloud ce project create --name country-mapping-app && \
ibmcloud ce project select --name country-mapping-app && \
ibmcloud ce application create \
  --name country-mapping-app \
  --build-source . \
  --strategy dockerfile \
  --port 8501 \
  --min-scale 0 \
  --max-scale 1 \
  --cpu 0.25 \
  --memory 0.5G
```

## Get Your App URL

```bash
ibmcloud ce application get --name country-mapping-app
```

Look for the URL in the output - it will look like:
`https://country-mapping-app.xxxxxx.us-south.codeengine.appdomain.cloud`

## What You Need

✅ **Dockerfile** - Already created  
✅ **.dockerignore** - Already created  
✅ **IBM Cloud Account** - You have as IBMer  
✅ **IBM Cloud CLI** - Download from https://cloud.ibm.com/docs/cli  

## Cost

**FREE** within these limits:
- 100,000 vCPU-seconds/month
- 200,000 GB-seconds/month
- ~222 hours of runtime per month

## Update Your App

```bash
ibmcloud ce application update --name country-mapping-app --build-source .
```

## View Logs

```bash
ibmcloud ce application logs --name country-mapping-app --follow
```

## Delete App

```bash
ibmcloud ce application delete --name country-mapping-app
```

---

For detailed instructions, see **IBM_CLOUD_DEPLOYMENT.md**