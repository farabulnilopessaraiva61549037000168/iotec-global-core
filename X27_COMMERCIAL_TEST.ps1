$mods = @(
"CRM_ENGINE.py",
"COMMERCIAL_FUNNEL_ENGINE.py",
"COMMERCIAL_OPPORTUNITY_ENGINE.py",
"CLIENT_ONBOARDING_ENGINE.py",
"IOTEC_CONTRACT_ENGINE.py",
"IOTEC_FIRST_REVENUE_ENGINE.py",
"SALES_AUTOPILOT_ENGINE.py",
"PROSPECTION_COMMAND_CENTER.py",
"REVENUE_COMMAND_CENTER.py",
"UNIFY_COMMERCIAL_CORE.py"
)

foreach ($m in $mods)
{
    Write-Host ""
    Write-Host "================================="
    Write-Host $m
    Write-Host "================================="

    $f = Get-ChildItem C:\IOTEC -Recurse -Filter $m -ErrorAction SilentlyContinue | Select-Object -First 1

    if ($f)
    {
        python $f.FullName
    }
}