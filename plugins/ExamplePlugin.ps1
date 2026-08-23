Write-IOTLog `
    -Module "Example Plugin" `
    -Level "INFO" `
    -Message "Plugin inicializado."

$Global:IOTEC.ExamplePlugin = @{
    Status = "ONLINE"
    Started = Get-Date
}
