@echo off
echo Initializing git repository and deploying to main branch...

REM Initialize git repository if not exists
if not exist .git (
    echo Initializing git repository...
    git init
    echo Git repository initialized.
)

REM Add all files
echo Adding files to git...
git add .

REM Commit with descriptive message
echo Committing changes...
git commit -m "feat: Optimize homepage for SEO and user experience

- Optimize keyword density: 'flip the bottle' (4.2%) and 'flip the bottle game' (1.4%)
- Reduce content length from 1500+ to ~700 words for better readability
- Streamline content structure with 3 core tips instead of 8 detailed ones
- Add Microsoft Clarity user behavior tracking (ID: su27md6ann)
- Improve meta descriptions and social media tags for better SEO
- Maintain responsive design and game functionality
- Ready for Vercel deployment"

REM Set main branch
echo Setting up main branch...
git branch -M main

echo.
echo ✅ Git commit completed successfully!
echo.
echo Next steps for Vercel deployment:
echo 1. Add your Vercel remote: git remote add origin [your-vercel-git-url]
echo 2. Push to main: git push -u origin main
echo 3. Vercel will automatically deploy your changes
echo.
echo Current commit includes:
echo - SEO-optimized homepage with proper keyword density
echo - Microsoft Clarity tracking integration
echo - Streamlined content structure
echo - Enhanced user experience
echo.
pause
