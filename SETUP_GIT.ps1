# GO2ABROAD SOP — init & prepare push
$ErrorActionPreference = "Stop"
Write-Host ">>> git init" -ForegroundColor Cyan
if (-not (Test-Path .git)) { git init }
git branch -M main
Write-Host ">>> staging release files" -ForegroundColor Cyan
git add README*.md CITATION.cff LICENSE client/ catalog/ sop_catalog_open.json featured_multilingual.json SETUP_GIT.ps1
Write-Host ">>> commit" -ForegroundColor Cyan
git commit -m "feat(catalog): release per-SOP intros and 11-language detail URLs with Zenodo DOI"
Write-Host ""
Write-Host "Next:" -ForegroundColor Green
Write-Host "  git remote add origin https://github.com/<org>/sop-catalog.git"
Write-Host "  git push -u origin main"
