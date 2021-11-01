New-AzResourceGroup -Name $resourceGroupName -Location "UK South"
New-AzResourceGroupDeployment `
    -ResourceGroupName $resourceGroupName `
    -TemplateFile "template.json" `
    -iotHubName "iotHub"