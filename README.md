# 🐱 ASCIICAT

A random ASCII art cat generator to brighten your terminal!

## Features

- 🎲 Generate random ASCII cats from a collection of 10 different designs
- 🌈 Random color support
- 🔊 Random meow sounds
- 📊 Generate multiple cats at once
- 🚀 Easy to use command-line interface

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ASCIICAT.git
cd ASCIICAT

# Make the script executable
chmod +x asciicat.py

# Or install with pip (optional)
pip install -e .
```

## Usage

### Basic usage
```bash
python3 asciicat.py
```

### With random colors
```bash
python3 asciicat.py --color
```

### With meow sounds
```bash
python3 asciicat.py --meow
```

### Generate multiple cats
```bash
python3 asciicat.py -n 5 -c -m
```

### Available options
- `-c, --color`: Add random colors to the cat
- `-m, --meow`: Add a random meow sound
- `-n, --number`: Number of cats to generate (default: 1)
- `-h, --help`: Show help message

## Example outputs

### Classic sitting cat
```
     /\_/\
    ( o.o )
     > ^ <
```

### Sleeping cat
```
     /\_/\
    ( -.- )
     > ^ <
```

### Happy cat
```
     /\_/\
    ( ^.^ )
     > ^ <
```

### Big chubby cat
```
      /\___/\
     (  o   o  )
    (     U     )
     \  ___  /
      \_____/
```

### Cat with tongue out
```
     /\_/\
    ( o.o )
     >:P <
```

### Minimalist cat
```
   /\_/\
  ( . .)
   )___(
```

### With colors and meows
```bash
$ python3 asciicat.py -c -m -n 2
```
Output (with colors):
```
     /\_/\
    ( O.O )
     > ^ <
    Nya~

      /\___/\
     (  o   o  )
      )  L  (
     (   v   )
    ^^m^^^^^^m^^
    Purr...
```

## Contributing

Contributions are welcome! Feel free to:
- Add new cat designs
- Improve colors and styling
- Add new features
- Fix bugs

## License

MIT License - see the LICENSE file for details.

---

Made with ❤️ and lots of coffee ☕