# Render Environment Variables Setup

## Quick Copy-Paste Values

Add these variables in Render Dashboard → Web Service → Environment:

### 1. FLASK_ENV
```
FLASK_ENV=production
```

### 2. AI_PROVIDER
```
AI_PROVIDER=gemini
```

### 3. SECRET_KEY (Click "Generate" button OR use):
```
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 4. JWT_SECRET_KEY (Click "Generate" button OR use):
```
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 5. GEMINI_API_KEY
Get from: https://aistudio.google.com/app/apikey
Paste the key value

### 6. DATABASE_URL (MOST IMPORTANT)
1. Go to PostgreSQL service (retrievai-db)
2. Click "Connections" tab
3. Copy "Internal Database URL"
4. Paste here

## Steps to Add:

1. In Render: Web Service → Environment
2. For each variable:
   - Enter NAME
   - Enter VALUE
   - Click "Add Environment Variable"
3. When done: Click "Save"
4. Then: "Manual Deploy" → "Latest"
5. Wait for build to finish
