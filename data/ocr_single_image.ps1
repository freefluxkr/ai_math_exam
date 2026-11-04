# PowerShell OCR script to recognize text from an image
param (
    [string]$ImagePath
)

Add-Type -AssemblyName System.Drawing
[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null

$lang = New-Object Windows.Globalization.Language("ko")
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)

$file = [Windows.Storage.StorageFile]::GetFileFromPathAsync($ImagePath).GetAwaiter().GetResult()
$stream = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read).GetAwaiter().GetResult()
$decoder = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream).GetAwaiter().GetResult()
$bitmap = $decoder.GetSoftwareBitmapAsync().GetAwaiter().GetResult()

$result = $engine.RecognizeAsync($bitmap).GetAwaiter().GetResult()

$lines = @()
foreach ($line in $result.Lines) {
    $words = @()
    foreach ($word in $line.Words) {
        $words += @{
            text = $word.Text
            x = $word.BoundingRect.X
            y = $word.BoundingRect.Y
            w = $word.BoundingRect.Width
            h = $word.BoundingRect.Height
        }
    }
    $lines += @{
        text = $line.Text
        words = $words
    }
}

$output = @{
    text = $result.Text
    lines = $lines
}

$output | ConvertTo-Json -Depth 5

