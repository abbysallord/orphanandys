# Orphan and Y's Restaurant Website

A full-stack restaurant website with FastAPI backend and React frontend.

## Deployment

### Vercel (Recommended)

1. Push the code to GitHub.
2. Connect the repo to Vercel.
3. Set environment variables in Vercel dashboard:
   - `MONGO_URL`: Your MongoDB connection string
   - `DB_NAME`: Your database name
   - `CORS_ORIGINS`: Your frontend domain (e.g., `https://your-app.vercel.app`)
   - `REACT_APP_BACKEND_URL`: Leave empty (for same-origin API calls)
4. Deploy.

### Netlify

For Netlify, deploy the frontend only and host the backend separately (e.g., on Vercel).

1. Push to GitHub.
2. Connect to Netlify.
3. In `netlify.toml`, update the backend URL in the redirects to your backend's URL.
4. Set `REACT_APP_BACKEND_URL` to your backend's URL.
5. Deploy.

## Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
# Set environment variables
python server.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```
