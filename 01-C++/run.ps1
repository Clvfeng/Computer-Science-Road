# 一键编译并运行 C++ 文件
# 用法: .\run.ps1 文件名  (不要带 .cpp，例如 .\run.ps1 hello)
param([Parameter(Mandatory = $true)][string]$Name)

Set-Location -Path $PSScriptRoot

$src = "$Name.cpp"
if (-not (Test-Path $src)) {
    Write-Host "找不到文件: $src" -ForegroundColor Red
    exit 1
}

& "D:\mingw64\bin\g++.exe" -g $src -o "$Name.exe"
if ($LASTEXITCODE -ne 0) {
    Write-Host "编译失败" -ForegroundColor Red
    exit 1
}

Write-Host "===== 运行结果 =====" -ForegroundColor Green
& ".\$Name.exe"