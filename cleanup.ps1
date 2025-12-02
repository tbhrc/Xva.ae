$files = Get-ChildItem -Path "c:\Users\TalentBridgeDubai\Talent Bridge HR Consultancy\Talent Bridge Dubai - TBHRC - IT Dept\Web Dev\Xva.ae\iaiv3" -Filter *.html
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # ROI Calculator
    $content = [Regex]::Replace($content, '(<a href="roi-calculator.html"[^>]*>ROI Calculator</a>)(\s*\1)+', '$1')
    
    # Team
    $content = [Regex]::Replace($content, '(<a href="team.html"[^>]*>Team</a>)(\s*\1)+', '$1')
    
    # Arabic Button
    $content = [Regex]::Replace($content, '(<button[^>]*title="Coming Soon">عربي</button>)(\s*\1)+', '$1')
    
    Set-Content $file.FullName $content -Encoding UTF8
}
