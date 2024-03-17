# Entity Manipulation and Cryptography

## Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Cryptography](#cryptography)
- [Unit Alteration](#unit-alteration)
- [File Format Modification](#file-format-modification)
- [Python Library Requirements](#python-library-requirements)
- [Directions to use](#directions-to-use)
- [Conclusion](#conclusion)
- [License](#license)

## Introduction
The **Entity Manipulation and Cryptography**  project is a versatile and user-friendly tool designed to facilitate the efficient conversion of various entities, including text, units, and file formats. With its intuitive interfaces and comprehensive functionalities, this project aims to streamline the conversion process and enhance user productivity.

## Key Features:

### [Data Encryption and Decryption](text.py):

- Convert text between different formats such as binary, decimal, hexadecimal, Morse code, Braille, and more.
- Perform encryption and decryption using various cryptographic algorithms including Caesar Cipher, Vigenère Cipher, Rail Fence Cipher, and Atbash Cipher.
- Generate QR codes from text inputs for easy sharing and storage, and text to speech.

### [Unit Alter](unit.py):

- Convert units across multiple categories including currency, length, area, volume, weight, temperature, speed, pressure, power, time, and data storage.
- Provides support for both metric and imperial units, ensuring comprehensive coverage for diverse conversion needs.

### [File Formats](file.py):

- Convert between different file formats for images, audio, video, documents, and archives.
- Supported file formats include JPEG, PNG, PDF, MP3, MP4, DOCX, ZIP, and many more.
- Offers seamless conversion capabilities to enhance file compatibility and accessibility.

## [Cryptography](text.py)
The text conversion and cryptography section offer the following functionalities:

### [Text to QR Code](qr.py)
Converts text into a QR code image using [qrcode](https://link-to-qrcode) library.

### [Text to Speech](speech.py)
Converts text into an MP3 file using [pyttsx3](https://link-to-pyttsx3) library.

### [Caesar Cipher](caesar.py)
Performs encryption and decryption using the Caesar Cipher algorithm. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

#### Example:
- Plain Text: "HELLO"
- Key: 3
- Encrypted Text: "KHOOR"

#### Step-by-step:
1. **Mapping the Alphabet:**
   - A -> D, B -> E, C -> F, ..., X -> A, Y -> B, Z -> C
2. **Shifting Process:**
   - H -> K (shifted 3 places forward)
   - E -> H
   - L -> O
   - L -> O
   - O -> R

- Rot13 is a Special case of the Caesar Cipher, which is a substitution cipher where each letter in the plaintext is shifted 13 places.

### [Vigenère Cipher](vigenere.py)
Utilizes the Vigenère Cipher for encryption and decryption. The Vigenère Cipher is a polyalphabetic substitution cipher that uses a keyword to determine the shift value for each letter in the plaintext.

#### Encryption Process:

1.  **Choose text and key word**
    Plaintext: ATTACKATDAWN
    Keyword: LEMON
    Repeat the keyword to match the length of the plaintext: LEMONLEMONLE

2.  **Convert the plaintext and the repeated keyword to numeric values**
    Plaintext: A(0) T(19) T(19) A(0) C(2) K(10) A(0) T(19) D(3) A(0) W(22) N(13)
    Keyword: L(11) E(4) M(12) O(14) N(13) L(11) E(4) M(12) O(14) N(13) L(11) E(4)

3.  Now, encrypt each letter:
    A + L = L, T + E = X, T + M = B, A + O = P, C + N = P, K + L = U, A + E = E, T + M = B, D + O = Q, A + N = O, W + L = I, N + E = R

4.  Encrypted Message: LXBPPUEBQOIR

### [Rail Fence Cipher](rail_fence.py)
Implements the Rail Fence Cipher algorithm for encryption and decryption. The Rail Fence Cipher is a transposition cipher that writes the plaintext across multiple "rails" of an imaginary fence, then reads off the ciphertext diagonally.

#### Encryption Process:
1. Plain text: "HELLOWORLD"
   Key: 3 (number of rows)

2. **Creating the Rail Fence Pattern:**

   | H |   |   |   | O |   |   |   | L |   |
   |---|---|---|---|---|---|---|---|---|---|
   |   | E |   | L |   | W |   | R |   | D |
   |   |   | L |   |   |   | O |   |   |   |

3. **Reading the Pattern Diagonally:**
   - HOLELWRDLO

### [Atbash Cipher](atbash.py)
Applies the Atbash Cipher for encryption and decryption. The Atbash Cipher is a monoalphabetic substitution cipher where each letter in the plaintext is replaced with its reverse in the alphabet.

#### Example:
- Plain Text: "HELLO"
- Encrypted Text: "SVOOL"

#### Encryption Process:
1. **Mapping the alphabet:**
   - A -> Z, B -> Y, C -> X, ..., W -> D, X -> C, Y -> B, Z -> A
2. **Reversing the order**
   - H -> S, E -> V, L -> O, L -> O, O -> L

### [Morse Code](morse.py)
Converts text to Morse code and vice versa. Morse code is a method used in telecommunication to encode text characters as sequences of two different signal durations, called dots and dashes.

#### Example:
- Plain Text: "HELLO"
- Morse Code: ".... . .-.. .-.. ---"

#### Cipher Process:
1. **Mapping Characters to Morse Code:**
   - H -> ...., E -> ., L -> .-.., O -> ---
2. **Converting Plain Text to Morse Code:**
   - H -> ...., E -> ., L -> .-.., L -> .-.., O -> ---

### [Braille](braille.py)
Converts text to Braille and Braille to text. Braille is a tactile writing system used by people who are visually impaired. Each character is represented by a pattern of raised dots arranged in a 2x3 grid.

#### Example:
- Plain Text: "HELLO"
- Braille: ⠓⠑⠇⠇⠕

## [Unit Alteration](unit.py)
The unit conversion section provides conversion functionalities for various units:

### [Currency](currency.py)

| Column 1                     | Column 2                   | Column 3                 |
|------------------------------|----------------------------|--------------------------|
| United States Dollar (USD)   | Euro (EUR)                 | Japanese Yen (JPY)       |
| British Pound (GBP)          | Swiss Franc (CHF)          | Australian Dollar (AUD)  |
| Canadian Dollar (CAD)        | Chinese Yuan (CNY)         | Swedish Krona (SEK)      |
| Norwegian Krone (NOK)        | South Korean Won (KRW)     | Singapore Dollar (SGD)   |
| New Zealand Dollar (NZD)     | Hong Kong Dollar (HKD)     | Danish Krone (DKK)       |
| Indian Rupee (INR)           | Brazilian Real (BRL)       | Russian Ruble (RUB)      |
| South African Rand (ZAR)     | Turkish Lira (TRY)         | Mexican Peso (MXN)       |
| Indonesian Rupiah (IDR)      | Saudi Riyal (SAR)          | Argentine Peso (ARS)     |
| Taiwanese Dollar (TWD)       | Thai Baht (THB)            | Polish Złoty (PLN)       |
| Israeli New Shekel (ILS)     | Philippine Peso (PHP)      | Malaysian Ringgit (MYR)  |
| Czech Koruna (CZK)           | Hungarian Forint (HUF)     | UAE Dirham (AED)         |
| Colombian Peso (COP)         | Egyptian Pound (EGP)       | Chilean Peso (CLP)       |
| Romanian Leu (RON)           | Nigerian Naira (NGN)       | Pakistani Rupee (PKR)    |
| Qatari Riyal (QAR)           | Ukrainian Hryvnia (UAH)    | Peruvian Sol (PEN)       |
| Vietnamese Đồng (VND)        | Bangladeshi Taka (BDT)     | Kenyan Shilling (KES)    |
| Iraqi Dinar (IQD)            | Iranian Rial (IRR)         | Kuwaiti Dinar (KWD)      |
| Lebanese Pound (LBP)         | Nepalese Rupee (NPR)       | Omani Rial (OMR)         |
| Sri Lankan Rupee (LKR)       | Syrian Pound (SYP)         | Yemeni Rial (YER)        |
| Zimbabwean Dollar (ZWD)      |                            |                          |


### [Length](length.py)
- Decimeter (dm)
- Light Year (ly)
- Millimeter (mm)
- Kilometer (km)
- Centimeter (cm)
- Meter (m)
- Micrometer (um)
- Parsec (pc)
- Astronomical Unit (au)
- Picometer (pm)
- Nanometer (nm)
- Furlong (fur)
- Yard (yd)
- Nautical Mile (nmi)
- Foot (ft)
- Mile (mi)
- Inch (in)

### [Area](area.py)
- Square Meter (m²)
- Square Decimeter (dm²)
- Square Centimeter (cm²)
- Square Kilometer (km²)
- Square Millimeter (mm²)
- Are (ar)
- Hectare (ha)
- Square Mile (mi²)
- Square Rod (rd²)
- Square Yard (yd²)
- Square Foot (ft²)
- Acre (ac)
- Square Inch (in²)

### [Volume](volume.py)
- Hectolitre (hl)
- Cubic Meter (m³)
- Cubic Centimeter (cm³)
- Decilitre (dl)
- Centilitre (cl)
- Cubic Decimeter (dm³)
- Litre (l)
- Cubic Millimeter (mm³)
- Millilitre (ml)
- Cubic Foot (ft³)
- US Fluid Ounce (US fl oz)
- Cubic Yard (yd³)
- Cubic Inch (in³)
- Acre-Foot (af)
- UK Gallon (UK gal)
- US Gallon (US gal)
- UK Fluid Ounce (UK fl oz)

### [Weight](weight.py)
- Gram (g)
- Microgram (µg)
- Quintal (q)
- Carat (ct)
- Tonne (t)
- Milligram (mg)
- Kilogram (kg)
- Short Ton (short ton)
- Long Ton (long ton)
- Ounce (oz)
- Grain (gr)
- Dram (dr)
- Pound (lb)
- Stone (st)

### [Temperature](temperature.py)
- Degree Rankine (°R)
- Degree Celsius (°C)
- Degree Reaumur (°Re)
- Degree Fahrenheit (°F)
- Kelvin (K)

### [Speed](speed.py)
- Speed of Light (c)
- Kilometer per Second (km/s)
- Mile per Hour (mph)
- Mach (ma)
- Inch per Second (in/s)
- Meter per Second (m/s)
- Kilometer per Hour (km/h)

### [Pressure](pressure.py)
- Millimeter of Water (mmw)
- Pounds per Square Foot (psf)
- Kilogram-force per Square Centimeter (kgf/cm²)
- Pounds per Square Inch (psi)
- Millimeter of Mercury (mmHg)
- Bar (bar)
- Inch of Mercury (inHg)
- Millibar (mbar)
- Hectopascal (hPa)
- Standard Atmosphere (atm)
- Kilopascal (kPa)
- Kilogram-force per Square Meter (kgf/m²)
- Megapascal (MPa)

### [Power](power.py)
- Joule per Second (j/s)
- British Thermal Unit per Second (btu/s)
- Metric Horsepower (ps)
- Kilogram-metre per Second (kgm/s)
- Kilocalorie per Second (kcal/s)
- Watt (w)
- Imperial Horsepower (hp)
- Foot-pound per Second (ftlb/s)
- Newton-metre per Second (nm/s)
- Kilowatt (kw)

### [Time](times.py)
- Planck Time (ps)
- Yoctosecond (y)
- Zeptosecond (z)
- Attosecond (a)
- Femtosecond (f)
- Picosecond (p)
- Nanosecond (n)
- Microsecond (u)
- Millisecond (m)
- Second (s)
- Minute (min)
- Hour (h)
- Day (d)
- Week (w)
- Month (mo)
- Quarter (q)
- Year (y)
- Decade (dec)
- Century (c)
- Millennium (M)

### [Data Storage](data.py)
- Yottabyte (YB)
- Zettabyte (ZB)
- Exabyte (EB)
- Petabyte (PB)
- Terabyte (TB)
- Gigabyte (GB)
- Megabyte (MB)
- Kilobyte (KB)
- Byte (B)
- Bit (b)
- Nibble (n)

## [File Format Modification](file.py)
The file format conversion section offers conversion functionalities for different file formats:

### [Image Conversion](image.py)
- JPEG
- PNG
- PDF
- WEBP
- BMP
- TIFF
- ICO
- GIF

### [Audio Conversion](audio.py)
- MP3
- FLAC
- WAV
- OGG
- AAC
- M4A

### [Video Conversion](video.py)
- MP4
- MKV
- MOV
- AVI
- WEBM
- GIF
- WMV
- FLV

### [Document Conversion](documents.py)
- DOCX
- PDF
- TXT

### [Archive Conversion](archive.py)
- ZIP
- RAR
- 7Z
- TAR
- GZIP
- BZIP2
- CAB

## Python Library Requirements(requirements.txt)
The project requires the following Python libraries, which can be installed using `pip install -r requirements.txt`:

- os
- shutil
- tkinter
- zipfile
- rarfile
- py7zr
- tarfile
- gzip
- bz2
- pycabinet
- tabulate
- moviepy
- forex-python
- docx
- PyPDF2
- Pillow
- pyttsx3
- qrcode


## Directions to Use:

1. **Clone the Repository:**
    - Clone the GitHub repository to your local machine using the following command:
      ```
      git clone https://github.com/pratham-pai/Entity-Manipulation-and-Cryptography
      ```

2. **Install Dependencies:**
    - Navigate to the project directory and install the [required Python libraries](requirements.txt) by running:
      ```
      pip install -r requirements.txt
      ```

3. **Run the Application:**
    - Once the dependencies are installed, execute the [app.py](app.py) file using Python to launch the application:
      ```
      python app.py
      ```
    - Follow the on-screen prompts and menu options to perform various conversions and cryptographic operations.


## Conclusion 

- The "Entity Manipulation and Cryptography" project offers an extensive range of conversion functionalities, making it a versatile tool for various purposes. Users can effortlessly convert text to different representations such as Morse code and Braille, perform cryptographic operations like encryption and decryption using popular algorithms, and convert units across diverse categories.

- Furthermore, the project provides comprehensive file format conversion capabilities, allowing users to convert images, audio files, videos, documents, and archives to different formats. This feature enhances file compatibility and ensures seamless data interchange across different platforms and applications.

- We encourage users to explore further and discover the full range of functionalities this project has to offer.


## License
This project is licensed under the [MIT License](LICENSE).
