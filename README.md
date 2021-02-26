# Carbon-API
---

[![Telegram](https://img.shields.io/badge/Telegram-Channel-pink)](https://t.me/phaticusthiccy)


> Carbon, girdiğiniz metni kod fotoğrafına dönüştürür.

#### Kullanımı

| Parametre              | Varsayılan                 | Tür     | Açıklama                                                     |
| ---------------------- | -------------------------- | ------- | ------------------------------------------------------------ |
| `code` (Gerekli)       | `hernangi bir metin`       | string  | Fotoğrafın içindeki yazıyı belirler.                         |
| `backgroundColor`      | `"rgba(171, 184, 195, 1)"` | string  | Arkaplan RGB rengi.                                          |
| `dropShadow`           | `true`                     | boolean | Gölge Detayı.                                                |
| `dropShadowBlurRadius` | `"68px"`                   | string  | Gölge Alanı.                                                 |
| `dropShadowOffsetY`    | `"20px"`                   | string  | Gölgenin Y (Yukarı Aşağı) Konumu.                            |
| `exportSize`           | `"2x"`                     | string  | Fotoğrafın Kalitesini Ayarlar. `"1x"` | `"2x"` | `"3x"`      |
| `fontSize`             | `"14px"`                   | string  | Yazı Boyutu                                                  |
| `fontFamily`           | `"Hack"`                   | string  | Yazı Ailesi                                                  |
| `firstLineNumber`      | `1`                        | number  | İlk Kodun Sayısı (Ayarlamak için Kod Sıra Göstergesini aç)   |
| `language`             | `"auto"`                   | string  | Programlama Dili                                             |
| `lineNumbers`          | `false`                    | boolean | Kod Sıra Göstergesi                                          |
| `paddingHorizontal`    | `"56px"`                   | string  | Dikey Genişlik                                               |
| `paddingVertical`      | `"56px"`                   | string  | Yatay Genişlik                                               |
| `theme`                | `"seti"`                   | string  | Kod Teması                                                   |
| `watermark`            | `false`                    | boolean | Filigran Aç/Kapa                                             | 
| `widthAdjustment`      | `true`                     | boolean | Otomatik Çözünürlüğü Aç/Kapa                                 |
| `windowControls`       | `true`                     | boolean | Çerçeve Görüntüsünü Aç/Kapa                                  |
| `windowTheme`          | `"none"`                   | string  | Çerçeve Teması                                               |

##

## Parametre Değerleri 

| Parametre              | Değerler                       |
| ---------------------- | -------------------------------|
| `backgroundColor`      | `"rgba(0, 0, 0, 1)"` ile `"rgba(255, 255, 255, 1)"` arasında olabilir. |
| `dropShadow`           | `true` veya `false` olabilir.                                 |
| `dropShadowBlurRadius` | `"10px"` ile `"400px"` arasında olabilir.                     |
| `dropShadowOffsetY`    | `"1px"` ile `"100px"` arasında olabilir.                      |
| `exportSize`           | `"1x"` ile `"3x"` arasında olabilir.                          |
| `fontSize`             | `"Hack"`, `"JetBrains Mono"`, `"Fira Code"`, `"Inconsolata"` vs. |
| `firstLineNumber`      | Sınırı yoktur.                                                |
| `language`             | `JavaScript`, `Python`, `C`, `Go`, `Bash`, `Swift` vs.        |
| `lineNumbers`          | `true` veya `false` olabilir.                                 |
| `paddingHorizontal`    | `"10px"` ile `"3000px"` arasında olabilir.                    |
| `paddingVertical`      | `"10px"` ile `"3000px"` arasında olabilir.                    |
| `theme`                | `seti`, `blackboard`, `panda`, `twilight`, `verminal` vs.     |
| `watermark`            | `true` veya `false` olabilir.                                 |
| `widthAdjustment`      | `true` veya `false` olabilir.                                 |
| `windowControls`       | `true` veya `false` olabilir.                                 |
| `windowTheme`          | `none`, `sharp` ve `bw` olabilir.                             |

### GET `/`

Değerler Encoded Şeklinde olmalıdır. Mümkünüse HTML Encoder kullanın.

```bash
https://carbonnowsh.herokuapp.com/?code=Phaticusthiccy&theme=darcula&backgroundColor=rgba(144, 19, 254, 100)
```

### POST `/`

Json

```json
{
    "backgroundColor": "rgba(144, 19, 254, 100)",
    "code": "Phaticusthiccy",
    "theme": "dracula"
}
```

#### Deploy Ayarları

* **[Heroku](https://www.heroku.com/) Method** 
  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/phaticusthiccy/Carbon-API/tree/main)

* **Diğer Method** 

  ```bash
  # Repoyu Klonla
  git clone https://github.com/phaticusthiccy/Carbon-API
  cd Carbon-API

  #  2
  virtualenv -p /usr/bin/python3 venv
  ../venv/bin/activate

  #  3
  pip3 install -r requirements.txt

  # Çalıştır
  python3 app.py
  ```
