# Git deployment script for flip the bottle project

Write-Host "Initializing git repository and deploying to main branch..." -ForegroundColor Green

# Initialize git repository if not exists
if (-not (Test-Path ".git")) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
    Write-Host "Git repository initialized." -ForegroundColor Green
}

# Add all files
Write-Host "Adding files to git..." -ForegroundColor Yellow
git add .

# Commit with descriptive message
Write-Host "Committing changes..." -ForegroundColor Yellow
git commit -m "feat: Optimize homepage for SEO and user experience

- Optimize keyword density: 'flip the bottle' (4.2%) and 'flip the bottle game' (1.4%)
- Reduce content length from 1500+ to ~700 words for better readability
- Streamline content structure with 3 core tips instead of 8 detailed ones
- Add Microsoft Clarity user behavior tracking (ID: su27md6ann)
- Improve meta descriptions and social media tags for better SEO
- Maintain responsive design and game functionality
- Ready for Vercel deployment"

# Set main branch
Write-Host "Setting up main branch..." -ForegroundColor Yellow
git branch -M main

Write-Host ""
Write-Host "✅ Git commit completed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps for Vercel deployment:" -ForegroundColor Cyan
Write-Host "1. Add your Vercel remote: git remote add origin [your-vercel-git-url]" -ForegroundColor White
Write-Host "2. Push to main: git push -u origin main" -ForegroundColor White
Write-Host "3. Vercel will automatically deploy your changes" -ForegroundColor White
Write-Host ""
Write-Host "Current commit includes:" -ForegroundColor Cyan
Write-Host "- SEO-optimized homepage with proper keyword density" -ForegroundColor White
Write-Host "- Microsoft Clarity tracking integration" -ForegroundColor White
Write-Host "- Streamlined content structure" -ForegroundColor White
Write-Host "- Enhanced user experience" -ForegroundColor White
Write-Host ""
